# TN3216: Supporting touch input for games on macOS

**Framework**: Technotes  
**Role**: Technote

Let players interact with your game through touch on a Mac with a touch display or a Sidecar-connected iPad.

## Overview

On a Mac with a touch display or a Sidecar-connected iPad, AppKit emulates mouse events from touch, so existing games can receive touch input with little or no code change. This guidance focuses on configurations common in games, such as an app with a single view backed by a [`CAMetalLayer`](../QuartzCore/cametallayer.md). For more information about touch support in AppKit, including the view hierarchy and hit-testing mechanism, see [Handling AppKit gestures](../AppKit/handling-appkit-gestures.md).

Run your game on a Mac with a touch display or a Sidecar-connected iPad to see how it responds to touch. Standard AppKit controls, such as text fields and buttons, support touch automatically. Content that relies on hover, mouse movement deltas, or other pointer-only behavior, such as a map that reveals details when the pointer rests on a location, needs updates for touch.

## Extend the player experience meaningfully

Touch extends the Mac experience rather than replacing other input. Players don’t use touch on a Mac the way they use it on iPhone, where they often hold the device with both hands. Different game styles suit different input devices. For example, first-person shooters work best with a keyboard and mouse, and third-person adventures are generally more enjoyable with a game controller. Touch works best for brief interactions that complement these devices.

Apply these guidelines so touch complements other input:

- Give players who use touch the same information and actions that mouse and game controller players have, so touch doesn’t put them at a disadvantage.
- Design touch interactions for brief moments that the player can complete with one hand, while the other hand stays on the keyboard, mouse, or controller.
- Identify the interactions players reasonably expect from touch, such as inventory management, map zoom and scroll, or the settings menu.

When touch covers these interactions well, it feels like a natural extension of your game without changing how the game plays with other input devices.

## Understand automatic touch support in existing games

