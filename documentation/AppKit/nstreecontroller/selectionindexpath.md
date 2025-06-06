# selectionIndexPath

**Framework**: AppKit  
**Kind**: property

The index path of the first selected object.

**Availability**:
- macOS ?+

## Declaration

```swift
var selectionIndexPath: IndexPath? { get }
```

#### Discussion

The value of this property is `nil` if there is no selection. This property is observable using key-value observing.

## See Also

- [func setSelectionIndexPath(IndexPath?) -> Bool](nstreecontroller/setselectionindexpath(_:).md)
  Sets the tree controller’s current selection.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/setselectionindexpaths(_:).md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectionIndexPaths: [IndexPath]](nstreecontroller/selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedObjects: [Any]](nstreecontroller/selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](nstreecontroller/selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectionindexpath)*