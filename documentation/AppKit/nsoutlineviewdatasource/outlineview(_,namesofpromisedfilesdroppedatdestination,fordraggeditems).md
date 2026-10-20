# outlineView(_:namesOfPromisedFilesDroppedAtDestination:forDraggedItems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of filenames for the created files that the receiver promises to create.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSFilePromiseReceiver objects instead

## Declaration

```swift
optional func outlineView(_ outlineView: NSOutlineView, namesOfPromisedFilesDroppedAtDestination dropDestination: URL, forDraggedItems items: [Any]) -> [String]
```

```objc
- (NSArray<NSString *> *) outlineView:(NSOutlineView *) outlineView namesOfPromisedFilesDroppedAtDestination:(NSURL *) dropDestination forDraggedItems:(NSArray *) items;
```

#### Return Value

An array of filenames (not full paths) for the created files that the receiver promises to create.

#### Discussion

For more information on file promise dragging, see documentation on the `NSDraggingSource` protocol and [`namesOfPromisedFilesDropped(atDestination:)`](../nsdragginginfo/namesofpromisedfilesdropped%28atdestination%29.md).

## Parameters

- `outlineView`: The outline view that sent the message.
- `dropDestination`: The drop location where the files are created.
- `items`: The items being dragged.

## See Also

### Instance Methods
- [func outlineView(NSOutlineView, acceptDrop: any NSDraggingInfo, item: Any?, childIndex: Int) -> Bool](./outlineview%28_,acceptdrop,item,childindex%29.md)
  Returns a Boolean value that indicates whether a drop operation was successful.
- [func outlineView(NSOutlineView, child: Int, ofItem: Any?) -> Any](./outlineview%28_,child,ofitem%29.md)
  Returns the child item at the specified index of a given item.
- [func outlineView(NSOutlineView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./outlineview%28_,draggingsession,endedat,operation%29.md)
  Implement this method to know when the given dragging session has ended.
- [func outlineView(NSOutlineView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItems: [Any])](./outlineview%28_,draggingsession,willbeginat,foritems%29.md)
  Implement this method know when the given dragging session is about to begin and potentially modify the dragging session.
- [func outlineView(NSOutlineView, isItemExpandable: Any) -> Bool](./outlineview%28_,isitemexpandable%29.md)
  Returns a Boolean value that indicates whether the a given item is expandable.
- [func outlineView(NSOutlineView, itemForPersistentObject: Any) -> Any?](./outlineview%28_,itemforpersistentobject%29.md)
  Invoked by `outlineView` to return the item for the archived `object`.
- [func outlineView(NSOutlineView, numberOfChildrenOfItem: Any?) -> Int](./outlineview%28_,numberofchildrenofitem%29.md)
  Returns the number of child items encompassed by a given item.
- [func outlineView(NSOutlineView, objectValueFor: NSTableColumn?, byItem: Any?) -> Any?](./outlineview%28_,objectvaluefor,byitem%29.md)
  Invoked by `outlineView` to return the data object associated with the specified `item`.
- [func outlineView(NSOutlineView, pasteboardWriterForItem: Any) -> (any NSPasteboardWriting)?](./outlineview%28_,pasteboardwriterforitem%29.md)
  Implement this method to enable the table to be an `NSDraggingSource` that supports dragging multiple items.
- [func outlineView(NSOutlineView, persistentObjectForItem: Any?) -> Any?](./outlineview%28_,persistentobjectforitem%29.md)
  Invoked by `outlineView` to return an archived object for `item`.
- [func outlineView(NSOutlineView, setObjectValue: Any?, for: NSTableColumn?, byItem: Any?)](./outlineview%28_,setobjectvalue,for,byitem%29.md)
  Set the data object for a given item in a given column.
- [func outlineView(NSOutlineView, sortDescriptorsDidChange: [NSSortDescriptor])](./outlineview%28_,sortdescriptorsdidchange%29.md)
  Invoked by an outline view to notify the data source that the descriptors changed and the data may need to be resorted.
- [func outlineView(NSOutlineView, updateDraggingItemsForDrag: any NSDraggingInfo)](./outlineview%28_,updatedraggingitemsfordrag%29.md)
  Implement this method to enable the table to update dragging items as they are dragged over the view.
- [func outlineView(NSOutlineView, validateDrop: any NSDraggingInfo, proposedItem: Any?, proposedChildIndex: Int) -> NSDragOperation](./outlineview%28_,validatedrop,proposeditem,proposedchildindex%29.md)
  Used by an outline view to determine a valid drop target.
- [func outlineView(NSOutlineView, writeItems: [Any], to: NSPasteboard) -> Bool](./outlineview%28_,writeitems,to%29.md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/outlineview(_:namesofpromisedfilesdroppedatdestination:fordraggeditems:))*