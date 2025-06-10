# UICollectionView.SelfSizingInvalidation.disabled

**Framework**: UIKit  
**Kind**: case

A mode that disables self-sizing invalidation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case disabled
```

#### Discussion

If you use this self-sizing invalidation mode, no sizing updates occur after calling [`invalidateIntrinsicContentSize()`](uiview/invalidateintrinsiccontentsize().md) on a self-sizing cell or its [`contentView`](uicollectionviewcell/contentview.md).

## See Also

- [UICollectionView.SelfSizingInvalidation.enabled](uicollectionview/selfsizinginvalidation-swift.enum/enabled.md)
  A mode that enables manual self-sizing invalidation.
- [UICollectionView.SelfSizingInvalidation.enabledIncludingConstraints](uicollectionview/selfsizinginvalidation-swift.enum/enabledincludingconstraints.md)
  A mode that enables automatic self-sizing invalidation after Auto Layout changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/disabled)*