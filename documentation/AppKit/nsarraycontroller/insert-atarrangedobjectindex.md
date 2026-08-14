# insert(_:atArrangedObjectIndex:)

**Framework**: AppKit  
**Kind**: method

Inserts `object` into the receiver’s arranged objects array at the location specified by `index`, and adds it to the receiver’s content collection.

**Availability**:
- macOS ?+

## Declaration

```swift
func insert(_ object: Any, atArrangedObjectIndex index: Int)
```

#### Discussion

Subclasses can override this method to provide customized arranged objects support. An error is returned if the given index is outside of the [`arrangedObjects`](nsarraycontroller/arrangedobjects.md) range, or if the given object would not appear in the arrangedObjects. Set the [`clearsFilterPredicateOnInsertion`](nsarraycontroller/clearsfilterpredicateoninsertion.md) to [`true`](https://developer.apple.com/documentation/swift/true) to allow insertion.

## See Also

- [func addObject(Any)](nsarraycontroller/addobject(_:).md)
  Adds `object` to the receiver’s content collection and the arranged objects array.
- [func add(contentsOf: [Any])](nsarraycontroller/add(contentsof:).md)
  Adds `objects` to the receiver’s content collection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/insert(_:atarrangedobjectindex:))*