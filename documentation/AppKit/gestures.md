# Gestures

**Framework**: AppKit  
**Role**: API Collection

Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.

## Overview

A gesture recognizer interprets a sequence of low-level events — mouse clicks, touches, or trackpad gestures — as a single, well-defined interaction, such as a click, a press-and-hold, a pan, a pinch, or a rotation, so you don’t have to track events yourself. Attach a gesture recognizer to a view, and it calls your action method when it recognizes that interaction, independent of the responder chain. For more information, see [Handling AppKit gestures](./handling-appkit-gestures.md).

Use one of the standard gesture recognizers when it fits your interaction:

- [`NSClickGestureRecognizer`](./nsclickgesturerecognizer.md)
- [`NSPressGestureRecognizer`](./nspressgesturerecognizer.md)
- [`NSPanGestureRecognizer`](./nspangesturerecognizer.md)
- [`NSRotationGestureRecognizer`](./nsrotationgesturerecognizer.md)
- [`NSMagnificationGestureRecognizer`](./nsmagnificationgesturerecognizer.md)

When none of them match the interaction your app needs, define a custom gesture recognizer by subclassing [`NSGestureRecognizer`](./nsgesturerecognizer.md) and use [`NSGestureRecognizerDelegate`](./nsgesturerecognizerdelegate.md) to fine-tune how it interacts with other recognizers.

Gesture recognizers are the primary way AppKit, SwiftUI, and Mac Catalyst handle input, and starting in macOS 27 they’re the only way to receive direct touch input from a Mac with a touch display. If your app currently tracks interactions by overriding [`mouseDown(with:)`](./nsresponder/mousedown%28with%29.md) and related event-handling methods, see [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md) to learn how to adopt gesture recognizers instead.

## Topics

### Gesture handling
- [Handling AppKit gestures](./handling-appkit-gestures.md)
  Use gesture recognizers to simplify input handling and create a consistent platform experience.
- [Adopting gesture recognizers in your app](./adopting-gesture-recognizers-in-your-app.md)
  Replace mouse-event overrides and tracking loops with gesture recognizers to support both existing mouse behavior and touch input on a Mac with a touch display.
### Standard gestures
- [class NSClickGestureRecognizer](./nsclickgesturerecognizer.md)
  A discrete gesture recognizer that tracks a specified number of mouse clicks.
- [class NSPressGestureRecognizer](./nspressgesturerecognizer.md)
  A discrete gesture recognizer that tracks whether the user holds down a mouse button for a minimum amount of time before releasing it.
- [class NSPanGestureRecognizer](./nspangesturerecognizer.md)
  A continuous gesture recognizer for panning gestures.
- [class NSRotationGestureRecognizer](./nsrotationgesturerecognizer.md)
  A continuous gesture recognizer that tracks two trackpad touches moving opposite each other in a circular motion.
- [class NSMagnificationGestureRecognizer](./nsmagnificationgesturerecognizer.md)
  A continuous gesture recognizer that tracks a pinch gesture that magnifies content.
### Custom gestures
- [class NSGestureRecognizer](./nsgesturerecognizer.md)
  An object that monitors events and calls its action method when a predefined sequence of events occur.
- [protocol NSGestureRecognizerDelegate](./nsgesturerecognizerdelegate.md)
  A set of methods for fine-tuning a gesture recognizer’s behavior.

## See Also

### User Interactions
- [Mouse, Keyboard, and Trackpad](./mouse-keyboard-and-trackpad.md)
  Handle events related to mouse, keyboard, and trackpad input.
- [Menus, Cursors, and the Dock](./menus-cursors-and-the-dock.md)
  Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.
- [Touch Bar](./touch-bar.md)
  Display interactive content and controls in the Touch Bar.
- [Drag and Drop](./drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Accessibility for AppKit](./accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/gestures)*