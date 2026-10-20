# UICollectionViewDropProposal

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Your proposed solution for handling a drop in a collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewDropProposal
```

```objc
@interface UICollectionViewDropProposal : UIDropProposal
```

## Mentions

- [Supporting Drag and Drop in Collection Views](./supporting-drag-and-drop-in-collection-views.md)

#### Overview

Create instances of this class in the [`collectionView(_:dropSessionDidUpdate:withDestinationIndexPath:)`](./uicollectionviewdropdelegate/collectionview%28_,dropsessiondidupdate,withdestinationindexpath%29.md) method of your drop delegate object. You create drop proposals to let the collection view know how you intend to handle a drop at the currently specified location. The collection view uses that information to provide appropriate visual feedback to the user.

## Topics

### Creating a Drop Proposal
- [init(operation: UIDropOperation, intent: UICollectionViewDropProposal.Intent)](./uicollectionviewdropproposal/init%28operation,intent%29.md)
  Creates a drop proposal object that specifies how to incorporate the dropped content.
### Getting the Proposed Drop Location
- [var intent: UICollectionViewDropProposal.Intent](./uicollectionviewdropproposal/intent-swift.property.md)
  The option to use when incorporating the dropped items into your content.
- [UICollectionViewDropProposal.Intent](./uicollectionviewdropproposal/intent-swift.enum.md)
  Constants indicating how you intend to handle a drop.
- [enum UIDropOperation](./uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
### Initializers
- [init(dropOperation: UIDropOperation, intent: UICollectionViewDropProposal.Intent)](./uicollectionviewdropproposal/init%28dropoperation,intent%29.md)

## Relationships

### Inherits From
- [UIDropProposal](./uidropproposal.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Drag and drop
- [Supporting Drag and Drop in Collection Views](./supporting-drag-and-drop-in-collection-views.md)
  Initiate drags and handle drops from a collection view.
- [protocol UICollectionViewDragDelegate](./uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [protocol UICollectionViewDropDelegate](./uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [protocol UICollectionViewDropCoordinator](./uicollectionviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the collection view.
- [class UICollectionViewDropPlaceholder](./uicollectionviewdropplaceholder.md)
  A placeholder for an item dropped on a collection view.
- [protocol UICollectionViewDropItem](./uicollectionviewdropitem.md)
  The data associated with an item being dropped into the collection view.
- [protocol UICollectionViewDropPlaceholderContext](./uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [protocol UIDataSourceTranslating](./uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UICollectionViewPlaceholder](./uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal)*