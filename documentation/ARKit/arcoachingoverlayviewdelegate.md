# ARCoachingOverlayViewDelegate

**Framework**: ARKit  
**Kind**: protocol

A set of callbacks you implement to be notified of coaching events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARCoachingOverlayViewDelegate : NSObjectProtocol
```

#### Overview

Implement a delegate to coordinate your app’s actions with coaching overlay. For example, when the coaching overlay determines the user needs guidance, you hide your app’s UI to allow the user to focus on the coaching experience. When the coaching overlay determines the [`goal`](arcoachingoverlayview/goal-swift.property.md) is met, you show your app’s UI and begin your app’s AR experience.

## Topics

### Enabling Coaching
- [func coachingOverlayViewWillActivate(ARCoachingOverlayView)](arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate(_:).md)
  Tells you when the coaching overlay view activates.
- [func coachingOverlayViewDidDeactivate(ARCoachingOverlayView)](arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:).md)
  Tells you when the coaching experience is completely deactivated.
### Restarting the Session
- [func coachingOverlayViewDidRequestSessionReset(ARCoachingOverlayView)](arcoachingoverlayviewdelegate/coachingoverlayviewdidrequestsessionreset(_:).md)
  Tells you when the user taps the coaching overlay view’s Start Over button while the session is relocalizing.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any ARCoachingOverlayViewDelegate)?](arcoachingoverlayview/delegate.md)
  An object you supply that implements coaching event callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayviewdelegate)*