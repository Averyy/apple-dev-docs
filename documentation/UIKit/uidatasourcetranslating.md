# UIDataSourceTranslating

**Framework**: UIKit  
**Kind**: protocol

An advanced interface for managing a data source object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIDataSourceTranslating : NSObjectProtocol
```

#### Overview

Use the methods of this protocol to map between the positions of items and sections in your data source object and the positions of those same items and sections in your presented layout. Objects that adopt this protocol do so because the position of items in their data source object don’t always match the corresponding positions in their presented layout.

[`UITableView`](uitableview.md) and [`UICollectionView`](uicollectionview.md) adopt this protocol and use it in conjunction with drag and drop operations. For example, [`UITableView`](uitableview.md) must account for the presence of placeholder cells, which appear as rows in the table but don’t have a corresponding entry in the data source object. Typically, you don’t adopt this protocol in your own classes.

## Topics

### Managing item positions
- [func presentationIndexPath(forDataSourceIndexPath: IndexPath?) -> IndexPath?](uidatasourcetranslating/presentationindexpath(fordatasourceindexpath:).md)
  Translates an index in your data source object to the equivalent index in your presented layout.
- [func dataSourceIndexPath(forPresentationIndexPath: IndexPath?) -> IndexPath?](uidatasourcetranslating/datasourceindexpath(forpresentationindexpath:).md)
  Translates an index in your presented layout to the equivalent index in your data source object.
### Managing section positions
- [func presentationSectionIndex(forDataSourceSectionIndex: Int) -> Int](uidatasourcetranslating/presentationsectionindex(fordatasourcesectionindex:).md)
  Translates a section index in your data source object to the equivalent section index in your presented layout.
- [func dataSourceSectionIndex(forPresentationSectionIndex: Int) -> Int](uidatasourcetranslating/datasourcesectionindex(forpresentationsectionindex:).md)
  Translates a section index in your presented layout to the equivalent section index in your data source object.
### Performing actions
- [func performUsingPresentationValues(() -> Void)](uidatasourcetranslating/performusingpresentationvalues(_:).md)
  Performs actions on the current object using index paths that are relative to the presentation layer of that object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UICollectionView](uicollectionview.md)
- [UITableView](uitableview.md)

## See Also

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)
  Initiate drags and handle drops from a collection view.
- [protocol UICollectionViewDragDelegate](uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [protocol UICollectionViewDropDelegate](uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [protocol UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the collection view.
- [class UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md)
  A placeholder for an item dropped on a collection view.
- [class UICollectionViewDropProposal](uicollectionviewdropproposal.md)
  Your proposed solution for handling a drop in a collection view.
- [protocol UICollectionViewDropItem](uicollectionviewdropitem.md)
  The data associated with an item being dropped into the collection view.
- [protocol UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [class UICollectionViewPlaceholder](uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating)*