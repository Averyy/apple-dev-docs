# coachingOverlayViewDidDeactivate(_:)

**Framework**: ARKit  
**Kind**: method

Tells you when the coaching experience is completely deactivated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func coachingOverlayViewDidDeactivate(_ coachingOverlayView: ARCoachingOverlayView)
```

#### Discussion

Implement this function to do any custom actions your app requires to begin the AR experience. For example, when coaching is deactivated, your app might restore custom UI.

When the coaching overlay is deactivating, [`isActive`](arcoachingoverlayview/isactive.md) is [`false`](https://developer.apple.com/documentation/swift/false). If the `animated` property of [`setActive(_:animated:)`](arcoachingoverlayview/setactive(_:animated:).md) is [`true`](https://developer.apple.com/documentation/swift/true), [`isActive`](arcoachingoverlayview/isactive.md) and [`isHidden`](https://developer.apple.com/documentation/UIKit/UIView/isHidden) are [`false`](https://developer.apple.com/documentation/swift/false) while the coaching overlay is fading out. When the coaching overlay is deactivated without animation, or when the animation finishes, ARKit sends a  [`coachingOverlayViewDidDeactivate(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:).md) notification.

## See Also

- [func coachingOverlayViewWillActivate(ARCoachingOverlayView)](arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate(_:).md)
  Tells you when the coaching overlay view activates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:))*