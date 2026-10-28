# coachingOverlayViewWillActivate(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells you when the coaching overlay view activates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
optional func coachingOverlayViewWillActivate(_ coachingOverlayView: ARCoachingOverlayView)
```

```objc
- (void) coachingOverlayViewWillActivate:(ARCoachingOverlayView *) coachingOverlayView;
```

## Discussion

Override this function to hide your app’s UI while the coaching overlay is active.

## See Also

### Enabling Coaching
- [func coachingOverlayViewDidDeactivate(ARCoachingOverlayView)](./coachingoverlayviewdiddeactivate%28_%29.md)
  Tells you when the coaching experience is completely deactivated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate(_:))*