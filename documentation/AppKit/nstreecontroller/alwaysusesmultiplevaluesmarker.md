# alwaysUsesMultipleValuesMarker

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the tree controller always returns the multiple values marker when multiple objects are selected, even if the selected items have the same value.

**Availability**:
- macOS ?+

## Declaration

```swift
var alwaysUsesMultipleValuesMarker: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) can increase performance if your application doesn’t allow editing multiple values. The default is [`false`](https://developer.apple.com/documentation/Swift/false). This property is observable using key-value observing.

## See Also

- [var selectsInsertedObjects: Bool](nstreecontroller/selectsinsertedobjects.md)
  A Boolean value that indicates whether the tree controller automatically selects objects as they are inserted.
- [func addSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/addselectionindexpaths(_:).md)
  Adds the objects at the specified `indexPaths` in the tree controller’s content to the current selection.
- [func removeSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/removeselectionindexpaths(_:).md)
  Removes the objects at the specified index paths from the tree controller’s current selection.
- [var avoidsEmptySelection: Bool](nstreecontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the tree controller requires the content array to attempt to maintain a selection at all times, avoiding an empty selection.
- [var preservesSelection: Bool](nstreecontroller/preservesselection.md)
  A Boolean value that indicates whether the tree controller will attempt to preserve the current selection when the content changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/alwaysusesmultiplevaluesmarker)*