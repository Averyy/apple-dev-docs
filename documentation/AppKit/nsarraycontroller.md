# NSArrayController

**Framework**: AppKit  
**Kind**: class

A bindings-compatible controller that manages a collection of objects.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSArrayController
```

#### Overview

Typically the collection that an [`NSArrayController`](nsarraycontroller.md) manages is an array, however, if the controller manages a relationship of a managed object (see [`NSManagedObject`](https://developer.apple.com/documentation/CoreData/NSManagedObject)) the collection may be a set. [`NSArrayController`](nsarraycontroller.md) provides selection management and sorting capabilities.

## Topics

### Managing Sort Descriptors
- [var sortDescriptors: [NSSortDescriptor]](nsarraycontroller/sortdescriptors.md)
  An array of [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) objects, used by the receiver to arrange its content.
### Arranging Objects
- [func arrange([Any]) -> [Any]](nsarraycontroller/arrange(_:).md)
  Returns a given array, appropriately sorted and filtered.
- [var arrangedObjects: Any](nsarraycontroller/arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](nsarraycontroller/arrange(_:).md).
- [func rearrangeObjects()](nsarraycontroller/rearrangeobjects.md)
  Triggers filtering of the receiver’s content.
### Managing Content
- [func add(Any?)](nsarraycontroller/add(_:).md)
  Creates and adds a new object to the receiver’s content and arranged objects.
### Selection Attributes
- [var avoidsEmptySelection: Bool](nsarraycontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection
- [var preservesSelection: Bool](nsarraycontroller/preservesselection.md)
  A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes
- [var alwaysUsesMultipleValuesMarker: Bool](nsarraycontroller/alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected
### Managing selections
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
- [var selectedObjects: [Any]!](nsarraycontroller/selectedobjects.md)
  An array containing the receiver’s selected objects
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
### Inserting
- [var canInsert: Bool](nsarraycontroller/caninsert.md)
  Returns a Boolean value that indicates whether an object can be inserted into the receiver’s content collection.
- [func insert(Any?)](nsarraycontroller/insert(_:).md)
  Creates a new object and inserts it into the receiver’s content array.
### Adding and Removing Objects
- [func addObject(Any)](nsarraycontroller/addobject(_:).md)
  Adds `object` to the receiver’s content collection and the arranged objects array.
- [func add(contentsOf: [Any])](nsarraycontroller/add(contentsof:).md)
  Adds `objects` to the receiver’s content collection.
- [func insert(Any, atArrangedObjectIndex: Int)](nsarraycontroller/insert(_:atarrangedobjectindex:).md)
  Inserts `object` into the receiver’s arranged objects array at the location specified by `index`, and adds it to the receiver’s content collection.
- [func insert(contentsOf: [Any], atArrangedObjectIndexes: IndexSet)](nsarraycontroller/insert(contentsof:atarrangedobjectindexes:).md)
  Inserts `object`s into the receiver’s arranged objects array at the locations specified in `indexes`, and adds it to the receiver’s content collection.
- [func remove(atArrangedObjectIndex: Int)](nsarraycontroller/remove(atarrangedobjectindex:).md)
  Removes the object at the specified `index` in the receiver’s arranged objects from the receiver’s content array.
- [func remove(atArrangedObjectIndexes: IndexSet)](nsarraycontroller/remove(atarrangedobjectindexes:).md)
  Removes the objects at the specified `indexes` in the receiver’s arranged objects from the content array.
- [func remove(Any?)](nsarraycontroller/remove(_:).md)
  Removes the receiver’s selected objects from the content collection.
- [func removeObject(Any)](nsarraycontroller/removeobject(_:).md)
  Removes `object` from the receiver’s content collection.
- [func remove(contentsOf: [Any])](nsarraycontroller/remove(contentsof:).md)
  Removes `objects` from the receiver’s content collection.
### Filtering Content
- [var clearsFilterPredicateOnInsertion: Bool](nsarraycontroller/clearsfilterpredicateoninsertion.md)
  A Boolean value that indicates whether the receiver automatically clears an existing filter predicate when new items are inserted or added to the content
- [var filterPredicate: NSPredicate?](nsarraycontroller/filterpredicate.md)
  A predicate used by the receiver to filter the array controller contents
### Automatic Content Rearranging
- [var automaticallyRearrangesObjects: Bool](nsarraycontroller/automaticallyrearrangesobjects.md)
  A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates
- [var automaticRearrangementKeyPaths: [String]?](nsarraycontroller/automaticrearrangementkeypaths.md)
  An array of key paths that trigger automatic content sorting or filtering
- [func didChangeArrangementCriteria()](nsarraycontroller/didchangearrangementcriteria.md)
  Invoked when any criteria for arranging objects change.

## Relationships

### Inherits From
- [NSObjectController](nsobjectcontroller.md)
### Inherited By
- [NSDictionaryController](nsdictionarycontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSEditorRegistration](nseditorregistration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller)*