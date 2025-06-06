# remove(_:)

**Framework**: AppKit  
**Kind**: method

Removes the receiver’s selected objects from the content collection.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func remove(_ sender: Any?)
```

#### Discussion

See [`removeObject(_:)`](nsarraycontroller/removeobject(_:).md) for a discussion of the semantics of removing objects when using Core Data.

##### Special Considerations

Beginning with OS X v10.4 the result of this method is deferred until the next iteration of the runloop so that the error presentation mechanism (see [`Error Responders and Error Recovery`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorRespondRecover/ErrorRespondRecover.html#//apple_ref/doc/uid/TP40001806-CH203)) can provide feedback as a sheet.

## Parameters

- `sender`: Typically the object that invoked this method.

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
- [func removeObject(Any)](nsarraycontroller/removeobject(_:).md)
  Removes `object` from the receiver’s content collection.
- [func remove(contentsOf: [Any])](nsarraycontroller/remove(contentsof:).md)
  Removes `objects` from the receiver’s content collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/remove(_:))*