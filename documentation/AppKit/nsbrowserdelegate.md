# NSBrowserDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a browser delegate implements to manage selection, scrolling, sizing, and other behavior.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSBrowserDelegate : NSObjectProtocol
```

## Topics

### Getting Browser Information
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](nsbrowserdelegate/browser(_:iscolumnvalid:).md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](nsbrowserdelegate/browser(_:numberofrowsincolumn:).md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](nsbrowserdelegate/browser(_:numberofchildrenofitem:).md)
  Asks the delegate for the number of children the given item has.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](nsbrowserdelegate/browser(_:titleofcolumn:).md)
  Asks the delegate for the title to display above the specified column.
### Managing Selection Behavior
- [func browser(NSBrowser, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](nsbrowserdelegate/browser(_:shouldtypeselectfor:withcurrentsearch:).md)
  Sent to the delegate to determine whether keyboard-based selection (type select) for a given event and search string should proceed.
- [func browser(NSBrowser, typeSelectStringForRow: Int, inColumn: Int) -> String?](nsbrowserdelegate/browser(_:typeselectstringforrow:incolumn:).md)
  Sent to the delegate to get the keyboard-based selection (type select) string for the specified row and column.
- [func browser(NSBrowser, nextTypeSelectMatchFromRow: Int, toRow: Int, inColumn: Int, for: String?) -> Int](nsbrowserdelegate/browser(_:nexttypeselectmatchfromrow:torow:incolumn:for:).md)
  Sent to the delegate to customize a browser’s keyboard-based selection (type select) behavior.
### Managing Selection
- [func browser(NSBrowser, selectCellWith: String, inColumn: Int) -> Bool](nsbrowserdelegate/browser(_:selectcellwith:incolumn:).md)
  Asks the delegate to select the cell with the given title in the specified column.
- [func browser(NSBrowser, selectRow: Int, inColumn: Int) -> Bool](nsbrowserdelegate/browser(_:selectrow:incolumn:).md)
  Asks the delegate to select the cell at the specified row and column location.
- [func browser(NSBrowser, selectionIndexesForProposedSelection: IndexSet, inColumn: Int) -> IndexSet](nsbrowserdelegate/browser(_:selectionindexesforproposedselection:incolumn:).md)
  Asks the delegate for a set of indexes to select when the user changes the selection in the browser with the keyboard or mouse.
### Accessing Components
- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](nsbrowserdelegate/browser(_:child:ofitem:).md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, isLeafItem: Any?) -> Bool](nsbrowserdelegate/browser(_:isleafitem:).md)
  Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).
- [func browser(NSBrowser, shouldEditItem: Any?) -> Bool](nsbrowserdelegate/browser(_:shouldedititem:).md)
  Asks the delegate whether the browser may start an editing session for the specified item.
- [func browser(NSBrowser, objectValueForItem: Any?) -> Any?](nsbrowserdelegate/browser(_:objectvalueforitem:).md)
  Returns the object that the specified item uses to draw its contents.
- [func browser(NSBrowser, setObjectValue: Any?, forItem: Any?)](nsbrowserdelegate/browser(_:setobjectvalue:foritem:).md)
  Sets the object that the specified item uses to draw its contents to the specified object.
- [func rootItem(for: NSBrowser) -> Any?](nsbrowserdelegate/rootitem(for:).md)
  Asks the delegate to return the root item of the browser.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](nsbrowserdelegate/browser(_:previewviewcontrollerforleafitem:).md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](nsbrowserdelegate/browser(_:headerviewcontrollerforitem:).md)
  Asks the delegate for a controller that provides a header view for the specified column item.
### Managing Columns
- [func browser(NSBrowser, createRowsForColumn: Int, in: NSMatrix)](nsbrowserdelegate/browser(_:createrowsforcolumn:in:).md)
  Creates a row in the given matrix for each row of data in the specified column of the browser.
- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](nsbrowserdelegate/browser(_:willdisplaycell:atrow:column:).md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.
- [func browser(NSBrowser, didChangeLastColumn: Int, toColumn: Int)](nsbrowserdelegate/browser(_:didchangelastcolumn:tocolumn:).md)
  Tells the delegate that the browser’s last column changed.
### Scrolling
- [func browserWillScroll(NSBrowser)](nsbrowserdelegate/browserwillscroll(_:).md)
  Notifies the delegate when the browser will scroll.
- [func browserDidScroll(NSBrowser)](nsbrowserdelegate/browserdidscroll(_:).md)
  Notifies the delegate when the browser has scrolled.
### Dragging
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowserdelegate/browser(_:candragrowswith:incolumn:with:).md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](nsbrowserdelegate/browser(_:draggingimageforrowswith:incolumn:with:offset:).md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](nsbrowserdelegate/browser(_:validatedrop:proposedrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](nsbrowserdelegate/browser(_:acceptdrop:atrow:column:dropoperation:).md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](nsbrowserdelegate/browser(_:writerowswith:incolumn:to:).md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](nsbrowserdelegate/browser(_:namesofpromisedfilesdroppedatdestination:fordraggedrowswith:incolumn:).md)
  Implements file promise drag operations.
### Sizing
- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](nsbrowserdelegate/browser(_:shouldsizecolumn:foruserresize:towidth:).md)
  Used to determine a column’s initial size.
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](nsbrowserdelegate/browser(_:sizetofitwidthofcolumn:).md)
  Returns the ideal width for a column.
- [func browserColumnConfigurationDidChange(Notification)](nsbrowserdelegate/browsercolumnconfigurationdidchange(_:).md)
  Used by clients to implement their own column width persistence.
- [func browser(NSBrowser, heightOfRow: Int, inColumn: Int) -> CGFloat](nsbrowserdelegate/browser(_:heightofrow:incolumn:).md)
  Specifies the height of the specified row in the specified column.
### Displaying Cell Content
- [func browser(NSBrowser, shouldShowCellExpansionForRow: Int, column: Int) -> Bool](nsbrowserdelegate/browser(_:shouldshowcellexpansionforrow:column:).md)
  Invoked to allow the delegate to control cell expansion for a specific row and column.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate)*