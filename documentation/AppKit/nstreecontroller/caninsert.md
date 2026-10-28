# canInsert

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if an object can be inserted into the tree controller’s content.

**Availability**:
- macOS

## Declaration

```swift
var canInsert: Bool { get }
```

```objc
@property (readonly) BOOL canInsert;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if an object can be inserted into the tree controller’s content. This property is observable using key-value observing.

## See Also

### Adding, inserting and removing objects
- [func add(Any?)](./add%28_%29.md)
  Adds an object to the tree controller’s content after the current selection.
- [func addChild(Any?)](./addchild%28_%29.md)
  Adds a child object to the currently selected item.
- [var canAddChild: Bool](./canaddchild.md)
  A Boolean value that indicates if a child object can be added to the tree controller’s content.
- [var canInsertChild: Bool](./caninsertchild.md)
  A Boolean value that indicates if a child object can be inserted into the tree controller’s content.
- [func insert(Any?)](./insert%28_%29.md)
  Creates a new object of the class specified by `objectClass` and inserts it into the tree controller’s content.
- [func insertChild(Any?)](./insertchild%28_%29.md)
  Creates a new object of the class specified by `objectClass` and inserts it into the tree controller’s content as a child of the current selection.
- [func insert(Any?, atArrangedObjectIndexPath: IndexPath)](./insert%28_,atarrangedobjectindexpath%29.md)
  Inserts `object` into the tree controller’s arranged objects array at the location specified by `indexPath`, and adds it to the tree controller’s content.
- [func insert([Any], atArrangedObjectIndexPaths: [IndexPath])](./insert%28_,atarrangedobjectindexpaths%29.md)
  Inserts `objects` into the tree controller’s arranged objects array at the locations specified in `indexPaths`, and adds them to the tree controller’s content.
- [func remove(Any?)](./remove%28_%29.md)
  Removes the tree controller’s selected objects from the content.
- [func removeObject(atArrangedObjectIndexPath: IndexPath)](./removeobject%28atarrangedobjectindexpath%29.md)
  Removes the object at the specified `indexPath` in the tree controller’s arranged objects from the tree controller’s content.
- [func removeObjects(atArrangedObjectIndexPaths: [IndexPath])](./removeobjects%28atarrangedobjectindexpaths%29.md)
  Removes the objects at the specified `indexPaths` in the tree controller’s arranged objects from the tree controller’s content.
- [func move(NSTreeNode, to: IndexPath)](./move%28_,to%29-s5xp.md)
  Moves the specified tree node to the new index path.
- [func move([NSTreeNode], to: IndexPath)](./move%28_,to%29-moi9.md)
  Moves the specified tree nodes to the new index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/caninsert)*