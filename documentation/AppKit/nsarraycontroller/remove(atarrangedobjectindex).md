# remove(atArrangedObjectIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the object at the specified `index` in the receiver’s arranged objects from the receiver’s content array.

**Availability**:
- macOS

## Declaration

```swift
func remove(atArrangedObjectIndex index: Int)
```

```objc
- (void) removeObjectAtArrangedObjectIndex:(NSUInteger) index;
```

#### Discussion

See [`removeObject(_:)`](./removeobject%28_%29.md) for a discussion of the semantics of removing objects when using Core Data.

## See Also

### Adding and Removing Objects
- [func addObject(Any)](./addobject%28_%29.md)
  Adds `object` to the receiver’s content collection and the arranged objects array.
- [func add(contentsOf: [Any])](./add%28contentsof%29.md)
  Adds `objects` to the receiver’s content collection.
- [func insert(Any, atArrangedObjectIndex: Int)](./insert%28_,atarrangedobjectindex%29.md)
  Inserts `object` into the receiver’s arranged objects array at the location specified by `index`, and adds it to the receiver’s content collection.
- [func insert(contentsOf: [Any], atArrangedObjectIndexes: IndexSet)](./insert%28contentsof,atarrangedobjectindexes%29.md)
  Inserts `object`s into the receiver’s arranged objects array at the locations specified in `indexes`, and adds it to the receiver’s content collection.
- [func remove(atArrangedObjectIndexes: IndexSet)](./remove%28atarrangedobjectindexes%29.md)
  Removes the objects at the specified `indexes` in the receiver’s arranged objects from the content array.
- [func remove(Any?)](./remove%28_%29.md)
  Removes the receiver’s selected objects from the content collection.
- [func removeObject(Any)](./removeobject%28_%29.md)
  Removes `object` from the receiver’s content collection.
- [func remove(contentsOf: [Any])](./remove%28contentsof%29.md)
  Removes `objects` from the receiver’s content collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/remove(atarrangedobjectindex:))*