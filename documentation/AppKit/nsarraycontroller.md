# NSArrayController

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A bindings-compatible controller that manages a collection of objects.

**Availability**:
- macOS

## Declaration

```swift
class NSArrayController
```

```objc
@interface NSArrayController : NSObjectController
```

## Overview

Typically the collection that an [`NSArrayController`](./nsarraycontroller.md) manages is an array, however, if the controller manages a relationship of a managed object (see [`NSManagedObject`](../CoreData/nsmanagedobject.md)) the collection may be a set. [`NSArrayController`](./nsarraycontroller.md) provides selection management and sorting capabilities.

## Topics

### Managing Sort Descriptors
- [var sortDescriptors: [NSSortDescriptor]](./nsarraycontroller/sortdescriptors.md)
  An array of sort descriptor objects, used by the receiver to arrange its content.
### Arranging Objects
- [func arrange([Any]) -> [Any]](./nsarraycontroller/arrange%28_%29.md)
  Returns a given array, appropriately sorted and filtered.
- [var arrangedObjects: Any](./nsarraycontroller/arrangedobjects.md)
  An array containing the receiver’s content objects arranged using [`arrange(_:)`](./nsarraycontroller/arrange%28_%29.md).
- [func rearrangeObjects()](./nsarraycontroller/rearrangeobjects%28%29.md)
  Triggers filtering of the receiver’s content.
### Managing Content
- [func add(Any?)](./nsarraycontroller/add%28_%29.md)
  Creates and adds a new object to the receiver’s content and arranged objects.
