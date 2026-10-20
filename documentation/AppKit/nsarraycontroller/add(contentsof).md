# add(contentsOf:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds `objects` to the receiver’s content collection.

**Availability**:
- macOS

## Declaration

```swift
func add(contentsOf objects: [Any])
```

```objc
- (void) addObjects:(NSArray *) objects;
```

#### Discussion

If [`selectsInsertedObjects`](./selectsinsertedobjects.md) is [`true`](../../Swift/true.md) (the default), the added objects are selected in the array controller.

It is important to note that inserting many objects with [`selectsInsertedObjects`](./selectsinsertedobjects.md) on can cause a significant performance penalty. In this case it is more efficient to use the [`content`](../nsobjectcontroller/content.md) method to set the array, or to set [`selectsInsertedObjects`](./selectsinsertedobjects.md) to [`false`](../../Swift/false.md) before adding the objects with [`add(contentsOf:)`](./add%28contentsof%29.md).

## See Also

### Adding and Removing Objects
- [func addObject(Any)](./addobject%28_%29.md)
  Adds `object` to the receiver’s content collection and the arranged objects array.
- [func insert(Any, atArrangedObjectIndex: Int)](./insert%28_,atarrangedobjectindex%29.md)
  Inserts `object` into the receiver’s arranged objects array at the location specified by `index`, and adds it to the receiver’s content collection.
- [func insert(contentsOf: [Any], atArrangedObjectIndexes: IndexSet)](./insert%28contentsof,atarrangedobjectindexes%29.md)
  Inserts `object`s into the receiver’s arranged objects array at the locations specified in `indexes`, and adds it to the receiver’s content collection.
- [func remove(atArrangedObjectIndex: Int)](./remove%28atarrangedobjectindex%29.md)
  Removes the object at the specified `index` in the receiver’s arranged objects from the receiver’s content array.
- [func remove(atArrangedObjectIndexes: IndexSet)](./remove%28atarrangedobjectindexes%29.md)
  Removes the objects at the specified `indexes` in the receiver’s arranged objects from the content array.
- [func remove(Any?)](./remove%28_%29.md)
  Removes the receiver’s selected objects from the content collection.
- [func removeObject(Any)](./removeobject%28_%29.md)
  Removes `object` from the receiver’s content collection.
- [func remove(contentsOf: [Any])](./remove%28contentsof%29.md)
  Removes `objects` from the receiver’s content collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/add(contentsof:))*