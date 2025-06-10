# NSOutlineViewDataSource

**Framework**: AppKit  
**Kind**: protocol

A set of methods that an outline view calls to retrieve data and information about it from the data source delegate, and—optionally—to update data values.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSOutlineViewDataSource : NSObjectProtocol
```

#### Overview

[`NSOutlineView`](nsoutlineview.md) objects support a data source delegate in addition to the regular delegate object.

All the methods in the [`NSOutlineViewDataSource`](nsoutlineviewdatasource.md) protocol are marked as `@optional`. While this is true, there are cases were you must implement some methods to achieve required functionality, specifically when working with conventional data sources rather than data that is provided by Cocoa bindings.

##### Required and Optional Methods Using Programmatic Conventions and Cocoa Bindings

If you are using conventional data sources for content you must implement the basic methods that provide the outline view with data: [`outlineView(_:child:ofItem:)`](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md), [`outlineView(_:isItemExpandable:)`](nsoutlineviewdatasource/outlineview(_:isitemexpandable:).md), [`outlineView(_:numberOfChildrenOfItem:)`](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md), and [`outlineView(_:objectValueFor:byItem:)`](nsoutlineviewdatasource/outlineview(_:objectvaluefor:byitem:).md). Applications that acquire their data using Cocoa bindings do not need to implement these methods.

Similarly, when using conventional data sources , if you want to allow the user to edit values, you must implement [`outlineView(_:setObjectValue:for:byItem:)`](nsoutlineviewdatasource/outlineview(_:setobjectvalue:for:byitem:).md). When these methods are invoked by the outline view, `nil` as the `item` refers to the “root” item. `NSOutlineView` requires that each item in the outline view be unique. In order for the collapsed state of an outline view to remain consistent between reloads you must always return the same object for an item. When using Cocoa bindings to provide outline view content, there is no requirement to implement this method.

> **Note**:  Some of the methods in this `protocol`, such as [`outlineView(_:child:ofItem:)`](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md) and [`outlineView(_:numberOfChildrenOfItem:)`](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md) along with other methods that return data, are called very frequently, so they must be efficient.

## Topics

### Instance Methods
- [func outlineView(NSOutlineView, acceptDrop: any NSDraggingInfo, item: Any?, childIndex: Int) -> Bool](nsoutlineviewdatasource/outlineview(_:acceptdrop:item:childindex:).md)
  Returns a Boolean value that indicates whether a drop operation was successful.
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

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSOutlineViewDelegate](nsoutlineviewdelegate.md)
  A set of optional methods implemented by delegates of [`NSOutlineView`](nsoutlineview.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource)*