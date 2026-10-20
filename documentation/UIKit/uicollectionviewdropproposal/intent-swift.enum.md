# UICollectionViewDropProposal.Intent

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating how you intend to handle a drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Intent
```

```c
enum UICollectionViewDropIntent : NSInteger;
```

## Topics

### Enumeration Cases
- [UICollectionViewDropProposal.Intent.insertAtDestinationIndexPath](./intent-swift.enum/insertatdestinationindexpath.md)
  Insert the dropped items at the specified index path.
- [UICollectionViewDropProposal.Intent.insertIntoDestinationIndexPath](./intent-swift.enum/insertintodestinationindexpath.md)
  Incorporate the dropped items into the item at the specified index path.
- [UICollectionViewDropProposal.Intent.unspecified](./intent-swift.enum/unspecified.md)
  No drop proposal was specified.
### Initializers
- [init?(rawValue: Int)](./intent-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Proposed Drop Location
- [var intent: UICollectionViewDropProposal.Intent](./intent-swift.property.md)
  The option to use when incorporating the dropped items into your content.
- [enum UIDropOperation](../uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum)*