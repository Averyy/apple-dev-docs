# outlineView(_:acceptDrop:item:childIndex:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether a drop operation was successful.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, acceptDrop info: any NSDraggingInfo, item: Any?, childIndex index: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the drop operation was successful, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The data source should incorporate the data from the dragging pasteboard in the implementation of this method. You can get the data for the drop operation from info using the [`draggingPasteboard`](nsdragginginfo/draggingpasteboard.md) method.

The return value indicates success or failure of the drag operation to the system.

## Parameters

- `outlineView`: The outline view that sent the message.   must have previously allowed a drop.
- `info`: An object that contains more information about this dragging operation.
- `item`: The parent of the item over which the cursor was placed when the mouse button was released.
- `index`: The index of the child of   over which the cursor was placed when the mouse button was released.

## See Also

- [func shouldCollapseAutoExpandedItems(forDeposited: Bool) -> Bool](nsoutlineview/shouldcollapseautoexpandeditems(fordeposited:).md)
  Returns a Boolean value that indicates whether auto-expanded items should return to their original collapsed state.
- [func outlineView(NSOutlineView, child: Int, ofItem: Any?) -> Any](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md)
  Returns the child item at the specified index of a given item.
- [func outlineView(NSOutlineView, draggingSession: NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nsoutlineviewdatasource/outlineview(_:draggingsession:endedat:operation:).md)
  Implement this method to know when the given dragging session has ended.
- [func outlineView(NSOutlineView, draggingSession: NSDraggingSession, willBeginAt: NSPoint, forItems: [Any])](nsoutlineviewdatasource/outlineview(_:draggingsession:willbeginat:foritems:).md)
  Implement this method know when the given dragging session is about to begin and potentially modify the dragging session.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:))*