# add(contentsOf:)

**Framework**: AppKit  
**Kind**: method

Adds `objects` to the receiver’s content collection.

**Availability**:
- macOS ?+

## Declaration

```swift
func add(contentsOf objects: [Any])
```

#### Discussion

If [`selectsInsertedObjects`](nsarraycontroller/selectsinsertedobjects.md) is [`true`](https://developer.apple.com/documentation/swift/true) (the default), the added objects are selected in the array controller.

It is important to note that inserting many objects with [`selectsInsertedObjects`](nsarraycontroller/selectsinsertedobjects.md) on can cause a significant performance penalty. In this case it is more efficient to use the [`content`](nsobjectcontroller/content.md) method to set the array, or to set [`selectsInsertedObjects`](nsarraycontroller/selectsinsertedobjects.md) to [`false`](https://developer.apple.com/documentation/swift/false) before adding the objects with [`add(contentsOf:)`](nsarraycontroller/add(contentsof:).md).

## See Also

- [func addObject(Any)](nsarraycontroller/addobject(_:).md)
  Adds `object` to the receiver’s content collection and the arranged objects array.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/add(contentsof:))*