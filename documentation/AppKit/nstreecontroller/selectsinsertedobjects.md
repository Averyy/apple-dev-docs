# selectsInsertedObjects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the tree controller automatically selects objects as they are inserted.

**Availability**:
- macOS

## Declaration

```swift
var selectsInsertedObjects: Bool { get set }
```

```objc
@property BOOL selectsInsertedObjects;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md). This property is observable using key-value observing.

## See Also

### Managing Selections
- [func addSelectionIndexPaths([IndexPath]) -> Bool](./addselectionindexpaths%28_%29.md)
  Adds the objects at the specified `indexPaths` in the tree controller’s content to the current selection.
- [func removeSelectionIndexPaths([IndexPath]) -> Bool](./removeselectionindexpaths%28_%29.md)
  Removes the objects at the specified index paths from the tree controller’s current selection.
- [var avoidsEmptySelection: Bool](./avoidsemptyselection.md)
  A Boolean value that indicates whether the tree controller requires the content array to attempt to maintain a selection at all times, avoiding an empty selection.
- [var preservesSelection: Bool](./preservesselection.md)
  A Boolean value that indicates whether the tree controller will attempt to preserve the current selection when the content changes.
- [var alwaysUsesMultipleValuesMarker: Bool](./alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the tree controller always returns the multiple values marker when multiple objects are selected, even if the selected items have the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/selectsinsertedobjects)*