# setSelectionIndexPath(_:)

**Framework**: AppKit  
**Kind**: method

Sets the tree controller’s current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSelectionIndexPath(_ indexPath: IndexPath?) -> Bool
```

#### Return Value

Return [`true`](https://developer.apple.com/documentation/swift/true) if the selection has changed, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Attempting to change the selection may cause a `commitEditing` message which fails, thus denying the selection change.

## Parameters

- `indexPath`: The proposed new selection.

## See Also

- [var selectionIndexPath: IndexPath?](nstreecontroller/selectionindexpath.md)
  The index path of the first selected object.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/setselectionindexpaths(_:).md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectionIndexPaths: [IndexPath]](nstreecontroller/selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedObjects: [Any]](nstreecontroller/selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](nstreecontroller/selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/setselectionindexpath(_:))*