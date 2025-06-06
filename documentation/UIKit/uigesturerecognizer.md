# UIGestureRecognizer

**Framework**: UIKit  
**Kind**: class

The base class for concrete gesture recognizers.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIGestureRecognizer
```

#### Overview

A  decouples the logic for recognizing a sequence of touches (or other input) and acting on that recognition. When one of these objects recognizes a common gesture or, in some cases, a change in the gesture, it sends an action message to each designated target object.

The concrete subclasses of [`UIGestureRecognizer`](uigesturerecognizer.md) are the following:

- [`UITapGestureRecognizer`](uitapgesturerecognizer.md)
- [`UIPinchGestureRecognizer`](uipinchgesturerecognizer.md)
- [`UIRotationGestureRecognizer`](uirotationgesturerecognizer.md)
- [`UISwipeGestureRecognizer`](uiswipegesturerecognizer.md)
- [`UIPanGestureRecognizer`](uipangesturerecognizer.md)
- [`UIScreenEdgePanGestureRecognizer`](uiscreenedgepangesturerecognizer.md)
- [`UILongPressGestureRecognizer`](uilongpressgesturerecognizer.md)
- [`UIHoverGestureRecognizer`](uihovergesturerecognizer.md)

The [`UIGestureRecognizer`](uigesturerecognizer.md) class defines a set of common behaviors that can be configured for all concrete gesture recognizers. It can also communicate with its delegate (an object that adopts the [`UIGestureRecognizerDelegate`](uigesturerecognizerdelegate.md) protocol), thereby enabling finer-grained customization of some behaviors.

A gesture recognizer operates on touches hit-tested to a specific view and all of that view’s subviews. It thus must be associated with that view. To make that association you must call the [`UIView`](uiview.md) method [`addGestureRecognizer(_:)`](uiview/addgesturerecognizer(_:).md). A gesture recognizer doesn’t participate in the view’s responder chain.

A gesture recognizer has one or more target-action pairs associated with it. If there are multiple target-action pairs, they’re discrete, and not cumulative. Recognition of a gesture results in the dispatch of an action message to a target for each of the associated pairs. The action methods invoked must conform to one of the following signatures:

Methods conforming to the latter signature permit the target in some cases to query the gesture recognizer sending the message for additional information. For example, the target could ask a [`UIRotationGestureRecognizer`](uirotationgesturerecognizer.md) object for the angle of rotation (in radians) since the last invocation of the action method for this gesture. Clients of gesture recognizers can also ask for the location of a gesture by calling [`location(in:)`](uigesturerecognizer/location(in:).md) or [`location(ofTouch:in:)`](uigesturerecognizer/location(oftouch:in:).md).

The gesture interpreted by a gesture recognizer can be either discrete or continuous. A discrete gesture, such as a double tap, occurs but once in a multi-touch sequence and results in a single action sent. However, when a gesture recognizer interprets a continuous gesture such as a rotation gesture, it sends an action message for each incremental change until the multi-touch sequence concludes.

A window delivers touch events to a gesture recognizer before it delivers them to the hit-tested view attached to the gesture recognizer. Generally, if a gesture recognizer analyzes the stream of touches in a multi-touch sequence and doesn’t recognize its gesture, the view receives the full complement of touches. If a gesture recognizer recognizes its gesture, the remaining touches for the view are canceled. The usual sequence of actions in gesture recognition follows a path determined by default values of the [`cancelsTouchesInView`](uigesturerecognizer/cancelstouchesinview.md), [`delaysTouchesBegan`](uigesturerecognizer/delaystouchesbegan.md), [`delaysTouchesEnded`](uigesturerecognizer/delaystouchesended.md) properties:

- [`cancelsTouchesInView`](uigesturerecognizer/cancelstouchesinview.md) — If a gesture recognizer recognizes its gesture, it unbinds the remaining touches of that gesture from their view (so the window won’t deliver them). The window cancels the previously delivered touches with a ([`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md)) message. If a gesture recognizer doesn’t recognize its gesture, the view receives all touches in the multi-touch sequence.
- [`delaysTouchesBegan`](uigesturerecognizer/delaystouchesbegan.md) — As long as a gesture recognizer, when analyzing touch events, hasn’t failed recognition of its gesture, the window withholds delivery of touch objects in the [`UITouch.Phase.began`](uitouch/phase-swift.enum/began.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, the view doesn’t receive these touch objects. If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md) method (and possibly a follow-up [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md) invocation to inform it of the touches current location).
- [`delaysTouchesEnded`](uigesturerecognizer/delaystouchesended.md) — As long as a gesture recognizer, when analyzing touch events, hasn’t failed recognition of its gesture, the window withholds delivery of touch objects in the [`UITouch.Phase.ended`](uitouch/phase-swift.enum/ended.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, the touches are canceled (in a [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) message). If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md) method.

