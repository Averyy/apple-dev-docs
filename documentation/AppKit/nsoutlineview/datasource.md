# dataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that provides the data displayed by the receiver.

**Availability**:
- macOS

## Declaration

```swift
weak var dataSource: (any NSOutlineViewDataSource)? { get set }
```

```objc
@property (weak, nullable) id<NSOutlineViewDataSource> dataSource;
```

#### Discussion

The object must implement the appropriate methods of [`NSOutlineViewDataSource`](../nsoutlineviewdatasource.md). Note that in versions of macOS prior to v10.12, the outline view did not retain the data source in a managed memory environment.

Setting the data source invokes [`tile()`](../nstableview/tile%28%29.md).

If the data source doesn’t respond to all of the [`outlineView(_:child:ofItem:)`](../nsoutlineviewdatasource/outlineview%28_,child,ofitem%29.md), [`outlineView(_:isItemExpandable:)`](../nsoutlineviewdatasource/outlineview%28_,isitemexpandable%29.md), [`outlineView(_:numberOfChildrenOfItem:)`](../nsoutlineviewdatasource/outlineview%28_,numberofchildrenofitem%29.md), and [`outlineView(_:objectValueFor:byItem:)`](../nsoutlineviewdatasource/outlineview%28_,objectvaluefor,byitem%29.md) methods, an [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) may be raised.

## See Also

### Related Documentation
- [Drag and Drop](../drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Outline View](../outline-view.md)
  Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one.
### Accessing the Data Source
- [var stronglyReferencesItems: Bool](./stronglyreferencesitems.md)
  A Boolean value that indicates whether the outline view retains and releases the objects returned from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/datasource)*