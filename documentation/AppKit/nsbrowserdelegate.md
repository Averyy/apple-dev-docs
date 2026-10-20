# NSBrowserDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that a browser delegate implements to manage selection, scrolling, sizing, and other behavior.

**Availability**:
- macOS

## Declaration

```swift
protocol NSBrowserDelegate : NSObjectProtocol
```

```objc
@protocol NSBrowserDelegate <NSObject>
```

## Topics

### Getting Browser Information
- [func browser(NSBrowser, isColumnValid: Int) -> Bool](./nsbrowserdelegate/browser%28_,iscolumnvalid%29.md)
  Returns whether the contents of the specified column are valid.
- [func browser(NSBrowser, numberOfRowsInColumn: Int) -> Int](./nsbrowserdelegate/browser%28_,numberofrowsincolumn%29.md)
  Returns the number of rows of data in the specified column.
- [func browser(NSBrowser, numberOfChildrenOfItem: Any?) -> Int](./nsbrowserdelegate/browser%28_,numberofchildrenofitem%29.md)
  Asks the delegate for the number of children the given item has.
- [func browser(NSBrowser, titleOfColumn: Int) -> String?](./nsbrowserdelegate/browser%28_,titleofcolumn%29.md)
  Asks the delegate for the title to display above the specified column.
### Managing Selection Behavior
- [func browser(NSBrowser, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](./nsbrowserdelegate/browser%28_,shouldtypeselectfor,withcurrentsearch%29.md)
  Sent to the delegate to determine whether keyboard-based selection (type select) for a given event and search string should proceed.
- [func browser(NSBrowser, typeSelectStringForRow: Int, inColumn: Int) -> String?](./nsbrowserdelegate/browser%28_,typeselectstringforrow,incolumn%29.md)
  Sent to the delegate to get the keyboard-based selection (type select) string for the specified row and column.
- [func browser(NSBrowser, nextTypeSelectMatchFromRow: Int, toRow: Int, inColumn: Int, for: String?) -> Int](./nsbrowserdelegate/browser%28_,nexttypeselectmatchfromrow,torow,incolumn,for%29.md)
  Sent to the delegate to customize a browser’s keyboard-based selection (type select) behavior.
### Managing Selection
- [func browser(NSBrowser, selectCellWith: String, inColumn: Int) -> Bool](./nsbrowserdelegate/browser%28_,selectcellwith,incolumn%29.md)
  Asks the delegate to select the cell with the given title in the specified column.
- [func browser(NSBrowser, selectRow: Int, inColumn: Int) -> Bool](./nsbrowserdelegate/browser%28_,selectrow,incolumn%29.md)
  Asks the delegate to select the cell at the specified row and column location.
- [func browser(NSBrowser, selectionIndexesForProposedSelection: IndexSet, inColumn: Int) -> IndexSet](./nsbrowserdelegate/browser%28_,selectionindexesforproposedselection,incolumn%29.md)
  Asks the delegate for a set of indexes to select when the user changes the selection in the browser with the keyboard or mouse.
### Accessing Components
- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](./nsbrowserdelegate/browser%28_,child,ofitem%29.md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, isLeafItem: Any?) -> Bool](./nsbrowserdelegate/browser%28_,isleafitem%29.md)
  Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).
- [func browser(NSBrowser, shouldEditItem: Any?) -> Bool](./nsbrowserdelegate/browser%28_,shouldedititem%29.md)
  Asks the delegate whether the browser may start an editing session for the specified item.
- [func browser(NSBrowser, objectValueForItem: Any?) -> Any?](./nsbrowserdelegate/browser%28_,objectvalueforitem%29.md)
  Returns the object that the specified item uses to draw its contents.
- [func browser(NSBrowser, setObjectValue: Any?, forItem: Any?)](./nsbrowserdelegate/browser%28_,setobjectvalue,foritem%29.md)
  Sets the object that the specified item uses to draw its contents to the specified object.
- [func rootItem(for: NSBrowser) -> Any?](./nsbrowserdelegate/rootitem%28for%29.md)
  Asks the delegate to return the root item of the browser.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](./nsbrowserdelegate/browser%28_,previewviewcontrollerforleafitem%29.md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](./nsbrowserdelegate/browser%28_,headerviewcontrollerforitem%29.md)
  Asks the delegate for a controller that provides a header view for the specified column item.
### Managing Columns
- [func browser(NSBrowser, createRowsForColumn: Int, in: NSMatrix)](./nsbrowserdelegate/browser%28_,createrowsforcolumn,in%29.md)
  Creates a row in the given matrix for each row of data in the specified column of the browser.
