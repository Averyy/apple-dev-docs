# outlineView(_:child:ofItem:)

**Framework**: AppKit  
**Kind**: method

Returns the child item at the specified index of a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, child index: Int, ofItem item: Any?) -> Any
```

#### Return Value

The child item at `index` of `item`. If `item` is `nil`, returns the appropriate child item of the root object.

#### Discussion

Children of a given parent `item` are accessed sequentially. In order for the collapsed state of the outline view to remain consistent when it is reloaded you must always return the same object for a specified `child` and `item`.

> ❗ **Important**:  While this method is marked as `@optional` in the protocol,  Do not call [`reloadData()`](nstableview/reloaddata().md) from this method.

 While this method is marked as `@optional` in the protocol, 

Do not call [`reloadData()`](nstableview/reloaddata().md) from this method.

##### Special Considerations

The [`outlineView(_:child:ofItem:)`](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md) method is called very frequently, so it must be efficient.

## Parameters

- `outlineView`: The outline view that sent the message.
- `index`: The index of the child item from   to return.
- `item`: An item in the data source.

## See Also

- [func outlineView(NSOutlineView, numberOfChildrenOfItem: Any?) -> Int](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md)
  Returns the number of child items encompassed by a given item.
- [Outline View Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OutlineView/OutlineView.html#//apple_ref/doc/uid/10000023i)
- [func outlineView(NSOutlineView, acceptDrop: any NSDraggingInfo, item: Any?, childIndex: Int) -> Bool](nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:).md)
  Returns a Boolean value that indicates whether a drop operation was successful.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource/outlineview(_:child:ofitem:))*