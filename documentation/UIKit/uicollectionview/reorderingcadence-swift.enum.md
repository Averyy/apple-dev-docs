# UICollectionView.ReorderingCadence

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the speed at which collection view items are reorganized during a drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum ReorderingCadence
```

```c
enum UICollectionViewReorderingCadence : NSInteger;
```

## Topics

### Constants
- [UICollectionView.ReorderingCadence.immediate](./reorderingcadence-swift.enum/immediate.md)
  Items are reordered into place immediately.
- [UICollectionView.ReorderingCadence.fast](./reorderingcadence-swift.enum/fast.md)
  Items are reordered quickly, but with a short delay.
- [UICollectionView.ReorderingCadence.slow](./reorderingcadence-swift.enum/slow.md)
  Items are reordered after a delay.
### Initializers
- [init?(rawValue: Int)](./reorderingcadence-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing drop interactions
- [var dropDelegate: (any UICollectionViewDropDelegate)?](./dropdelegate.md)
  The delegate object that manages the dropping of items into the collection view.
- [protocol UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [var hasActiveDrop: Bool](./hasactivedrop.md)
  A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [var reorderingCadence: UICollectionView.ReorderingCadence](./reorderingcadence-swift.property.md)
  The speed at which items in the collection view are reordered to show potential drop locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reorderingcadence-swift.enum)*