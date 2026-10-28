# UICollectionView.SelfSizingInvalidation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UICollectionViewSelfSizingInvalidation : NSInteger;
```

## Discussion

Use these constants with the [`selfSizingInvalidation`](./selfsizinginvalidation-swift.property.md) property.

## Topics

### Constants
- [UICollectionView.SelfSizingInvalidation.disabled](./selfsizinginvalidation-swift.enum/disabled.md)
  A mode that disables self-sizing invalidation.
- [UICollectionView.SelfSizingInvalidation.enabled](./selfsizinginvalidation-swift.enum/enabled.md)
  A mode that enables manual self-sizing invalidation.
- [UICollectionView.SelfSizingInvalidation.enabledIncludingConstraints](./selfsizinginvalidation-swift.enum/enabledincludingconstraints.md)
  A mode that enables automatic self-sizing invalidation after Auto Layout changes.
### Initializers
- [init?(rawValue: Int)](./selfsizinginvalidation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Resizing self-sizing cells
- [var selfSizingInvalidation: UICollectionView.SelfSizingInvalidation](./selfsizinginvalidation-swift.property.md)
  The mode that the collection view uses for invalidating the size of self-sizing cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/selfsizinginvalidation-swift.enum)*