# isActive

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A flag that indicates whether coaching is in progress.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isActive;
```

#### Discussion

If [`activatesAutomatically`](./activatesautomatically.md) is enabled, this flag tells you whether coaching is in progress. Assign a [`delegate`](./delegate.md) to coordinate your actions with the coaching overlay and allow [`coachingOverlayViewWillActivate(_:)`](../arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate%28_%29.md) to notify you when the coaching overlay is active.

When the coaching overlay is deactivating, [`isActive`](./isactive.md) is [`false`](../../Swift/false.md). If the `animated` property of [`setActive(_:animated:)`](./setactive%28_,animated%29.md) is [`true`](../../Swift/true.md), [`isActive`](./isactive.md) and [`isHidden`](../../UIKit/uiview/ishidden.md) are [`false`](../../Swift/false.md) while the coaching overlay is fading out. When the coaching overlay is deactivated without animation, or when the animation finishes, ARKit notifies you by calling [`coachingOverlayViewDidDeactivate(_:)`](../arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate%28_%29.md).

## See Also

### Activating the View
- [var activatesAutomatically: Bool](./activatesautomatically.md)
  A flag that indicates whether the coaching view activates automatically, depending on the current session state.
- [func setActive(Bool, animated: Bool)](./setactive%28_,animated%29.md)
  Controls whether coaching is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/isactive)*