# UICollectionView.SelfSizingInvalidation.enabledIncludingConstraints

**Framework**: UIKit  
**Kind**: case

A mode that enables automatic self-sizing invalidation after Auto Layout changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case enabledIncludingConstraints
```

#### Discussion

If you use this self-sizing invalidation mode, calling [`invalidateIntrinsicContentSize()`](uiview/invalidateintrinsiccontentsize().md) on a self-sizing cell or its [`contentView`](uicollectionviewcell/contentview.md) causes the cell to resize if necessary. Additionally, any Auto Layout change within the [`contentView`](uicollectionviewcell/contentview.md) of a self-sizing cell automatically calls [`invalidateIntrinsicContentSize()`](uiview/invalidateintrinsiccontentsize().md).

## See Also

- [UICollectionView.SelfSizingInvalidation.disabled](uicollectionview/selfsizinginvalidation-swift.enum/disabled.md)
  A mode that disables self-sizing invalidation.
- [UICollectionView.SelfSizingInvalidation.enabled](uicollectionview/selfsizinginvalidation-swift.enum/enabled.md)
  A mode that enables manual self-sizing invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum/enabledincludingconstraints)*