# isActive

**Framework**: ARKit  
**Kind**: property

A flag that indicates whether coaching is in progress.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isActive: Bool { get }
```

#### Discussion

If [`activatesAutomatically`](arcoachingoverlayview/activatesautomatically.md) is enabled, this flag tells you whether coaching is in progress. Assign a [`delegate`](arcoachingoverlayview/delegate.md) to coordinate your actions with the coaching overlay and allow [`coachingOverlayViewWillActivate(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewwillactivate(_:).md) to notify you when the coaching overlay is active.

When the coaching overlay is deactivating, [`isActive`](arcoachingoverlayview/isactive.md) is [`false`](https://developer.apple.com/documentation/Swift/false). If the `animated` property of [`setActive(_:animated:)`](arcoachingoverlayview/setactive(_:animated:).md) is [`true`](https://developer.apple.com/documentation/Swift/true), [`isActive`](arcoachingoverlayview/isactive.md) and [`isHidden`](https://developer.apple.com/documentation/UIKit/UIView/isHidden) are [`false`](https://developer.apple.com/documentation/Swift/false) while the coaching overlay is fading out. When the coaching overlay is deactivated without animation, or when the animation finishes, ARKit notifies you by calling [`coachingOverlayViewDidDeactivate(_:)`](arcoachingoverlayviewdelegate/coachingoverlayviewdiddeactivate(_:).md).

## See Also

- [var activatesAutomatically: Bool](arcoachingoverlayview/activatesautomatically.md)
  A flag that indicates whether the coaching view activates automatically, depending on the current session state.
- [func setActive(Bool, animated: Bool)](arcoachingoverlayview/setactive(_:animated:).md)
  Controls whether coaching is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/isactive)*