# dataSource

**Framework**: AppKit  
**Kind**: property

The object that provides the data displayed by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var dataSource: (any NSOutlineViewDataSource)? { get set }
```

#### Discussion

The object must implement the appropriate methods of [`NSOutlineViewDataSource`](nsoutlineviewdatasource.md). Note that in versions of macOS prior to v10.12, the outline view did not retain the data source in a managed memory environment.

Setting the data source invokes [`tile()`](nstableview/tile().md).

If the data source doesn’t respond to all of the [`outlineView(_:child:ofItem:)`](nsoutlineviewdatasource/outlineview(_:child:ofitem:).md), [`outlineView(_:isItemExpandable:)`](nsoutlineviewdatasource/outlineview(_:isitemexpandable:).md), [`outlineView(_:numberOfChildrenOfItem:)`](nsoutlineviewdatasource/outlineview(_:numberofchildrenofitem:).md), and [`outlineView(_:objectValueFor:byItem:)`](nsoutlineviewdatasource/outlineview(_:objectvaluefor:byitem:).md) methods, an [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException) may be raised.

## See Also

- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Outline View](outline-view.md)
  Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one.
- [var stronglyReferencesItems: Bool](nsoutlineview/stronglyreferencesitems.md)
  A Boolean value that indicates whether the outline view retains and releases the objects returned from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/datasource)*