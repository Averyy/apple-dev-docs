# selectionIndexPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the index paths of the currently selected objects.

**Availability**:
- macOS

## Declaration

```swift
var selectionIndexPaths: [IndexPath] { get }
```

```objc
@property (copy, readonly) NSArray<NSIndexPath *> * selectionIndexPaths;
```

## Discussion

This property contains an array containing [`NSIndexPath`](../../Foundation/nsindexpath.md) objects for each of the selected objects in the tree controller’s content. This property is observable using key-value observing.

## See Also

### Getting the current selection
- [func setSelectionIndexPath(IndexPath?) -> Bool](./setselectionindexpath%28_%29.md)
  Sets the tree controller’s current selection.
- [var selectionIndexPath: IndexPath?](./selectionindexpath.md)
  The index path of the first selected object.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](./setselectionindexpaths%28_%29.md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectedObjects: [Any]](./selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](./selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectionindexpaths)*