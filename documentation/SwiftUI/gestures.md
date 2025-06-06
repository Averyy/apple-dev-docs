# Gestures

**Framework**: SwiftUI

Define interactions from taps, clicks, and swipes to fine-grained gestures.

#### Overview

Respond to gestures by adding gesture modifiers to your views. You can listen for taps, drags, pinches, and other standard gestures.

![None](https://docs-assets.developer.apple.com/published/6a1478e9bc9c150def717738cb949d52/gestures-hero%402x.png)

You can also compose custom gestures from individual gestures using the [`simultaneously(with:)`](gesture/simultaneously(with:).md), [`sequenced(before:)`](gesture/sequenced(before:).md), or [`exclusively(before:)`](gesture/exclusively(before:).md) modifiers, or combine gestures with keyboard modifiers using the [`modifiers(_:)`](gesture/modifiers(_:).md) modifier.

> ❗ **Important**: When you need a button, use a [`Button`](button.md) instance rather than a tap gesture. You can use any view as the button’s label, and the button type automatically provides many of the standard behaviors that users expect from a button, like accessibility labels and hints.

When you need a button, use a [`Button`](button.md) instance rather than a tap gesture. You can use any view as the button’s label, and the button type automatically provides many of the standard behaviors that users expect from a button, like accessibility labels and hints.

For design guidance, see [`Gestures`](https://developer.apple.com/design/Human-Interface-Guidelines/gestures) in the Human Interface Guidelines.

## Topics

### Essentials
- [Adding interactivity with gestures](adding-interactivity-with-gestures.md)
  Use gesture modifiers to add interactivity to your app.
### Recognizing tap gestures
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](view/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onTapGesture(count:coordinateSpace:perform:)](view/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [struct TapGesture](tapgesture.md)
  A gesture that recognizes one or more taps.
- [struct SpatialTapGesture](spatialtapgesture.md)
  A gesture that recognizes one or more taps and reports their location.
### Recognizing long press gestures
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:).md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [struct LongPressGesture](longpressgesture.md)
  A gesture that succeeds when the user performs a long press.
### Recognizing spatial events
- [struct SpatialEventGesture](spatialeventgesture.md)
  A gesture that provides information about ongoing spatial events like clicks and touches.
- [struct SpatialEventCollection](spatialeventcollection.md)
  A collection of spatial input events that target a specific view.
- [enum Chirality](chirality.md)
  The chirality, or handedness, of a pose.
### Recognizing gestures that change over time
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](view/gesture(_:).md)
  Attaches a [`UIGestureRecognizerRepresentable`](uigesturerecognizerrepresentable.md) to the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](view/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](view/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](view/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [struct DragGesture](draggesture.md)
  A dragging motion that invokes an action as the drag-event sequence changes.
- [struct WindowDragGesture](windowdraggesture.md)
  A gesture that recognizes the motion of and handles dragging a window.
- [struct MagnifyGesture](magnifygesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [struct RotateGesture](rotategesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [struct RotateGesture3D](rotategesture3d.md)
  A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [struct GestureMask](gesturemask.md)
  Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.
### Recognizing Apple Pencil gestures
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](view/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](view/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [var preferredPencilDoubleTapAction: PencilPreferredAction](environmentvalues/preferredpencildoubletapaction.md)
  The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [var preferredPencilSqueezeAction: PencilPreferredAction](environmentvalues/preferredpencilsqueezeaction.md)
  The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [struct PencilPreferredAction](pencilpreferredaction.md)
  An action that the user prefers to perform after double-tapping their Apple Pencil.
- [struct PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md)
  Describes the value of an Apple Pencil double-tap gesture.
- [struct PencilSqueezeGestureValue](pencilsqueezegesturevalue.md)
  Describes the value of an Apple Pencil squeeze gesture.
- [enum PencilSqueezeGesturePhase](pencilsqueezegesturephase.md)
  Describes the phase and value of an Apple Pencil squeeze gesture.
- [struct PencilHoverPose](pencilhoverpose.md)
  A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.
### Combining gestures
- [Composing SwiftUI gestures](composing-swiftui-gestures.md)
  Combine gestures to create complex interactions.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](view/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](view/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [struct SequenceGesture](sequencegesture.md)
  A gesture that’s a sequence of two gestures.
- [struct SimultaneousGesture](simultaneousgesture.md)
  A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [struct ExclusiveGesture](exclusivegesture.md)
  A gesture that consists of two gestures where only one of them can succeed.
### Defining custom gestures
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](view/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](view/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func defersSystemGestures(on: Edge.Set) -> some View](view/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [protocol Gesture](gesture.md)
  An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [struct AnyGesture](anygesture.md)
  A type-erased gesture.
- [struct HandActivationBehavior](handactivationbehavior.md)
  An activation behavior specific to hand-driven input.
- [struct HandGestureShortcut](handgestureshortcut.md)
  Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.
### Managing gesture state
- [struct GestureState](gesturestate.md)
  A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.
- [struct GestureStateGesture](gesturestategesture.md)
  A gesture that updates the state provided by a gesture’s updating callback.
### Handling activation events
- [func allowsWindowActivationEvents(Bool?) -> some View](view/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
### Deprecated gestures
- [struct MagnificationGesture](magnificationgesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [struct RotationGesture](rotationgesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.

## See Also

- [Input events](input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md)
  Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Drag and drop](drag-and-drop.md)
  Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](focus.md)
  Identify and control which visible object responds to user interaction.
- [System events](system-events.md)
  React to system events, like opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gestures)*