Note that “recognize” in the above descriptions doesn’t necessarily equate to a transition to the Recognized state.

##### Subclassing Notes

You may create a subclass of [`UIGestureRecognizer`](uigesturerecognizer.md) that recognizes a distinctive gesture — for example, a “check mark” gesture. If you’re going to create such a concrete gesture recognizer, be sure to import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift). This file declares all the methods and properties a subclass must either override, call, or reset.

Gesture recognizers operate within a predefined state machine, transitioning to subsequent states as they handle multi-touch events. The states and their possible transitions differ for continuous and discrete gestures. All gesture recognizers begin a multi-touch sequence in the Possible state ([`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md)). Discrete gestures transition from Possible to either Recognized ([`recognized`](uigesturerecognizer/state-swift.enum/recognized.md)) or Failed ([`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md)), depending on whether they successfully interpret the gesture or not. If the gesture recognizer transitions to Recognized, it sends its action message to its target.

For continuous gestures, the state transitions a gesture recognizer might make are more numerous, as indicated in the following sequence:

- Possible —> Began —> [Changed] —> Cancelled
- Possible —> Began —> [Changed] —> Ended

The Changed state is optional and may occur multiple times before the Cancelled or Ended state is reached. The gesture recognizer sends action messages at each state transition. Thus for a continuous gesture such as a pinch, action messages are sent as the two fingers move toward or away from each other. The `enum` constants representing these states are of type [`UIGestureRecognizer.State`](uigesturerecognizer/state-swift.enum.md). (Note that the constants for Recognized and Ended states are synonymous.)

Subclasses must set the [`state`](uigesturerecognizer/state-swift.property.md) property to the appropriate value when they transition between states.

###### Methods to Override

The methods that subclasses must override are described in [`Implementing subclasses`](uigesturerecognizer#Implementing-subclasses.md). Subclasses must also periodically reset the [`state`](uigesturerecognizer/state-swift.property.md) property (as described above) and may call the [`ignore(_:for:)`](uigesturerecognizer/ignore(_:for:)-5f685.md) method.

###### Special Considerations

The [`state`](uigesturerecognizer/state-swift.property.md) property is declared in `UIGestureRecognizer.h` as being read-only. This property declaration is intended for clients of gesture recognizers. Subclasses of `UIGestureRecognizer` must import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift). This file contains a redeclaration of `state` that makes it read-write.

## Topics

### Initializing a gesture recognizer
- [init(target: Any?, action: Selector?)](uigesturerecognizer/init(target:action:).md)
  Creates a gesture recognizer with a target and an action selector.
- [convenience init?(coder: NSCoder)](uigesturerecognizer/init(coder:).md)
  Creates a gesture recognizer from data in an unarchiver.
- [convenience init()](uigesturerecognizer/init.md)
  Creates a gesture recognizer.
### Managing gesture-related interactions
- [var delegate: (any UIGestureRecognizerDelegate)?](uigesturerecognizer/delegate.md)
  The delegate of the gesture recognizer.
- [protocol UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md)
  A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.
### Adding and removing targets and actions
- [func addTarget(Any, action: Selector)](uigesturerecognizer/addtarget(_:action:).md)
  Adds a target and an action to a gesture-recognizer object.
- [func removeTarget(Any?, action: Selector?)](uigesturerecognizer/removetarget(_:action:).md)
  Removes a target and an action from a gesture-recognizer object.
### Getting the touches and location of a gesture
- [func location(in: UIView?) -> CGPoint](uigesturerecognizer/location(in:).md)
  Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.
- [func location(ofTouch: Int, in: UIView?) -> CGPoint](uigesturerecognizer/location(oftouch:in:).md)
  Returns the location of one of the gesture’s touches in the local coordinate system of a given view.
- [var numberOfTouches: Int](uigesturerecognizer/numberoftouches.md)
  The number of touches involved in the gesture represented by the gesture recognizer.
