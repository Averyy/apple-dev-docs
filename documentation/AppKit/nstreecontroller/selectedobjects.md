# selectedObjects

**Framework**: AppKit  
**Kind**: property

An array containing the currently selected objects in the tree controller’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
var selectedObjects: [Any] { get }
```

#### Discussion

This property is observable using key-value observing.

## See Also

- [func setSelectionIndexPath(IndexPath?) -> Bool](nstreecontroller/setselectionindexpath(_:).md)
  Sets the tree controller’s current selection.
- [var selectionIndexPath: IndexPath?](nstreecontroller/selectionindexpath.md)
  The index path of the first selected object.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/setselectionindexpaths(_:).md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectionIndexPaths: [IndexPath]](nstreecontroller/selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedNodes: [NSTreeNode]](nstreecontroller/selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectedobjects)*