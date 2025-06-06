# NSAlignmentFeedbackFilter

**Framework**: AppKit  
**Kind**: class

An object that can filter the movement of an object and provides haptic feedback when alignment occurs.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSAlignmentFeedbackFilter
```

#### Overview

With a Force Touch trackpad, apps can produce tactile feedback to complement user actions. If your app implements alignment features, you can use the [`NSAlignmentFeedbackFilter`](nsalignmentfeedbackfilter.md) class to filter object movements and provide haptic feedback to the user at appropriate times. As the user drags objects into alignment with a guide or another object, the user actually feels a physical bump as the object snaps into place.

##### Implementing Alignment Feedback

To implement alignment feedback in your custom alignment controller class, set up the class to receive events for tracking the movement of an object. These can be events matching the [`inputEventMask`](nsalignmentfeedbackfilter/inputeventmask.md) value of an `NSAlignmentFeedbackFilter` object, or events from a gesture recognizer ([`NSGestureRecognizer`](nsgesturerecognizer.md)). For each event received:

1. Create an instance of an `NSAlignmentFeedbackFilter` object. For example:

1. Inform the alignment feedback filter object about the event. To do this, call one of the following methods:

- [`update(with:)`](nsalignmentfeedbackfilter/update(with:).md)
- [`update(withPanRecognizer:)`](nsalignmentfeedbackfilter/update(withpanrecognizer:).md)

1. Store the location of the object before it moves in response to the event. This is considered the  location of the object.
2. Move the object to its new location in response to the event. This is the location where the object will reside if no alignment occurs.
3. Store the new location of the object. This is considered the  location of the object.
4. Determine where the object will move to be aligned. This is considered the  location of the object.
5. Request a feedback token based on the previous location, default location, and aligned location. To do this, call one of the following methods:

- [`alignmentFeedbackTokenForMovement(in:previousPoint:alignedPoint:defaultPoint:)`](nsalignmentfeedbackfilter/alignmentfeedbacktokenformovement(in:previouspoint:alignedpoint:defaultpoint:).md) - If the object will be moved both horizontally and vertically to become aligned.
- [`alignmentFeedbackTokenForHorizontalMovement(in:previousX:alignedX:defaultX:)`](nsalignmentfeedbackfilter/alignmentfeedbacktokenforhorizontalmovement(in:previousx:alignedx:defaultx:).md) - If the object will be moved horizontally only to become aligned.
- [`alignmentFeedbackTokenForVerticalMovement(in:previousY:alignedY:defaultY:)`](nsalignmentfeedbackfilter/alignmentfeedbacktokenforverticalmovement(in:previousy:alignedy:defaulty:).md) - If the object will be moved vertically only to become aligned.

1. If a feedback token is successfully prepared, call [`performFeedback(_:performanceTime:)`](nsalignmentfeedbackfilter/performfeedback(_:performancetime:).md) to perform the haptic feedback. Then, move the object to the aligned location.

If a value of `null` is returned, rather than a feedback token, then the system has determined that alignment and feedback are not appropriate. Perhaps the cursor is moving too fast or the distance to the aligned location is not significant enough to produce a visual snap. Move the object to its default location.

## Topics

### Determining Event Types for the Filter
- [class var inputEventMask: NSEvent.EventTypeMask](nsalignmentfeedbackfilter/inputeventmask.md)
  Retrieves the event types the filter accepts.
### Informing the Filter About Events
- [func update(with: NSEvent)](nsalignmentfeedbackfilter/update(with:).md)
  Informs the feedback filter about a new event.
- [func update(withPanRecognizer: NSPanGestureRecognizer)](nsalignmentfeedbackfilter/update(withpanrecognizer:).md)
  Informs the feedback filter about a new pan (drag) gesture recognizer event.
### Preparing Haptic Feedback for Alignment
- [func alignmentFeedbackTokenForMovement(in: NSView?, previousPoint: NSPoint, alignedPoint: NSPoint, defaultPoint: NSPoint) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenformovement(in:previouspoint:alignedpoint:defaultpoint:).md)
  Requests a feedback token for the alignment of an object requiring horizontal and vertical movement.
- [func alignmentFeedbackTokenForHorizontalMovement(in: NSView?, previousX: CGFloat, alignedX: CGFloat, defaultX: CGFloat) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenforhorizontalmovement(in:previousx:alignedx:defaultx:).md)
  Requests a feedback token for the alignment of an object requiring horizontal movement only.
- [func alignmentFeedbackTokenForVerticalMovement(in: NSView?, previousY: CGFloat, alignedY: CGFloat, defaultY: CGFloat) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenforverticalmovement(in:previousy:alignedy:defaulty:).md)
  Requests a feedback token for the alignment of an object requiring vertical movement only.
### Providing Feedback to the User
- [func performFeedback([any NSAlignmentFeedbackToken], performanceTime: NSHapticFeedbackManager.PerformanceTime)](nsalignmentfeedbackfilter/performfeedback(_:performancetime:).md)
  Performs the haptic feedback described by one or more alignment feedback tokens.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSHapticFeedbackManager](nshapticfeedbackmanager.md)
  An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.
- [protocol NSHapticFeedbackPerformer](nshapticfeedbackperformer.md)
  A set of methods and constants that a haptic feedback performer implements.
- [protocol NSAlignmentFeedbackToken](nsalignmentfeedbacktoken.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter)*