- [func browser(NSBrowser, willDisplayCell: Any, atRow: Int, column: Int)](./nsbrowserdelegate/browser%28_,willdisplaycell,atrow,column%29.md)
  Gives the delegate the opportunity to modify the specified cell at the given row and column location before the browser displays it.
- [func browser(NSBrowser, didChangeLastColumn: Int, toColumn: Int)](./nsbrowserdelegate/browser%28_,didchangelastcolumn,tocolumn%29.md)
  Tells the delegate that the browser’s last column changed.
### Scrolling
- [func browserWillScroll(NSBrowser)](./nsbrowserdelegate/browserwillscroll%28_%29.md)
  Notifies the delegate when the browser will scroll.
- [func browserDidScroll(NSBrowser)](./nsbrowserdelegate/browserdidscroll%28_%29.md)
  Notifies the delegate when the browser has scrolled.
### Dragging
- [func browser(NSBrowser, canDragRowsWith: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./nsbrowserdelegate/browser%28_,candragrowswith,incolumn,with%29.md)
  Sent to the delegate to determine whether the browser can attempt to initiate a drag of the specified rows for the specified event.
- [func browser(NSBrowser, draggingImageForRowsWith: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer) -> NSImage?](./nsbrowserdelegate/browser%28_,draggingimageforrowswith,incolumn,with,offset%29.md)
  Sent to the delegate to obtain an image to represent dragged rows during a drag operation on a browser.
- [func browser(NSBrowser, validateDrop: any NSDraggingInfo, proposedRow: UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, dropOperation: UnsafeMutablePointer<NSBrowser.DropOperation>) -> NSDragOperation](./nsbrowserdelegate/browser%28_,validatedrop,proposedrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether a drop should be accepted and to obtain the drop location. This method is required for a browser to be a drag destination.
- [func browser(NSBrowser, acceptDrop: any NSDraggingInfo, atRow: Int, column: Int, dropOperation: NSBrowser.DropOperation) -> Bool](./nsbrowserdelegate/browser%28_,acceptdrop,atrow,column,dropoperation%29.md)
  Sent to the delegate during a dragging session to determine whether to accept the drop.
- [func browser(NSBrowser, writeRowsWith: IndexSet, inColumn: Int, to: NSPasteboard) -> Bool](./nsbrowserdelegate/browser%28_,writerowswith,incolumn,to%29.md)
  Determines whether a drag operation can proceed. This method is required for a browser to be a drag source.
- [func browser(NSBrowser, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedRowsWith: IndexSet, inColumn: Int) -> [String]](./nsbrowserdelegate/browser%28_,namesofpromisedfilesdroppedatdestination,fordraggedrowswith,incolumn%29.md)
  Implements file promise drag operations.
### Sizing
- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](./nsbrowserdelegate/browser%28_,shouldsizecolumn,foruserresize,towidth%29.md)
  Used to determine a column’s initial size.
- [func browser(NSBrowser, sizeToFitWidthOfColumn: Int) -> CGFloat](./nsbrowserdelegate/browser%28_,sizetofitwidthofcolumn%29.md)
  Returns the ideal width for a column.
- [func browserColumnConfigurationDidChange(Notification)](./nsbrowserdelegate/browsercolumnconfigurationdidchange%28_%29.md)
  Used by clients to implement their own column width persistence.
- [func browser(NSBrowser, heightOfRow: Int, inColumn: Int) -> CGFloat](./nsbrowserdelegate/browser%28_,heightofrow,incolumn%29.md)
  Specifies the height of the specified row in the specified column.
### Displaying Cell Content
- [func browser(NSBrowser, shouldShowCellExpansionForRow: Int, column: Int) -> Bool](./nsbrowserdelegate/browser%28_,shouldshowcellexpansionforrow,column%29.md)
  Invoked to allow the delegate to control cell expansion for a specific row and column.
### Instance Methods
- [func browser(NSBrowser, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./nsbrowserdelegate/browser%28_,draggingsession,endedat,operation%29.md)
- [func browser(NSBrowser, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forRowsWith: IndexSet, column: Int)](./nsbrowserdelegate/browser%28_,draggingsession,willbeginat,forrowswith,column%29.md)
- [func browser(NSBrowser, pasteboardWriterForRow: Int, column: Int) -> (any NSPasteboardWriting)?](./nsbrowserdelegate/browser%28_,pasteboardwriterforrow,column%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate)*