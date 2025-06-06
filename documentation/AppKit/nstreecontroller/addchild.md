# addChild(_:)

**Framework**: AppKit  
**Kind**: method

Adds a child object to the currently selected item.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func addChild(_ sender: Any?)
```

#### Discussion

The `sender` is typically the object that invoked this method.

If the receiver is in object mode `newObject` is called and the returned object is added as a child. If the receiver is in entity mode a new object is created that is appropriate for the relationship as specified by the entity, and `newObject` is not used.

##### Special Considerations

The result of this method is deferred until the next iteration of the run loop so that the error presentation mechanism can provide feedback as a sheet.

## See Also

- [func add(Any?)](nstreecontroller/add(_:).md)
  Adds an object to the tree controller’s content after the current selection.
- [var canAddChild: Bool](nstreecontroller/canaddchild.md)
  A Boolean value that indicates if a child object can be added to the tree controller’s content.
- [var canInsert: Bool](nstreecontroller/caninsert.md)
  A Boolean value that indicates if an object can be inserted into the tree controller’s content.
- [var canInsertChild: Bool](nstreecontroller/caninsertchild.md)
  A Boolean value that indicates if a child object can be inserted into the tree controller’s content.
- [func insert(Any?)](nstreecontroller/insert(_:).md)
  Creates a new object of the class specified by `objectClass` and inserts it into the tree controller’s content.
- [func insertChild(Any?)](nstreecontroller/insertchild(_:).md)
  Creates a new object of the class specified by `objectClass` and inserts it into the tree controller’s content as a child of the current selection.
- [func insert(Any?, atArrangedObjectIndexPath: IndexPath)](nstreecontroller/insert(_:atarrangedobjectindexpath:).md)
  Inserts `object` into the tree controller’s arranged objects array at the location specified by `indexPath`, and adds it to the tree controller’s content.
- [func insert([Any], atArrangedObjectIndexPaths: [IndexPath])](nstreecontroller/insert(_:atarrangedobjectindexpaths:).md)
  Inserts `objects` into the tree controller’s arranged objects array at the locations specified in `indexPaths`, and adds them to the tree controller’s content.
- [func remove(Any?)](nstreecontroller/remove(_:).md)
  Removes the tree controller’s selected objects from the content.
- [func removeObject(atArrangedObjectIndexPath: IndexPath)](nstreecontroller/removeobject(atarrangedobjectindexpath:).md)
  Removes the object at the specified `indexPath` in the tree controller’s arranged objects from the tree controller’s content.
- [func removeObjects(atArrangedObjectIndexPaths: [IndexPath])](nstreecontroller/removeobjects(atarrangedobjectindexpaths:).md)
  Removes the objects at the specified `indexPaths` in the tree controller’s arranged objects from the tree controller’s content.
- [func move(NSTreeNode, to: IndexPath)](nstreecontroller/move(_:to:)-s5xp.md)
  Moves the specified tree node to the new index path.
- [func move([NSTreeNode], to: IndexPath)](nstreecontroller/move(_:to:)-moi9.md)
  Moves the specified tree nodes to the new index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/addchild(_:))*