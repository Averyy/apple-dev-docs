# setSelectionIndex(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s selection to the given index, and returns a Boolean value that indicates whether the selection was changed.

**Availability**:
- macOS

## Declaration

```swift
func setSelectionIndex(_ index: Int) -> Bool
```

```objc
- (BOOL) setSelectionIndex:(NSUInteger) index;
```

#### Return Value

[`true`](../../Swift/true.md) if the selection was changed, otherwise [`false`](../../Swift/false.md).

#### Discussion

Attempting to change the selection may cause a [`commitEditing()`](../nscontroller/commitediting%28%29.md) message which fails, thus denying the selection change.

## Parameters

- `index`: The index for the selection.

## See Also

### Managing selections
- [var selectionIndex: Int](./selectionindex.md)
  The index of the first object in the receiver’s selection
- [var selectsInsertedObjects: Bool](./selectsinsertedobjects.md)
  A Boolean value that indicates whether the receiver automatically selects inserted objects
- [func setSelectionIndexes(IndexSet) -> Bool](./setselectionindexes%28_%29.md)
  Sets the receiver’s selection indexes and returns a Boolean value that indicates whether the selection changed.
- [var selectionIndexes: IndexSet](./selectionindexes.md)
  An index set containing the indexes of the receiver’s currently selected objects in the content array
- [func addSelectionIndexes(IndexSet) -> Bool](./addselectionindexes%28_%29.md)
  Adds the objects at the specified indexes in the receiver’s content array to the current selection.
- [func removeSelectionIndexes(IndexSet) -> Bool](./removeselectionindexes%28_%29.md)
  Removes the object as the specified indexes from the receiver’s current selection.
- [func setSelectedObjects([Any]) -> Bool](./setselectedobjects%28_%29.md)
  Sets the specified objects as the receiver’s current selection.
- [var selectedObjects: [Any]!](./selectedobjects.md)
  An array containing the receiver’s selected objects
- [func addSelectedObjects([Any]) -> Bool](./addselectedobjects%28_%29.md)
  Adds the specified objects from the receiver’s content array to the current selection.
- [func removeSelectedObjects([Any]) -> Bool](./removeselectedobjects%28_%29.md)
  Removes the specified objects from the receiver’s current selection.
- [func selectNext(Any?)](./selectnext%28_%29.md)
  Selects the next object, relative to the current selection, in the receiver’s arranged content.
- [var canSelectNext: Bool](./canselectnext.md)
  A Boolean value indicating whether the next object, relative to the current selection, in the receiver’s content array can be selected
- [func selectPrevious(Any?)](./selectprevious%28_%29.md)
  Selects the previous object, relative to the current selection, in the receiver’s arranged content.
- [var canSelectPrevious: Bool](./canselectprevious.md)
  A Boolean value indicating whether the previous object, relative to the current selection, in the receiver’s content array can be selected


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/setselectionindex(_:))*