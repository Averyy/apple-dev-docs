# selectedObjects

**Framework**: AppKit  
**Kind**: property

An array containing the receiver’s selected objects

**Availability**:
- macOS ?+

## Declaration

```swift
var selectedObjects: [Any]! { get }
```

#### Discussion

This property is observable using key-value observing.

## See Also

- [var selectionIndex: Int](nsarraycontroller/selectionindex.md)
  The index of the first object in the receiver’s selection
- [func setSelectionIndex(Int) -> Bool](nsarraycontroller/setselectionindex(_:).md)
  Sets the receiver’s selection to the given index, and returns a Boolean value that indicates whether the selection was changed.
- [var selectsInsertedObjects: Bool](nsarraycontroller/selectsinsertedobjects.md)
  A Boolean value that indicates whether the receiver automatically selects inserted objects
- [func setSelectionIndexes(IndexSet) -> Bool](nsarraycontroller/setselectionindexes(_:).md)
  Sets the receiver’s selection indexes and returns a Boolean value that indicates whether the selection changed.
- [var selectionIndexes: IndexSet](nsarraycontroller/selectionindexes.md)
  An index set containing the indexes of the receiver’s currently selected objects in the content array
- [func addSelectionIndexes(IndexSet) -> Bool](nsarraycontroller/addselectionindexes(_:).md)
  Adds the objects at the specified indexes in the receiver’s content array to the current selection, returning [`true`](https://developer.apple.com/documentation/swift/true) if the selection was changed.
- [func removeSelectionIndexes(IndexSet) -> Bool](nsarraycontroller/removeselectionindexes(_:).md)
  Removes the object as the specified `indexes` from the receiver’s current selection, returning [`true`](https://developer.apple.com/documentation/swift/true) if the selection was changed.
- [func setSelectedObjects([Any]) -> Bool](nsarraycontroller/setselectedobjects(_:).md)
  Sets `objects` as the receiver’s current selection, returning [`true`](https://developer.apple.com/documentation/swift/true) if the selection was changed.
- [func addSelectedObjects([Any]) -> Bool](nsarraycontroller/addselectedobjects(_:).md)
  Adds `objects` from the receiver’s content array to the current selection, returning [`true`](https://developer.apple.com/documentation/swift/true) if the selection was changed.
- [func removeSelectedObjects([Any]) -> Bool](nsarraycontroller/removeselectedobjects(_:).md)
  Removes `objects` from the receiver’s current selection, returning [`true`](https://developer.apple.com/documentation/swift/true) if the selection was changed.
- [func selectNext(Any?)](nsarraycontroller/selectnext(_:).md)
  Selects the next object, relative to the current selection, in the receiver’s arranged content.
- [var canSelectNext: Bool](nsarraycontroller/canselectnext.md)
  A Boolean value indicating whether the next object, relative to the current selection, in the receiver’s content array can be selected
- [func selectPrevious(Any?)](nsarraycontroller/selectprevious(_:).md)
  Selects the previous object, relative to the current selection, in the receiver’s arranged content.
- [var canSelectPrevious: Bool](nsarraycontroller/canselectprevious.md)
  A Boolean value indicating whether the previous object, relative to the current selection, in the receiver’s content array can be selected


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/selectedobjects)*