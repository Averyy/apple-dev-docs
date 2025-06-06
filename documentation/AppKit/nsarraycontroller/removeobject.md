# removeObject(_:)

**Framework**: AppKit  
**Kind**: method

Removes `object` from the receiver’s content collection.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeObject(_ object: Any)
```

#### Discussion

If you are using Core Data, the exact semantics of this method differ depending on the settings for the array controller. If the receiver’s content is fetched automatically, removed objects are marked for deletion by the managed object context (and hence removal from the object graph). If, however, the receiver’s `contentSet` is bound to a relationship, `removeObject:` by default only removes the object from the relationship (not from the object graph). You can, though, set the “Deletes Object on Remove” option for the `contentSet` binding, in which case objects are marked for deletion as well as being removed from the relationship.

## See Also

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
- [func remove(contentsOf: [Any])](nsarraycontroller/remove(contentsof:).md)
  Removes `objects` from the receiver’s content collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/removeobject(_:))*