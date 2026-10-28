# selectionIndexPath

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index path of the first selected object.

**Availability**:
- macOS

## Declaration

```swift
var selectionIndexPath: IndexPath? { get }
```

```objc
@property (copy, readonly, nullable) NSIndexPath * selectionIndexPath;
```

## Discussion

The value of this property is `nil` if there is no selection. This property is observable using key-value observing.

## See Also

### Getting the current selection
- [func setSelectionIndexPath(IndexPath?) -> Bool](./setselectionindexpath%28_%29.md)
  Sets the tree controller’s current selection.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](./setselectionindexpaths%28_%29.md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectionIndexPaths: [IndexPath]](./selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedObjects: [Any]](./selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](./selectednodes.md)
  An array containing the tree controller’s selected tree nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectionindexpath)*