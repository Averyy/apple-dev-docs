# coachingOverlayViewDidDeactivate(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells you when the coaching experience is completely deactivated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
optional func coachingOverlayViewDidDeactivate(_ coachingOverlayView: ARCoachingOverlayView)
```

```objc
- (void) coachingOverlayViewDidDeactivate:(ARCoachingOverlayView *) coachingOverlayView;
```

## Discussion

Implement this function to do any custom actions your app requires to begin the AR experience. For example, when coaching is deactivated, your app might restore custom UI.

When the coaching overlay is deactivating, [`isActive`](../arcoachingoverlayview/isactive.md) is [`false`](../../Swift/false.md). If the `animated` property of [`setActive(_:animated:)`](../arcoachingoverlayview/setactive%28_,animated%29.md) is [`true`](../../Swift/true.md), [`isActive`](../arcoachingoverlayview/isactive.md) and [`isHidden`](../../UIKit/uiview/ishidden.md) are [`false`](../../Swift/false.md) while the coaching overlay is fading out. When the coaching overlay is deactivated without animation, or when the animation finishes, ARKit sends a  [`coachingOverlayViewDidDeactivate(_:)`](./coachingoverlayviewdiddeactivate%28_%29.md) notification.

## See Also

### Enabling Coaching
- [func coachingOverlayViewWillActivate(ARCoachingOverlayView)](./coachingoverlayviewwillactivate%28_%29.md)
  Tells you when the coaching overlay view activates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:))*