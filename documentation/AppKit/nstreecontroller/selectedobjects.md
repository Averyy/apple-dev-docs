# selectedObjects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the currently selected objects in the tree controller’s content.

**Availability**:
- macOS

## Declaration

```swift
var selectedObjects: [Any] { get }
```

```objc
@property (copy, readonly) NSArray * selectedObjects;
```

#### Discussion

This property is observable using key-value observing.

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
- [var selectedNodes: [NSTreeNode]](./selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectedobjects)*