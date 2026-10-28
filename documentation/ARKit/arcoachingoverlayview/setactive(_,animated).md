# setActive(_:animated:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Controls whether coaching is in progress.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
func setActive(_ active: Bool, animated: Bool)
```

```objc
- (void) setActive:(BOOL) active animated:(BOOL) animated;
```

## Discussion

If the `animated` property of [`setActive(_:animated:)`](./setactive%28_,animated%29.md) is [`true`](../../Swift/true.md), [`isActive`](./isactive.md) and [`isHidden`](../../UIKit/uiview/ishidden.md) are [`false`](../../Swift/false.md) while the coaching overlay is fading out. When the coaching overlay is deactivated without animation, or when the animation finishes, ARKit notifies you by calling [`coachingOverlayViewDidDeactivate(_:)`](../arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate%28_%29.md).

## Parameters

- `active`: A flag you set to indicate whether the coaching overlay should activate or deactivate.
- `animated`: A flag that when [`true`](../../Swift/true.md), fades the coaching overlay in or out. When you pass a value of [`false`](../../Swift/false.md), the coaching overlay shows or hides instantly.

## See Also

### Activating the View
- [var activatesAutomatically: Bool](./activatesautomatically.md)
  A flag that indicates whether the coaching view activates automatically, depending on the current session state.
- [var isActive: Bool](./isactive.md)
  A flag that indicates whether coaching is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/setactive(_:animated:))*