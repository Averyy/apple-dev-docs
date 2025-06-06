# coachingOverlayViewWillActivate(_:)

**Framework**: ARKit  
**Kind**: method

Tells you when the coaching overlay view activates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func coachingOverlayViewWillActivate(_ coachingOverlayView: ARCoachingOverlayView)
```

#### Discussion

Override this function to hide your app’s UI while the coaching overlay is active.

## See Also

- [func coachingOverlayViewDidDeactivate(ARCoachingOverlayView)](arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:).md)
  Tells you when the coaching experience is completely deactivated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate(_:))*