### Getting the recognizer’s state and view
- [var state: UIGestureRecognizer.State](uigesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [UIGestureRecognizer.State](uigesturerecognizer/state-swift.enum.md)
  Constants that represent the current state a gesture recognizer is in.
- [var view: UIView?](uigesturerecognizer/view.md)
  The view the gesture recognizer is attached to.
- [var isEnabled: Bool](uigesturerecognizer/isenabled.md)
  A Boolean property that indicates whether the gesture recognizer is enabled.
- [var buttonMask: UIEvent.ButtonMask](uigesturerecognizer/buttonmask.md)
  A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [var modifierFlags: UIKeyModifierFlags](uigesturerecognizer/modifierflags.md)
  The bit mask of modifier flags in the gesture represented by the gesture recognizer.
### Canceling and delaying touches
- [var cancelsTouchesInView: Bool](uigesturerecognizer/cancelstouchesinview.md)
  A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [var delaysTouchesBegan: Bool](uigesturerecognizer/delaystouchesbegan.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.
- [var delaysTouchesEnded: Bool](uigesturerecognizer/delaystouchesended.md)
  A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.
### Specifying dependencies between gesture recognizers
- [func require(toFail: UIGestureRecognizer)](uigesturerecognizer/require(tofail:).md)
  Creates a dependency relationship between the gesture recognizer and another gesture recognizer when the objects are created.
### Recognizing different gestures
- [var allowedPressTypes: [NSNumber]](uigesturerecognizer/allowedpresstypes.md)
  An array of press types used to distinguish the type of button press.
- [var allowedTouchTypes: [NSNumber]](uigesturerecognizer/allowedtouchtypes.md)
  An array of touch types used to distinguish type of touches.
- [var requiresExclusiveTouchType: Bool](uigesturerecognizer/requiresexclusivetouchtype.md)
  A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.
### Debugging gesture recognizers
- [var name: String?](uigesturerecognizer/name.md)
  The unique name of the gesture recognizer.
### Implementing subclasses
- [func touchesBegan(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchesbegan(_:with:).md)
  Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchesmoved(_:with:).md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchesended(_:with:).md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesCancelled(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchescancelled(_:with:).md)
  Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](uigesturerecognizer/touchesestimatedpropertiesupdated(_:).md)
  Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [func reset()](uigesturerecognizer/reset.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func ignore(UITouch, for: UIEvent)](uigesturerecognizer/ignore(_:for:)-5f685.md)
  Tells the gesture recognizer to ignore a specific touch of the given event.
- [func canBePrevented(by: UIGestureRecognizer) -> Bool](uigesturerecognizer/canbeprevented(by:).md)
  Overridden to indicate that the specified gesture recognizer can prevent the receiver from recognizing a gesture.
- [func canPrevent(UIGestureRecognizer) -> Bool](uigesturerecognizer/canprevent(_:).md)
  Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.
- [func shouldReceive(UIEvent) -> Bool](uigesturerecognizer/shouldreceive(_:).md)
- [func shouldRequireFailure(of: UIGestureRecognizer) -> Bool](uigesturerecognizer/shouldrequirefailure(of:).md)
  Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [func shouldBeRequiredToFail(by: UIGestureRecognizer) -> Bool](uigesturerecognizer/shouldberequiredtofail(by:).md)
  Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [func ignore(UIPress, for: UIPressesEvent)](uigesturerecognizer/ignore(_:for:)-8qqor.md)
  Tells the gesture recognizer to ignore a specific press of the given event.
- [func pressesBegan(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/pressesbegan(_:with:).md)
  Sent to the receiver when a physical button is pressed in the associated view.
- [func pressesChanged(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/presseschanged(_:with:).md)
  Sent to the receiver when the [`force`](uipress/force.md) of the press has changed in the associated view.
- [func pressesEnded(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/pressesended(_:with:).md)
  Sent to the receiver when a button is released from the associated view.
- [func pressesCancelled(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/pressescancelled(_:with:).md)
  Sent to the receiver when a system event (such as a low-memory warning) cancels a press event.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md)
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md)
- [UIPanGestureRecognizer](uipangesturerecognizer.md)
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md)
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md)
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
- [UITapGestureRecognizer](uitapgesturerecognizer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing a custom gesture recognizer](implementing-a-custom-gesture-recognizer.md)
  Discover when and how to build your own gesture recognizers.
- [protocol UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md)
  A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer)*