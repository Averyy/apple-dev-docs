# UICollectionViewPlaceholder

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A placeholder for an item dragged or dropped on a collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewPlaceholder
```

```objc
@interface UICollectionViewPlaceholder : NSObject
```

## Topics

### Initializing a Placeholder
- [init(insertionIndexPath: IndexPath, reuseIdentifier: String)](./uicollectionviewplaceholder/init%28insertionindexpath,reuseidentifier%29.md)
  Creates a placeholder object with the specified index path and reuse identifier.
### Updating the Cell’s Content
- [var cellUpdateHandler: ((UICollectionViewCell) -> Void)?](./uicollectionviewplaceholder/cellupdatehandler.md)
  The block that updates the contents of the placeholder cell.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UICollectionViewDropPlaceholder](./uicollectionviewdropplaceholder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

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
- [class UICollectionViewDropProposal](./uicollectionviewdropproposal.md)
  Your proposed solution for handling a drop in a collection view.
- [protocol UICollectionViewDropItem](./uicollectionviewdropitem.md)
  The data associated with an item being dropped into the collection view.
- [protocol UICollectionViewDropPlaceholderContext](./uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [protocol UIDataSourceTranslating](./uidatasourcetranslating.md)
  An advanced interface for managing a data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewplaceholder)*