# UICollectionViewDropProposal.Intent

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Enumeration Cases
- [UICollectionViewDropProposal.Intent.insertAtDestinationIndexPath](uicollectionviewdropproposal/intent-swift.enum/insertatdestinationindexpath.md)
  Insert the dropped items at the specified index path.
- [UICollectionViewDropProposal.Intent.insertIntoDestinationIndexPath](uicollectionviewdropproposal/intent-swift.enum/insertintodestinationindexpath.md)
  Incorporate the dropped items into the item at the specified index path.
- [UICollectionViewDropProposal.Intent.unspecified](uicollectionviewdropproposal/intent-swift.enum/unspecified.md)
  No drop proposal was specified.
### Initializers
- [init?(rawValue: Int)](uicollectionviewdropproposal/intent-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var intent: UICollectionViewDropProposal.Intent](uicollectionviewdropproposal/intent-swift.property.md)
  The option to use when incorporating the dropped items into your content.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal/intent-swift.enum)*