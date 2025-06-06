# setActive(_:animated:)

**Framework**: ARKit  
**Kind**: method

Controls whether coaching is in progress.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setActive(_ active: Bool, animated: Bool)
```

#### Discussion

If the `animated` property of [`setActive(_:animated:)`](arcoachingoverlayview/setactive(_:animated:).md) is [`true`](https://developer.apple.com/documentation/swift/true), [`isActive`](arcoachingoverlayview/isactive.md) and [`isHidden`](https://developer.apple.com/documentation/UIKit/UIView/isHidden) are [`false`](https://developer.apple.com/documentation/swift/false) while the coaching overlay is fading out. When the coaching overlay is deactivated without animation, or when the animation finishes, ARKit notifies you by calling [`coachingOverlayViewDidDeactivate(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:).md).

## Parameters

- `active`: A flag you set to indicate whether the coaching overlay should activate or deactivate.
- `animated`: A flag that when  , fades the coaching overlay in or out. When you pass a value of  , the coaching overlay shows or hides instantly.

## See Also

- [var activatesAutomatically: Bool](arcoachingoverlayview/activatesautomatically.md)
  A flag that indicates whether the coaching view activates automatically, depending on the current session state.
- [var isActive: Bool](arcoachingoverlayview/isactive.md)
  A flag that indicates whether coaching is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/setactive(_:animated:))*