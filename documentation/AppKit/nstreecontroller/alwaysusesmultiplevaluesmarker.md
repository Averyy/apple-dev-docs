# alwaysUsesMultipleValuesMarker

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the tree controller always returns the multiple values marker when multiple objects are selected, even if the selected items have the same value.

**Availability**:
- macOS

## Declaration

```swift
var alwaysUsesMultipleValuesMarker: Bool { get set }
```

```objc
@property BOOL alwaysUsesMultipleValuesMarker;
```

## Discussion

Setting this property to [`true`](../../Swift/true.md) can increase performance if your application doesn’t allow editing multiple values. The default is [`false`](../../Swift/false.md). This property is observable using key-value observing.

## See Also

### Managing Selections
- [var selectsInsertedObjects: Bool](./selectsinsertedobjects.md)
  A Boolean value that indicates whether the tree controller automatically selects objects as they are inserted.
- [func addSelectionIndexPaths([IndexPath]) -> Bool](./addselectionindexpaths%28_%29.md)
  Adds the objects at the specified `indexPaths` in the tree controller’s content to the current selection.
- [func removeSelectionIndexPaths([IndexPath]) -> Bool](./removeselectionindexpaths%28_%29.md)
  Removes the objects at the specified index paths from the tree controller’s current selection.
- [var avoidsEmptySelection: Bool](./avoidsemptyselection.md)
  A Boolean value that indicates whether the tree controller requires the content array to attempt to maintain a selection at all times, avoiding an empty selection.
- [var preservesSelection: Bool](./preservesselection.md)
  A Boolean value that indicates whether the tree controller will attempt to preserve the current selection when the content changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/alwaysusesmultiplevaluesmarker)*