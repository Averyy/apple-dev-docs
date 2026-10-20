# setSelectionIndexPaths(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the tree controller’s current selection to the specified index paths.

**Availability**:
- macOS

## Declaration

```swift
func setSelectionIndexPaths(_ indexPaths: [IndexPath]) -> Bool
```

```objc
- (BOOL) setSelectionIndexPaths:(NSArray<NSIndexPath *> *) indexPaths;
```

#### Return Value

Return [`true`](../../Swift/true.md) if the selection has changed, otherwise [`false`](../../Swift/false.md).

#### Discussion

Attempting to change the selection may cause a `commitEditing` message which fails, thus denying the selection change.

## Parameters

- `indexPaths`: An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects specifying the selected objects.

## See Also

### Getting the current selection
- [func setSelectionIndexPath(IndexPath?) -> Bool](./setselectionindexpath%28_%29.md)
  Sets the tree controller’s current selection.
- [var selectionIndexPath: IndexPath?](./selectionindexpath.md)
  The index path of the first selected object.
- [var selectionIndexPaths: [IndexPath]](./selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedObjects: [Any]](./selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](./selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/setselectionindexpaths(_:))*