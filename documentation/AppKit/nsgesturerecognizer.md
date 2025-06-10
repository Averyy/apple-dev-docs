# NSGestureRecognizer

**Framework**: AppKit  
**Kind**: class

An object that monitors events and calls its action method when a predefined sequence of events occur.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSGestureRecognizer
```

#### Overview

A gesture recognizer might recognize a single click, a click and drag, or a sequence of events that imply rotation. You do not create instances of this class directly. This class is an abstract base class that defines the common behavior for all gesture recognizers. When using a gesture recognizer in your app, create an instance of one of the concrete subclasses.

The concrete subclasses of [`NSGestureRecognizer`](nsgesturerecognizer.md) are the following:

- [`NSClickGestureRecognizer`](nsclickgesturerecognizer.md)
- [`NSMagnificationGestureRecognizer`](nsmagnificationgesturerecognizer.md)
- [`NSPanGestureRecognizer`](nspangesturerecognizer.md)
- [`NSPressGestureRecognizer`](nspressgesturerecognizer.md)
- [`NSRotationGestureRecognizer`](nsrotationgesturerecognizer.md)

A gesture recognizer operates on events in a specific view (or in any of that view’s subviews). After creating a gesture recognizer, attach it to one of your views using the [`addGestureRecognizer(_:)`](nsview/addgesturerecognizer(_:).md) method. Events received by your app are forwarded automatically to any relevant gesture recognizers before they are sent to the corresponding view. The gesture recognizer can delay the further progression of the events until recognition is complete or allow the events to be delivered normally.

A gesture recognizer can detect gestures that are either discrete or continuous in nature. A click gesture is discrete because it involves a mouse-down and mouse-up event without any mouse movements in between. By contrast, a pan or rotation gesture is continuous because it involves tracking mouse movements over a period of time.

During the gesture recognition process, a gesture recognizer calls the action method of its associated target object to report the state of the recognition process. For discrete gestures, the action method is typically called only once when the gesture is recognized. For continuous gestures, it may be called multiple times depending on the current state of the gesture recognizer. In that situation, you can use your action method to perform appropriate tasks, such as creating animations for any mouse-related movements, in addition to handling the final results of the gesture recognition process.

A gesture recognizer has only one action method and one target object, and the method must conform to one of the following signatures:

When your code needs additional information about the particulars of a gesture, define your action method to include the gesture recognizer parameter. You almost always want the gesture recognizer object when handling continuous gestures. For example, for a rotation gesture, you would use the gesture recognizer object to get the updated rotation value. You can also use the gesture recognizer object to get the location of where the gesture occurred.

##### State Transitions

Gesture recognizers operate within a predefined state machine, transitioning from state to state as they handle events. All gesture recognizers begin in the Possible ([`NSGestureRecognizer.State.possible`](nsgesturerecognizer/state-swift.enum/possible.md)) state, but the possible transitions differ for continuous and discrete gestures.

Discrete gestures transition from the Possible state directly to the Recognized ([`recognized`](nsgesturerecognizer/state-swift.enum/recognized.md)) or Failed ([`NSGestureRecognizer.State.failed`](nsgesturerecognizer/state-swift.enum/failed.md)) state, depending on whether they successfully interpret the gesture. When a discrete gesture recognizer transitions to the Recognized state, it calls the action method of its target object.

For continuous gestures, the state transitions are as follows:

- Possible —> Began —> [Changed] —> Cancelled
- Possible —> Began —> [Changed] —> Ended

The Changed state is optional and may occur multiple times before the Cancelled or Ended state is reached. Many state transitions cause the gesture recognizer to call its action method. Setting the [`state`](nsgesturerecognizer/state-swift.property.md) property to [`NSGestureRecognizer.State.changed`](nsgesturerecognizer/state-swift.enum/changed.md) while monitoring events also calls the action method. You can use these calls to update the state of your app or update any custom animations.

For a list of possible states, see the constants in [`NSGestureRecognizer.State`](nsgesturerecognizer/state-swift.enum.md).

##### Subclassing Notes

You may create a subclass of `NSGestureRecognizer` that recognizes a distinctive gesture—for example, a “check mark” gesture. A custom gesture recognizer implements any appropriate event-related methods to detect its gesture along with a few other methods for managing state information.

All gesture recognizers must update the value in the state property at appropriate times. Specifically, you must update it for all state transitions. For more information about the possible state transitions of a gesture recognizer, see [`State Transitions`](nsgesturerecognizer#State-Transitions.md).

> **Note**:  [`NSGestureRecognizer`](nsgesturerecognizer.md) does not support handing off event tracking to other non-gesture recognizer mechanisms (for example drag and drop and pop-up menus).

###### Methods to Override

When creating your own gesture recognizer subclass:

- Implement the [`reset()`](nsgesturerecognizer/reset().md) method and any other relevant methods in Methods for Subclasses.
- Override the [`location(in:)`](nsgesturerecognizer/location(in:).md) method as needed to specify an appropriate point for your gesture.

AppKit waits for a mouse-down event, magnify event, or rotation event to occur before starting the gesture recognition process. A gesture recognizer that used only key-down events to recognize its gesture would not have its [`keyDown(with:)`](nsgesturerecognizer/keydown(with:).md) method called until a mouse-down, magnify, or rotation event started the recognition process.

###### Alternatives to Subclassing

The `NSGestureRecognizer` class defines the common behaviors that can be configured for all concrete gesture recognizers. It also supports a delegate—an object that adopts the [`NSGestureRecognizerDelegate`](nsgesturerecognizerdelegate.md) protocol—for handling finer-grained customization of some behaviors without the need for subclassing. For example, you can use the delegate to create dependencies between specific gesture recognizer objects.

For more information about using the delegate to control the behavior of your gesture recognizers, see [`NSGestureRecognizerDelegate`](nsgesturerecognizerdelegate.md).

## Topics

### Initializing a Gesture Recognizer
- [init(target: Any?, action: Selector?)](nsgesturerecognizer/init(target:action:).md)
  Initializes the gesture recognizer with the specified target and action information.
### Accessing the Target and Action
- [var action: Selector?](nsgesturerecognizer/action.md)
  The action method to call when the gesture is recognized.
- [var target: AnyObject?](nsgesturerecognizer/target.md)
  The object that implements the action method.
### Getting the Location of Events
- [func location(in: NSView?) -> NSPoint](nsgesturerecognizer/location(in:).md)
  Returns the point computed as the location of the gesture.
### Accessing the Recognizer’s State
- [var state: NSGestureRecognizer.State](nsgesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [var view: NSView?](nsgesturerecognizer/view.md)
  The view to which the gesture recognizer is attached.
- [var isEnabled: Bool](nsgesturerecognizer/isenabled.md)
  A Boolean value indicating whether the gesture recognizer is able to handle events.
### Delaying Events
- [var delaysPrimaryMouseButtonEvents: Bool](nsgesturerecognizer/delaysprimarymousebuttonevents.md)
  A Boolean value that indicates whether primary mouse button events are delivered only after gesture recognition fails.
- [var delaysSecondaryMouseButtonEvents: Bool](nsgesturerecognizer/delayssecondarymousebuttonevents.md)
  A Boolean value that indicates whether secondary mouse button events are delivered only after gesture recognition fails.
- [var delaysOtherMouseButtonEvents: Bool](nsgesturerecognizer/delaysothermousebuttonevents.md)
  A Boolean value that indicates whether other mouse button events are delivered only after gesture recognition fails.
- [var delaysKeyEvents: Bool](nsgesturerecognizer/delayskeyevents.md)
  A Boolean value that indicates whether key events are delivered only after gesture recognition fails.
- [var delaysMagnificationEvents: Bool](nsgesturerecognizer/delaysmagnificationevents.md)
  A Boolean value that indicates whether magnification events are delivered only after gesture recognition fails.
- [var delaysRotationEvents: Bool](nsgesturerecognizer/delaysrotationevents.md)
  A Boolean value that indicates whether rotation events are delivered only after gesture recognition fails.
### Accessing the Delegate
- [var delegate: (any NSGestureRecognizerDelegate)?](nsgesturerecognizer/delegate.md)
  The delegate of the gesture recognizer.
### Methods for Subclasses
- [func reset()](nsgesturerecognizer/reset.md)
  Overridden to reset the internal state of the gesture recognizer when an attempt completes.
- [func mouseDown(with: NSEvent)](nsgesturerecognizer/mousedown(with:).md)
  Informs the gesture recognizer that the user pressed the left mouse button.
- [func mouseDragged(with: NSEvent)](nsgesturerecognizer/mousedragged(with:).md)
  Informs the gesture recognizer that the user moved the mouse with the left button pressed.
- [func mouseUp(with: NSEvent)](nsgesturerecognizer/mouseup(with:).md)
  Informs the gesture recognizer that the user released the left mouse button.
- [func otherMouseDown(with: NSEvent)](nsgesturerecognizer/othermousedown(with:).md)
  Informs the gesture recognizer that the user pressed a mouse button other than the left or right one.
- [func otherMouseDragged(with: NSEvent)](nsgesturerecognizer/othermousedragged(with:).md)
  Informs the gesture recognizer that the user moved the mouse with a button other than the left or right one pressed.
- [func otherMouseUp(with: NSEvent)](nsgesturerecognizer/othermouseup(with:).md)
  Informs the gesture recognizer that the user released a mouse button other than the left or right one.
- [func rightMouseDown(with: NSEvent)](nsgesturerecognizer/rightmousedown(with:).md)
  Informs the gesture recognizer that the user pressed the right mouse button.
- [func rightMouseDragged(with: NSEvent)](nsgesturerecognizer/rightmousedragged(with:).md)
  Informs the gesture recognizer that the user moved the mouse with the right button pressed.
- [func rightMouseUp(with: NSEvent)](nsgesturerecognizer/rightmouseup(with:).md)
  Informs the gesture recognizer that the user released the right mouse button.
- [func magnify(with: NSEvent)](nsgesturerecognizer/magnify(with:).md)
  Informs the gesture recognizer that the user is performing a pinch gesture.
- [func rotate(with: NSEvent)](nsgesturerecognizer/rotate(with:).md)
  Informs the gesture recognizer that the user is performing a rotation gesture.
- [func canBePrevented(by: NSGestureRecognizer) -> Bool](nsgesturerecognizer/canbeprevented(by:).md)
  Overridden to indicate that the specified gesture recognizer can prevent the current object from recognizing a gesture.
- [func canPrevent(NSGestureRecognizer) -> Bool](nsgesturerecognizer/canprevent(_:).md)
  Overridden to indicate that the current object can prevent the specified gesture recognizer from recognizing its gesture.
- [func shouldBeRequiredToFail(by: NSGestureRecognizer) -> Bool](nsgesturerecognizer/shouldberequiredtofail(by:).md)
  Overridden to indicate that the current object must fail before the specified gesture recognizer begins recognizing its gesture.
- [func shouldRequireFailure(of: NSGestureRecognizer) -> Bool](nsgesturerecognizer/shouldrequirefailure(of:).md)
  Overridden to indicate that the specified gesture recognizer must fail before the current object begins recognizing its gesture.
- [func keyDown(with: NSEvent)](nsgesturerecognizer/keydown(with:).md)
  Informs the gesture recognizer that the user has pressed a key.
- [func keyUp(with: NSEvent)](nsgesturerecognizer/keyup(with:).md)
  Informs the gesture recognizer that the user released a key.
- [func tabletPoint(with: NSEvent)](nsgesturerecognizer/tabletpoint(with:).md)
  Informs the user that a tablet-point event occurred.
- [func flagsChanged(with: NSEvent)](nsgesturerecognizer/flagschanged(with:).md)
  Informs the current object that the user pressed or released a modifier key (Shift, Control, and so on).
- [func pressureChange(with: NSEvent)](nsgesturerecognizer/pressurechange(with:).md)
  Informs the current object that a pressure change occurred on a system that supports pressure sensitivity.
### Configuring Pressure
- [var pressureConfiguration: NSPressureConfiguration](nsgesturerecognizer/pressureconfiguration.md)
  Configures the behavior and progression of the Force Touch trackpad when responding to recognized pressure gestures.
### Constants
- [NSGestureRecognizer.State](nsgesturerecognizer/state-swift.enum.md)
  The current state of the gesture recognizer.
### Initializers
- [init?(coder: NSCoder)](nsgesturerecognizer/init(coder:).md)
### Instance Properties
- [var allowedTouchTypes: NSTouch.TouchTypeMask](nsgesturerecognizer/allowedtouchtypes.md)
- [var modifierFlags: NSEvent.ModifierFlags](nsgesturerecognizer/modifierflags.md)
- [var name: String?](nsgesturerecognizer/name.md)
### Instance Methods
- [func touchesBegan(with: NSEvent)](nsgesturerecognizer/touchesbegan(with:).md)
  Called when one or more fingers first make contact with an [`NSTouchBar`](nstouchbar.md) instance on the Touch Bar.
- [func touchesCancelled(with: NSEvent)](nsgesturerecognizer/touchescancelled(with:).md)
  Called when a system event, such as a low-memory warning, cancels an in-progress touch event in an [`NSTouchBar`](nstouchbar.md) object.
- [func touchesEnded(with: NSEvent)](nsgesturerecognizer/touchesended(with:).md)
  Called when one or more fingers are removed from contact with an [`NSTouchBar`](nstouchbar.md) instance on the Touch Bar.
- [func touchesMoved(with: NSEvent)](nsgesturerecognizer/touchesmoved(with:).md)
  Called when one or more fingers, associated with an in-progress event, move within an [`NSTouchBar`](nstouchbar.md) instance on the Touch Bar.
- [func mouseCancelled(NSEvent)](nsgesturerecognizer/mousecancelled(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSClickGestureRecognizer](nsclickgesturerecognizer.md)
- [NSMagnificationGestureRecognizer](nsmagnificationgesturerecognizer.md)
- [NSPanGestureRecognizer](nspangesturerecognizer.md)
- [NSPressGestureRecognizer](nspressgesturerecognizer.md)
- [NSRotationGestureRecognizer](nsrotationgesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSGestureRecognizerDelegate](nsgesturerecognizerdelegate.md)
  A set of methods for fine-tuning a gesture recognizer’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer)*