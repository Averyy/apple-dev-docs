# outlineView(_:draggingSession:willBeginAt:forItems:)

**Framework**: AppKit  
**Kind**: method

Implement this method know when the given dragging session is about to begin and potentially modify the dragging session.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, draggingSession session: NSDraggingSession, willBeginAt screenPoint: NSPoint, forItems draggedItems: [Any])
```

#### Discussion

The `draggedItems` array directly matches the pasteboard writer array used to begin the dragging session with the `NSView` method [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md). Hence, the order is deterministic, and can be used in [`outlineView(_:acceptDrop:item:childIndex:)`](nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:).md) when enumerating the `NSDraggingInfo` protocol’s pasteboard classes.

## Parameters

- `outlineView`: The outline view in which the drag is about to begin.
- `session`: The dragging session that is about to begin.
- `screenPoint`: The point onscreen at which the drag is to begin.
- `draggedItems`: A array of items to be dragged, excluding items for which   returns  .

## See Also

- [func outlineView(NSOutlineView, acceptDrop: any NSDraggingInfo, item: Any?, childIndex: Int) -> Bool](nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:).md)
  Returns a Boolean value that indicates whether a drop operation was successful.
- [func outlineView(NSOutlineView, child: Int, ofItem: Any?) -> Any](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md)
  Returns the child item at the specified index of a given item.
- [func outlineView(NSOutlineView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nsoutlineviewdatasource/outlineview(_:draggingsession:endedat:operation:).md)
  Implement this method to know when the given dragging session has ended.
- [func outlineView(NSOutlineView, isItemExpandable: Any) -> Bool](nsoutlineviewdatasource/outlineview(_:isitemexpandable:).md)
  Returns a Boolean value that indicates whether the a given item is expandable.
- [func outlineView(NSOutlineView, itemForPersistentObject: Any) -> Any?](nsoutlineviewdatasource/outlineview(_:itemforpersistentobject:).md)
  Invoked by `outlineView` to return the item for the archived `object`.
- [func outlineView(NSOutlineView, namesOfPromisedFilesDroppedAtDestination: URL, forDraggedItems: [Any]) -> [String]](nsoutlineviewdatasource/outlineview(_:namesofpromisedfilesdroppedatdestination:fordraggeditems:).md)
  Returns an array of filenames for the created files that the receiver promises to create.
- [func outlineView(NSOutlineView, numberOfChildrenOfItem: Any?) -> Int](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md)
  Returns the number of child items encompassed by a given item.
- [func outlineView(NSOutlineView, objectValueFor: NSTableColumn?, byItem: Any?) -> Any?](nsoutlineviewdatasource/outlineview(_:objectvaluefor:byitem:).md)
  Invoked by `outlineView` to return the data object associated with the specified `item`.
- [func outlineView(NSOutlineView, pasteboardWriterForItem: Any) -> (any NSPasteboardWriting)?](nsoutlineviewdatasource/outlineview(_:pasteboardwriterforitem:).md)
  Implement this method to enable the table to be an `NSDraggingSource` that supports dragging multiple items.
- [func outlineView(NSOutlineView, persistentObjectForItem: Any?) -> Any?](nsoutlineviewdatasource/outlineview(_:persistentobjectforitem:).md)
  Invoked by `outlineView` to return an archived object for `item`.
- [func outlineView(NSOutlineView, setObjectValue: Any?, for: NSTableColumn?, byItem: Any?)](nsoutlineviewdatasource/outlineview(_:setobjectvalue:for:byitem:).md)
  Set the data object for a given item in a given column.
- [func outlineView(NSOutlineView, sortDescriptorsDidChange: [NSSortDescriptor])](nsoutlineviewdatasource/outlineview(_:sortdescriptorsdidchange:).md)
  Invoked by an outline view to notify the data source that the descriptors changed and the data may need to be resorted.
- [func outlineView(NSOutlineView, updateDraggingItemsForDrag: any NSDraggingInfo)](nsoutlineviewdatasource/outlineview(_:updatedraggingitemsfordrag:).md)
  Implement this method to enable the table to update dragging items as they are dragged over the view.
- [func outlineView(NSOutlineView, validateDrop: any NSDraggingInfo, proposedItem: Any?, proposedChildIndex: Int) -> NSDragOperation](nsoutlineviewdatasource/outlineview(_:validatedrop:proposeditem:proposedchildindex:).md)
  Used by an outline view to determine a valid drop target.
- [func outlineView(NSOutlineView, writeItems: [Any], to: NSPasteboard) -> Bool](nsoutlineviewdatasource/outlineview(_:writeitems:to:).md)
  Returns a Boolean value that indicates whether a drag operation is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/outlineview(_:draggingsession:willbeginat:foritems:))*