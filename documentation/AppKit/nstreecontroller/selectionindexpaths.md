# selectionIndexPaths

**Framework**: AppKit  
**Kind**: property

An array containing the index paths of the currently selected objects.

**Availability**:
- macOS ?+

## Declaration

```swift
var selectionIndexPaths: [IndexPath] { get }
```

#### Discussion

This property contains an array containing [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects for each of the selected objects in the tree controller’s content. This property is observable using key-value observing.

## See Also

- [func setSelectionIndexPath(IndexPath?) -> Bool](nstreecontroller/setselectionindexpath(_:).md)
  Sets the tree controller’s current selection.
- [var selectionIndexPath: IndexPath?](nstreecontroller/selectionindexpath.md)
  The index path of the first selected object.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/setselectionindexpaths(_:).md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectedObjects: [Any]](nstreecontroller/selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](nstreecontroller/selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectionindexpaths)*