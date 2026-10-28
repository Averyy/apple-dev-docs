# outlineView(_:draggingSession:endedAt:operation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implement this method to know when the given dragging session has ended.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, draggingSession session: NSDraggingSession, endedAt screenPoint: NSPoint, operation: NSDragOperation)
```

```objc
- (void) outlineView:(NSOutlineView *) outlineView draggingSession:(NSDraggingSession *) session endedAtPoint:(NSPoint) screenPoint operation:(NSDragOperation) operation;
```

## Discussion

You can implement this optional delegate method to know when the dragging source operation ended at a specific location, such as the trash (by checking for an operation of [`delete`](../nsdragoperation/delete.md)).

## Parameters

- `outlineView`: The outline view in which the drag began.
- `session`: The dragging session that ended.
- `screenPoint`: The point onscreen at which the drag ended.
- `operation`: A mask specifying the types of drag operations permitted by the dragging source.

## See Also

### Instance Methods
- [func outlineView(NSOutlineView, acceptDrop: any NSDraggingInfo, item: Any?, childIndex: Int) -> Bool](./outlineview%28_,acceptdrop,item,childindex%29.md)
  Returns a Boolean value that indicates whether a drop operation was successful.
- [func outlineView(NSOutlineView, child: Int, ofItem: Any?) -> Any](./outlineview%28_,child,ofitem%29.md)
  Returns the child item at the specified index of a given item.
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
- [func outlineView(NSOutlineView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItems: [Any]) -> [String]](./outlineview%28_,namesofpromisedfilesdroppedatdestination,fordraggeditems%29.md)
  Returns an array of filenames for the created files that the receiver promises to create.
- [func outlineView(NSOutlineView, writeItems: [Any], to: NSPasteboard) -> Bool](./outlineview%28_,writeitems,to%29.md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/outlineview(_:draggingsession:endedat:operation:))*