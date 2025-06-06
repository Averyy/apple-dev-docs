# NSOutlineView

**Framework**: AppKit  
**Kind**: class

A view that uses a row-and-column format to display hierarchical data like directories and files that can be expanded and collapsed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSOutlineView
```

#### Overview

Like a table view, an outline view does not store its own data, instead it retrieves data values as needed from a data source to which it has a weak reference (see [`Delegates and Data Sources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/DelegatesandDataSources/DelegatesandDataSources.html#//apple_ref/doc/uid/TP40010810-CH11)). See [`NSOutlineViewDataSource`](nsoutlineviewdatasource.md), which declares the methods that an `NSOutlineView` object uses to access the contents of its data source object.

An outline view has the following features:

- A user can expand and collapse rows, edit values, and resize and rearrange columns.
- Each item in the outline view must be unique. In order for the collapsed state to remain consistent between reloads the item’s pointer must remain the same and the item must maintain [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) sameness.
- The view gets data from a data source (see [`NSOutlineViewDataSource`](nsoutlineviewdatasource.md)).
- The view retrieves only the data that needs to be displayed.

> ❗ **Important**:  It is possible that your data source methods for populating the outline view may be called before [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) if the data source is specified in Interface Builder. You should defend against this by having the data source’s [`outlineView(_:numberOfChildrenOfItem:)`](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md) method return `0` for the number of items when the data source has not yet been configured. In [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()), when the data source is initialized you should always call [`reloadData()`](nstableview/reloaddata().md).

 It is possible that your data source methods for populating the outline view may be called before [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) if the data source is specified in Interface Builder. You should defend against this by having the data source’s [`outlineView(_:numberOfChildrenOfItem:)`](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md) method return `0` for the number of items when the data source has not yet been configured. In [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()), when the data source is initialized you should always call [`reloadData()`](nstableview/reloaddata().md).

For more information about using NSOutlineView in your app, see [`Navigating Hierarchical Data Using Outline and Split Views`](navigating-hierarchical-data-using-outline-and-split-views.md).

##### Subclassing

Subclassing `NSOutlineView` is not recommended. Customization can be accomplished in your data source class implementation (conforming to [`NSOutlineViewDataSource`](nsoutlineviewdatasource.md)) or your delegate class implementation (conforming to [`NSOutlineViewDelegate`](nsoutlineviewdelegate.md)).

## Topics

### Accessing the Data Source
- [var dataSource: (any NSOutlineViewDataSource)?](nsoutlineview/datasource.md)
  The object that provides the data displayed by the receiver.
- [var stronglyReferencesItems: Bool](nsoutlineview/stronglyreferencesitems.md)
  A Boolean value that indicates whether the outline view retains and releases the objects returned from its data source.
### Working with Expandability
- [func isExpandable(Any?) -> Bool](nsoutlineview/isexpandable(_:).md)
  Returns a Boolean value that indicates whether a given item is expandable.
- [func isItemExpanded(Any?) -> Bool](nsoutlineview/isitemexpanded(_:).md)
  Returns a Boolean value that indicates whether a given item is expanded.
### Expanding and Collapsing the Outline
- [func expandItem(Any?)](nsoutlineview/expanditem(_:).md)
  Expands a given item.
- [func expandItem(Any?, expandChildren: Bool)](nsoutlineview/expanditem(_:expandchildren:).md)
  Expands a specified item and, optionally, its children.
- [func collapseItem(Any?)](nsoutlineview/collapseitem(_:).md)
  Collapses a given item.
- [func collapseItem(Any?, collapseChildren: Bool)](nsoutlineview/collapseitem(_:collapsechildren:).md)
  Collapses a given item and, optionally, its children.
### Redisplaying Information
- [func reloadItem(Any?)](nsoutlineview/reloaditem(_:).md)
  Reloads and redisplays the data for the given item.
- [func reloadItem(Any?, reloadChildren: Bool)](nsoutlineview/reloaditem(_:reloadchildren:).md)
  Reloads a given item and, optionally, its children.
### Converting Between Items and Rows
- [func item(atRow: Int) -> Any?](nsoutlineview/item(atrow:).md)
  Returns the item associated with a given row.
- [func row(forItem: Any?) -> Int](nsoutlineview/row(foritem:).md)
  Returns the row associated with a given item.
### Working with the Outline Column
- [var outlineTableColumn: NSTableColumn?](nsoutlineview/outlinetablecolumn.md)
  The table column in which hierarchical data is displayed.
- [var autoresizesOutlineColumn: Bool](nsoutlineview/autoresizesoutlinecolumn.md)
  A Boolean value that indicates whether the outline view resizes its outline column when the user expands or collapses items.
### Working with Indentation
- [func level(forItem: Any?) -> Int](nsoutlineview/level(foritem:).md)
  Returns the indentation level for a given item.
