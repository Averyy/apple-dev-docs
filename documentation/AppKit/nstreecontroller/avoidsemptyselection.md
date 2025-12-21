# avoidsEmptySelection

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the tree controller requires the content array to attempt to maintain a selection at all times, avoiding an empty selection.

**Availability**:
- macOS ?+

## Declaration

```swift
var avoidsEmptySelection: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the tree controller maintains a selection unless there are no objects in the content. The default value is [`true`](https://developer.apple.com/documentation/Swift/true). This property is observable using key-value observing.

## See Also

- [var selectsInsertedObjects: Bool](nstreecontroller/selectsinsertedobjects.md)
  A Boolean value that indicates whether the tree controller automatically selects objects as they are inserted.
- [func addSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/addselectionindexpaths(_:).md)
  Adds the objects at the specified `indexPaths` in the tree controller’s content to the current selection.
- [func removeSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/removeselectionindexpaths(_:).md)
  Removes the objects at the specified index paths from the tree controller’s current selection.
- [var preservesSelection: Bool](nstreecontroller/preservesselection.md)
  A Boolean value that indicates whether the tree controller will attempt to preserve the current selection when the content changes.
- [var alwaysUsesMultipleValuesMarker: Bool](nstreecontroller/alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the tree controller always returns the multiple values marker when multiple objects are selected, even if the selected items have the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/avoidsemptyselection)*