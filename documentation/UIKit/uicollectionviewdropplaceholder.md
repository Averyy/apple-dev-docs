# UICollectionViewDropPlaceholder

**Framework**: UIKit  
**Kind**: class

A placeholder for an item dropped on a collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewDropPlaceholder
```

#### Overview

When you want to insert a placeholder cell into your collection view, create a `UICollectionViewDropPlaceholder` object and pass it to the [`drop(_:to:)`](uicollectionviewdropcoordinator/drop(_:to:)-l5tg.md) method of your [`UICollectionViewDropCoordinator`](uicollectionviewdropcoordinator.md). You use a placeholder cell to display a temporary interface while you load the cell’s contents asynchronously. For example, your placeholder cell might display a progress indicator or a message that the cell content isn’t yet available. The placeholder object contains the reuse identifier of the temporary cell you want to display in your collection view. It can also include a custom preview to use during the drop.

You must register the cells you use with your placeholders in advance. In your storyboard file, add a collection view cell object to your collection view, configure its appearance, set its class to [`UICollectionViewCell`](uicollectionviewcell.md) (or an appropriate subclass), and assign a reuse identifier to it. When you create your `UICollectionViewDropPlaceholder` object, pass the cell’s reuse identifier to [`init(insertionIndexPath:reuseIdentifier:)`](uicollectionviewplaceholder/init(insertionindexpath:reuseidentifier:).md). The collection view uses the information in your placeholder object to insert the cell into the collection view.

Set the [`cellUpdateHandler`](uicollectionviewplaceholder/cellupdatehandler.md) to a block of code that configures the cell as a placeholder for the incoming data.

For more information, see [`Supporting Drag and Drop in Collection Views`](supporting-drag-and-drop-in-collection-views.md).

> ❗ **Important**:  Placeholder cells are meant to be a temporary part of your collection view. Always replace them with actual cells as soon as possible, or cancel the drop to remove them from the collection view. Use the methods of a [`UICollectionViewDropPlaceholderContext`](uicollectionviewdropplaceholdercontext.md) object to remove placeholders from your collection view.

 Placeholder cells are meant to be a temporary part of your collection view. Always replace them with actual cells as soon as possible, or cancel the drop to remove them from the collection view. Use the methods of a [`UICollectionViewDropPlaceholderContext`](uicollectionviewdropplaceholdercontext.md) object to remove placeholders from your collection view.

## Topics

### Providing a Custom Preview
- [var previewParametersProvider: ((UICollectionViewCell) -> UIDragPreviewParameters?)?](uicollectionviewdropplaceholder/previewparametersprovider.md)
  The object that provides the preview parameters for a drag item.

## Relationships

### Inherits From
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)
  Initiate drags and handle drops from a collection view.
- [protocol UICollectionViewDragDelegate](uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [protocol UICollectionViewDropDelegate](uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [protocol UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the collection view.
- [class UICollectionViewDropProposal](uicollectionviewdropproposal.md)
  Your proposed solution for handling a drop in a collection view.
- [protocol UICollectionViewDropItem](uicollectionviewdropitem.md)
  The data associated with an item being dropped into the collection view.
- [protocol UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UICollectionViewPlaceholder](uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholder)*