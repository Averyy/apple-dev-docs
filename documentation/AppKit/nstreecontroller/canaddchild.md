# canAddChild

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if a child object can be added to the tree controller’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
var canAddChild: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if a child object can be added to the tree controller’s content. This property is observable using key-value observing.

## See Also

- [func add(Any?)](nstreecontroller/add(_:).md)
  Adds an object to the tree controller’s content after the current selection.
- [func addChild(Any?)](nstreecontroller/addchild(_:).md)
  Adds a child object to the currently selected item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/canaddchild)*