Existing games get touch support automatically. AppKit emulates mouse events from a single finger tapping or dragging, so your game receives touch as mouse input without code changes. AppKit applies game-specific emulation to apps in a games category, and can apply emulation to an individual view, such as one that hosts a third-party UI framework. To turn off the emulation, see [Opt out of mouse emulation](./tn3216-supporting-touch-input-for-games-on-macos.md#Opt-out-of-mouse-emulation).

If your game’s engine doesn’t handle touch directly, your game receives touch as mouse input. A tap arrives as a click, so interfaces that respond only to clicks, such as menus and buttons, work with touch without changes. Interfaces that depend on mouse movement deltas, hover, or other pointer-only behavior need updates, because touch doesn’t report movement between taps and has no hover state.

A mouse moves continuously from one position to the next, but a player can tap or start a drag at two distant locations in succession. If your game tracks the pointer by adding up the movement deltas from [`mouseMoved(with:)`](../AppKit/nsresponder/mousemoved%28with%29.md) and [`mouseDragged(with:)`](../AppKit/nsresponder/mousedragged%28with%29.md) events, the tracked position drifts away from where the player touched. Instead, read the location from the event itself. For games, AppKit sends a `mouseMoved` event to the new location before each [`mouseDown(with:)`](../AppKit/nsresponder/mousedown%28with%29.md), so your game can refresh its cached mouse position.

If the [`LSApplicationCategoryType`](../BundleResources/information-property-list/lsapplicationcategorytype.md) value in your information property list is `public.app-category.games` or a game subcategory such as `public.app-category.action-games`, the system applies game-specific mouse emulation.

Specifically for games, AppKit sends these ordered mouse events for a single tap:

- [`mouseMoved(with:)`](../AppKit/nsresponder/mousemoved%28with%29.md), from the last mouse position to the tap location
- [`mouseDown(with:)`](../AppKit/nsresponder/mousedown%28with%29.md)
- [`mouseUp(with:)`](../AppKit/nsresponder/mouseup%28with%29.md)

For a drag, AppKit sends these mouse events, in this order:

- [`mouseMoved(with:)`](../AppKit/nsresponder/mousemoved%28with%29.md), to the location where the drag begins
- [`mouseDown(with:)`](../AppKit/nsresponder/mousedown%28with%29.md)
- [`mouseDragged(with:)`](../AppKit/nsresponder/mousedragged%28with%29.md), repeatedly while the touch continues
- [`mouseUp(with:)`](../AppKit/nsresponder/mouseup%28with%29.md)

> ❗ **Important**: Don’t intercept events by overriding [`sendEvent(_:)`](../AppKit/nsapplication/sendevent%28_%29.md) or pulling them with [`nextEvent(matching:until:inMode:dequeue:)`](../AppKit/nsapplication/nextevent%28matching,until,inmode,dequeue%29.md). Doing so can interfere with gesture recognizers that respond to a physical mouse.

## Understand GCMouse emulation

Games can read mouse events from [`GCMouse`](../GameController/gcmouse.md) for low-latency mouse input. By default, the system presents each touch surface, whether a Mac with a touch display or a Sidecar-connected iPad, as an additional `GCMouse` that emulates mouse input from touches:

- A finger touching down presses the left button.
- Moving the finger calls [`mouseMovedHandler`](../GameController/gcmouseinput/mousemovedhandler.md) with the movement delta.
- Lifting the finger releases the button.

The emulated `GCMouse` ignores additional fingers, and it doesn’t emulate other buttons, scrolling, or pinch input. Because a player can touch disconnected locations, the emulated deltas don’t represent continuous pointer movement. Don’t use them to track an absolute pointer position. To stop the system from presenting touch as a `GCMouse`, opt out of mouse emulation.

## Opt out of mouse emulation

To opt out of mouse emulation, add the [`NSIsTouchNative`](../BundleResources/information-property-list/nsistouchnative.md) key to your app’s information property list and set it to `YES`. AppKit’s emulation will stick to a generic emulation - ignoring the app’s category or whether it uses a third-party UI framework - and disable `GCMouse` emulation. Setting this key to `YES` has the following effects:

- The system no longer presents the touch surface of a Mac with a touch display or a Sidecar-connected iPad as an additional `GCMouse` device.
- Your game receives touch through gesture recognizers instead of emulated mouse events.

AppKit still emulates mouse events for any [`NSView`](../AppKit/nsview.md) that handles them, for example by overriding `mouseDown:`. To handle touch directly in such a view, add an [`NSGestureRecognizer`](../AppKit/nsgesturerecognizer.md) that allows direct touch to that view.

## Implement touch events

After you decide where touch fits in your game, handle touch directly with gesture recognizers to support gestures such as pinch to zoom, two-finger rotate, and other multi-finger interactions. Opt out of mouse emulation, and then:

1. Add gesture recognizers to your game view.
2. Implement the action method for each gesture recognizer.
3. In an object that conforms to [`NSGestureRecognizerDelegate`](../AppKit/nsgesturerecognizerdelegate.md), specify which gestures the system can recognize together and which it can’t.

> **Note**: The gesture recognizers must include [`direct`](../AppKit/nstouch/touchtypemask/direct.md) in [`allowedTouchTypes`](../AppKit/nsgesturerecognizer/allowedtouchtypes.md). On macOS 27 and later, this is the default.

The following example registers gesture recognizers in an [`NSViewController`](../AppKit/nsviewcontroller.md). The `handleTap:` and `handlePinch:` action methods follow the same pattern as `handlePan:`, which appears later in this article.

**Swift**:

```swift
// One-time setup, typically in an NSViewController
// that conforms to NSGestureRecognizerDelegate.
// Store the recognizers as properties so the delegate
// methods below can reference them.

pan = NSPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
pan.buttonMask = 0 // Do not react to a physical mouse.
pan.delegate = self
gameView.addGestureRecognizer(pan)

tap = NSClickGestureRecognizer(target: self, action: #selector(handleTap(_:)))
tap.buttonMask = 0 // Do not react to a physical mouse.
tap.delegate = self
gameView.addGestureRecognizer(tap)

pinch = NSMagnificationGestureRecognizer(target: self, action: #selector(handlePinch(_:)))
pinch.delegate = self
gameView.addGestureRecognizer(pinch)
```

**Objective-C**:

```objc
// One-time setup, typically in an NSViewController
// that conforms to <NSGestureRecognizerDelegate>.
// Store the recognizers as properties so the delegate
// methods below can reference them.

self.pan = [[NSPanGestureRecognizer alloc] initWithTarget:self action:@selector(handlePan:)];
self.pan.buttonMask = 0; // Do not react to a physical mouse.
self.pan.delegate = self;
[self.gameView addGestureRecognizer:self.pan];

self.tap = [[NSClickGestureRecognizer alloc] initWithTarget:self action:@selector(handleTap:)];
self.tap.buttonMask = 0; // Do not react to a physical mouse.
self.tap.delegate = self;
[self.gameView addGestureRecognizer:self.tap];

self.pinch = [[NSMagnificationGestureRecognizer alloc] initWithTarget:self action:@selector(handlePinch:)];
self.pinch.delegate = self;
[self.gameView addGestureRecognizer:self.pinch];
```

The following example lets the system recognize pan and pinch together and makes tap wait for both to fail:

**Swift**:

```swift
// NSGestureRecognizerDelegate: allow only pan and pinch to be recognized together.
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
                       shouldRecognizeSimultaneouslyWith other: NSGestureRecognizer) -> Bool {
    (gestureRecognizer === pan || gestureRecognizer === pinch) &&
        (other === pan || other === pinch)
}

// NSGestureRecognizerDelegate: a tap must wait for pan/pinch to fail,
// so it doesn't fire in the middle of a drag or pinch.
func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer,
                       shouldRequireFailureOf other: NSGestureRecognizer) -> Bool {
    gestureRecognizer === tap && (other === pan || other === pinch)
}
```

**Objective-C**:

```objc
// NSGestureRecognizerDelegate: allow only pan and pinch to be recognized together.
- (BOOL)gestureRecognizer:(NSGestureRecognizer *)gestureRecognizer
        shouldRecognizeSimultaneouslyWithGestureRecognizer:(NSGestureRecognizer *)other {
    return (gestureRecognizer == self.pan || gestureRecognizer == self.pinch) &&
           (other == self.pan || other == self.pinch);
}

// NSGestureRecognizerDelegate: a tap must wait for pan/pinch to fail,
// so it doesn't fire in the middle of a drag or pinch.
- (BOOL)gestureRecognizer:(NSGestureRecognizer *)gestureRecognizer
        shouldRequireFailureOfGestureRecognizer:(NSGestureRecognizer *)other {
    return gestureRecognizer == self.tap &&
           (other == self.pan || other == self.pinch);
}
```

### Route gestures in your game engine

Games typically have several input contexts, such as gameplay, a main menu, and a mini-map, and each context reacts differently to the same gesture. To handle this, use the gesture recognizers as a single entry point and let your engine route the gestures to whichever input handler is active:

1. Install the gesture recognizers once in your app and leave them enabled.
2. Convert recognizer callbacks into your engine’s input events and send them to the active input handler (for example, the character, main menu, or mini-map input handler).
3. Let the active input handler decide if and how to react to different gestures.

The following example, in the same `NSViewController` that registered the recognizers, converts a pan gesture into an engine input event and sends it to the active input handler:

**Swift**:

```swift
@objc func handlePan(_ gesture: NSPanGestureRecognizer) {
    let deltaPts = gesture.translation(in: gameView)
    let scale = gameView.window?.backingScaleFactor ?? 1
    gesture.setTranslation(.zero, in: gameView) // Reset it so the next callback reports a fresh delta.

    // Convert points to pixels. Invert the y-axis if your engine's origin is at the top left,
    // because AppKit's origin is at the bottom left.
    Game.currentInputHandler.onPan(deltaPts.x * scale, -deltaPts.y * scale)
}
```

**Objective-C**:

```objcpp
- (void)handlePan:(NSPanGestureRecognizer *)gesture {
    const NSPoint deltaPts = [gesture translationInView:self.gameView];
    const CGFloat scale = self.gameView.window.backingScaleFactor;
    [gesture setTranslation:NSZeroPoint inView:self.gameView]; // Reset it so the next callback reports a fresh delta.

    // Convert points to pixels. Invert the y-axis if your engine's origin is at the top left,
    // because AppKit's origin is at the bottom left.
    Game::GetCurrentInputHandler()->OnPan(deltaPts.x * scale, -deltaPts.y * scale);
}
```

The following input handlers show how the mini-map pans its content and how gameplay ignores the gesture:

```cpp
// C++ virtual function that handles pan events in the mini-map.
void MiniMapInputHandler::OnPan(float dx, float dy)
{
    // Implement map pan.
    mapLocation.x += dx;
    mapLocation.y += dy;
}

// C++ virtual function that handles pan events during gameplay.
void GameplayInputHandler::OnPan(float, float)
{
    // Nothing to do during gameplay.
    // Gameplay is driven by the physical mouse (GCMouse), keyboard, or controller.
    return;
}
```

### Use standard AppKit controls for automatic touch support

Standard AppKit controls, such as a text field for a player name or buttons in a settings panel, support touch automatically. For example, a tap places the caret in a text field or presses a button. The controls keep this behavior after you set `NSIsTouchNative` to `YES` and handle touch in your own view, as long as you don’t attach your own direct-touch gesture recognizers to them.

For more information about how AppKit gathers gesture recognizers, including the view hierarchy and hit-testing mechanism, see [Handling AppKit gestures](../AppKit/handling-appkit-gestures.md).

## Review your touch integration

After you make your changes, use this checklist to verify that your game handles touch correctly.

If your game relies on mouse emulation:

- Read the location from each mouse event instead of using a cached pointer location.
- Don’t intercept events by overriding `sendEvent:` or pulling them with `nextEventMatchingMask:`.

If your game handles touch directly:

- Set `NSIsTouchNative` to `YES`.
- Use direct-touch gesture recognizers, and set [`buttonMask`](../AppKit/nsclickgesturerecognizer/buttonmask.md) to `0` so they don’t respond to a physical mouse.
- Add touch to interactions players reasonably expect from it, such as inventory management, map zoom and scroll, or the settings menu, and make them usable with one hand alongside other input methods.
- Continue to read `GCMouse` for the physical mouse. With `NSIsTouchNative` set, touch no longer appears as an emulated `GCMouse`.
- Use standard AppKit controls where possible. They continue to support touch as long as you don’t attach your own direct-touch gesture recognizers to them.

## Revision History

- **2026-10-28** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3216-supporting-touch-input-for-games-on-macos)*