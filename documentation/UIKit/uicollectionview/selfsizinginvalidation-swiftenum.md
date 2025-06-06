# UICollectionView.SelfSizingInvalidation

**Framework**: UIKit  
**Kind**: enum

Constants that describe modes for invalidating the size of self-sizing collection view cells.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum SelfSizingInvalidation
```

#### Discussion

Use these constants with the [`selfSizingInvalidation`](uicollectionview/selfsizinginvalidation-swift.property.md) property.

## Topics

### Constants
- [UICollectionView.SelfSizingInvalidation.disabled](uicollectionview/selfsizinginvalidation-swift.enum/disabled.md)
  A mode that disables self-sizing invalidation.
- [UICollectionView.SelfSizingInvalidation.enabled](uicollectionview/selfsizinginvalidation-swift.enum/enabled.md)
  A mode that enables manual self-sizing invalidation.
- [UICollectionView.SelfSizingInvalidation.enabledIncludingConstraints](uicollectionview/selfsizinginvalidation-swift.enum/enabledincludingconstraints.md)
  A mode that enables automatic self-sizing invalidation after Auto Layout changes.
### Initializers
- [init?(rawValue: Int)](uicollectionview/selfsizinginvalidation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var selfSizingInvalidation: UICollectionView.SelfSizingInvalidation](uicollectionview/selfsizinginvalidation-swift.property.md)
  The mode that the collection view uses for invalidating the size of self-sizing cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum)*