### Selection Attributes
- [var avoidsEmptySelection: Bool](./nsarraycontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the receiver requires that the content array attempt to maintain a selection
- [var preservesSelection: Bool](./nsarraycontroller/preservesselection.md)
  A Boolean value that indicates whether the receiver will attempt to preserve the current selection when the content changes
- [var alwaysUsesMultipleValuesMarker: Bool](./nsarraycontroller/alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the receiver always returns the multiple values marker when multiple objects are selected
### Managing selections
- [var selectionIndex: Int](./nsarraycontroller/selectionindex.md)
  The index of the first object in the receiver’s selection
- [func setSelectionIndex(Int) -> Bool](./nsarraycontroller/setselectionindex%28_%29.md)
  Sets the receiver’s selection to the given index, and returns a Boolean value that indicates whether the selection was changed.
- [var selectsInsertedObjects: Bool](./nsarraycontroller/selectsinsertedobjects.md)
  A Boolean value that indicates whether the receiver automatically selects inserted objects
- [func setSelectionIndexes(IndexSet) -> Bool](./nsarraycontroller/setselectionindexes%28_%29.md)
  Sets the receiver’s selection indexes and returns a Boolean value that indicates whether the selection changed.
- [var selectionIndexes: IndexSet](./nsarraycontroller/selectionindexes.md)
  An index set containing the indexes of the receiver’s currently selected objects in the content array
- [func addSelectionIndexes(IndexSet) -> Bool](./nsarraycontroller/addselectionindexes%28_%29.md)
  Adds the objects at the specified indexes in the receiver’s content array to the current selection.
- [func removeSelectionIndexes(IndexSet) -> Bool](./nsarraycontroller/removeselectionindexes%28_%29.md)
  Removes the object as the specified indexes from the receiver’s current selection.
- [func setSelectedObjects([Any]) -> Bool](./nsarraycontroller/setselectedobjects%28_%29.md)
  Sets the specified objects as the receiver’s current selection.
- [var selectedObjects: [Any]!](./nsarraycontroller/selectedobjects.md)
  An array containing the receiver’s selected objects
- [func addSelectedObjects([Any]) -> Bool](./nsarraycontroller/addselectedobjects%28_%29.md)
  Adds the specified objects from the receiver’s content array to the current selection.
- [func removeSelectedObjects([Any]) -> Bool](./nsarraycontroller/removeselectedobjects%28_%29.md)
  Removes the specified objects from the receiver’s current selection.
- [func selectNext(Any?)](./nsarraycontroller/selectnext%28_%29.md)
  Selects the next object, relative to the current selection, in the receiver’s arranged content.
- [var canSelectNext: Bool](./nsarraycontroller/canselectnext.md)
  A Boolean value indicating whether the next object, relative to the current selection, in the receiver’s content array can be selected
- [func selectPrevious(Any?)](./nsarraycontroller/selectprevious%28_%29.md)
  Selects the previous object, relative to the current selection, in the receiver’s arranged content.
- [var canSelectPrevious: Bool](./nsarraycontroller/canselectprevious.md)
  A Boolean value indicating whether the previous object, relative to the current selection, in the receiver’s content array can be selected
### Inserting
- [var canInsert: Bool](./nsarraycontroller/caninsert.md)
  Returns a Boolean value that indicates whether an object can be inserted into the receiver’s content collection.
- [func insert(Any?)](./nsarraycontroller/insert%28_%29.md)
  Creates a new object and inserts it into the receiver’s content array.
### Adding and Removing Objects
- [func addObject(Any)](./nsarraycontroller/addobject%28_%29.md)
  Adds `object` to the receiver’s content collection and the arranged objects array.
- [func add(contentsOf: [Any])](./nsarraycontroller/add%28contentsof%29.md)
  Adds `objects` to the receiver’s content collection.
- [func insert(Any, atArrangedObjectIndex: Int)](./nsarraycontroller/insert%28_,atarrangedobjectindex%29.md)
  Inserts `object` into the receiver’s arranged objects array at the location specified by `index`, and adds it to the receiver’s content collection.
- [func insert(contentsOf: [Any], atArrangedObjectIndexes: IndexSet)](./nsarraycontroller/insert%28contentsof,atarrangedobjectindexes%29.md)
  Inserts `object`s into the receiver’s arranged objects array at the locations specified in `indexes`, and adds it to the receiver’s content collection.
- [func remove(atArrangedObjectIndex: Int)](./nsarraycontroller/remove%28atarrangedobjectindex%29.md)
  Removes the object at the specified `index` in the receiver’s arranged objects from the receiver’s content array.
- [func remove(atArrangedObjectIndexes: IndexSet)](./nsarraycontroller/remove%28atarrangedobjectindexes%29.md)
  Removes the objects at the specified `indexes` in the receiver’s arranged objects from the content array.
- [func remove(Any?)](./nsarraycontroller/remove%28_%29.md)
  Removes the receiver’s selected objects from the content collection.
- [func removeObject(Any)](./nsarraycontroller/removeobject%28_%29.md)
  Removes `object` from the receiver’s content collection.
- [func remove(contentsOf: [Any])](./nsarraycontroller/remove%28contentsof%29.md)
  Removes `objects` from the receiver’s content collection.
### Filtering Content
- [var clearsFilterPredicateOnInsertion: Bool](./nsarraycontroller/clearsfilterpredicateoninsertion.md)
  A Boolean value that indicates whether the receiver automatically clears an existing filter predicate when new items are inserted or added to the content
- [var filterPredicate: NSPredicate?](./nsarraycontroller/filterpredicate.md)
  A predicate used by the receiver to filter the array controller contents
### Automatic Content Rearranging
- [var automaticallyRearrangesObjects: Bool](./nsarraycontroller/automaticallyrearrangesobjects.md)
  A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates
- [var automaticRearrangementKeyPaths: [String]?](./nsarraycontroller/automaticrearrangementkeypaths.md)
  An array of key paths that trigger automatic content sorting or filtering
- [func didChangeArrangementCriteria()](./nsarraycontroller/didchangearrangementcriteria%28%29.md)
  Invoked when any criteria for arranging objects change.

## Relationships

### Inherits From
- [NSObjectController](./nsobjectcontroller.md)
### Inherited By
- [NSDictionaryController](./nsdictionarycontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](./nseditor.md)
- [NSEditorRegistration](./nseditorregistration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller)*