# addSelectionIndexPaths(_:)

**Framework**: AppKit  
**Kind**: method

Adds the objects at the specified `indexPaths` in the tree controller’s content to the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
func addSelectionIndexPaths(_ indexPaths: [IndexPath]) -> Bool
```

#### Discussion

Attempting to change the selection may cause a `commitEditing` message which fails, thus denying the selection change.

## See Also

- [var selectsInsertedObjects: Bool](nstreecontroller/selectsinsertedobjects.md)
  A Boolean value that indicates whether the tree controller automatically selects objects as they are inserted.
- [func removeSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/removeselectionindexpaths(_:).md)
  Removes the objects at the specified index paths from the tree controller’s current selection.
- [var avoidsEmptySelection: Bool](nstreecontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the tree controller requires the content array to attempt to maintain a selection at all times, avoiding an empty selection.
- [var preservesSelection: Bool](nstreecontroller/preservesselection.md)
  A Boolean value that indicates whether the tree controller will attempt to preserve the current selection when the content changes.
- [var alwaysUsesMultipleValuesMarker: Bool](nstreecontroller/alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the tree controller always returns the multiple values marker when multiple objects are selected, even if the selected items have the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/addselectionindexpaths(_:))*