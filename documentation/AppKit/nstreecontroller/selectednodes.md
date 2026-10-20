# selectedNodes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the tree controller’s selected tree nodes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var selectedNodes: [NSTreeNode] { get }
```

```objc
@property (copy, readonly) NSArray<NSTreeNode *> * selectedNodes;
```

## See Also

### Getting the current selection
- [func setSelectionIndexPath(IndexPath?) -> Bool](./setselectionindexpath%28_%29.md)
  Sets the tree controller’s current selection.
- [var selectionIndexPath: IndexPath?](./selectionindexpath.md)
  The index path of the first selected object.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](./setselectionindexpaths%28_%29.md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectionIndexPaths: [IndexPath]](./selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedObjects: [Any]](./selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectednodes)*