- [func level(forRow: Int) -> Int](nsoutlineview/level(forrow:).md)
  Returns the indentation level for a given row.
- [var indentationPerLevel: CGFloat](nsoutlineview/indentationperlevel.md)
  The per-level indentation, measured in points.
- [var indentationMarkerFollowsCell: Bool](nsoutlineview/indentationmarkerfollowscell.md)
  A Boolean value indicating whether the indentation marker symbol displayed in the outline column should be indented along with the cell contents.
### Working with Persistence
- [var autosaveExpandedItems: Bool](nsoutlineview/autosaveexpandeditems.md)
  A Boolean value indicating whether the expanded items are automatically saved across launches of the app.
### Supporting Drag and Drop
- [func setDropItem(Any?, dropChildIndex: Int)](nsoutlineview/setdropitem(_:dropchildindex:).md)
  Used to “retarget” a proposed drop.
- [func shouldCollapseAutoExpandedItems(forDeposited: Bool) -> Bool](nsoutlineview/shouldcollapseautoexpandeditems(fordeposited:).md)
  Returns a Boolean value that indicates whether auto-expanded items should return to their original collapsed state.
### Getting Related Items
- [func parent(forItem: Any?) -> Any?](nsoutlineview/parent(foritem:).md)
  Returns the parent for a given item.
- [func childIndex(forItem: Any) -> Int](nsoutlineview/childindex(foritem:).md)
  Returns the child index of the specified item within its parent.
- [func child(Int, ofItem: Any?) -> Any?](nsoutlineview/child(_:ofitem:).md)
  Returns the specified child of an item.
- [func numberOfChildren(ofItem: Any?) -> Int](nsoutlineview/numberofchildren(ofitem:).md)
  Returns the number of children for the specified parent item.
### Getting the Frame for a Cell
- [func frameOfOutlineCell(atRow: Int) -> NSRect](nsoutlineview/frameofoutlinecell(atrow:).md)
  Returns the frame of the outline cell for a given row.
### Accessing the Delegate
- [var delegate: (any NSOutlineViewDelegate)?](nsoutlineview/delegate.md)
  The outline view’s delegate.
### Manipulating Items
- [func insertItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](nsoutlineview/insertitems(at:inparent:withanimation:).md)
  Inserts new items at the given indexes in the given parent with the specified optional animations.
- [func moveItem(at: Int, inParent: Any?, to: Int, inParent: Any?)](nsoutlineview/moveitem(at:inparent:to:inparent:).md)
  Moves an item at a given index in the given parent to a new index in a new parent.
- [func removeItems(at: IndexSet, inParent: Any?, withAnimation: NSTableView.AnimationOptions)](nsoutlineview/removeitems(at:inparent:withanimation:).md)
  Removes items at the given indexes in the given parent with the specified optional animations.
### User Interface Layout Direction
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nsoutlineview/userinterfacelayoutdirection.md)
  The user interface layout direction.
### Constants
- [Drop on Item Index](drop-on-item-index.md)
  This constant defines an index that allows you to drop an item directly on a target.
- [Outline View Button Keys](outline-view-button-keys.md)
  These keys are used by the outline view to create disclosure buttons that collapse and expand items.
### Notifications
- [class let columnDidMoveNotification: NSNotification.Name](nsoutlineview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSOutlineView` object.
- [class let columnDidResizeNotification: NSNotification.Name](nsoutlineview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSOutlineView` object.
- [class let itemDidCollapseNotification: NSNotification.Name](nsoutlineview/itemdidcollapsenotification.md)
  Posted whenever an item is collapsed in an `NSOutlineView` object.
- [class let itemDidExpandNotification: NSNotification.Name](nsoutlineview/itemdidexpandnotification.md)
  Posted whenever an item is expanded in an `NSOutlineView` object.
- [class let itemWillCollapseNotification: NSNotification.Name](nsoutlineview/itemwillcollapsenotification.md)
  Posted before an item is collapsed (after the user clicks the arrow but before the item is collapsed).
- [class let itemWillExpandNotification: NSNotification.Name](nsoutlineview/itemwillexpandnotification.md)
  Posted before an item is expanded (after the user clicks the arrow but before the item is collapsed).
- [class let selectionDidChangeNotification: NSNotification.Name](nsoutlineview/selectiondidchangenotification.md)
  Posted after the outline view’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nsoutlineview/selectionischangingnotification.md)
  Posted as the outline view’s selection changes (while the mouse button is still down).

## Relationships

### Inherits From
- [NSTableView](nstableview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSAccessibilityOutline](nsaccessibilityoutline.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityTable](nsaccessibilitytable.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSDraggingSource](nsdraggingsource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextDelegate](nstextdelegate.md)
- [NSTextViewDelegate](nstextviewdelegate.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Navigating Hierarchical Data Using Outline and Split Views](navigating-hierarchical-data-using-outline-and-split-views.md)
  Build a structured user interface that simplifies navigation in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview)*