# NSTreeController

**Framework**: AppKit  
**Kind**: class

A bindings-compatible controller that manages a tree of objects.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSTreeController
```

#### Overview

The [`NSTreeController`](nstreecontroller.md) class provides selection and sort management. Its primary purpose is to act as the controller when binding [`NSOutlineView`](nsoutlineview.md) and [`NSBrowser`](nsbrowser.md) instances to a hierarchical collection of objects. The root content object of the tree can be a single object, or an array of objects.

An [`NSTreeController`](nstreecontroller.md) object requires that you describe how the tree of objects is traversed by specifying the key-path for child objects specified by [`childrenKeyPath`](nstreecontroller/childrenkeypath.md). All child objects for the tree must be key-value coding compliant for the same child key path. If necessary, you should add properties to your model classes that map the child key name to the appropriate class-specific property name.

Child objects can implement a count method (specified to the tree controller using [`countKeyPath`](nstreecontroller/countkeypath.md)) that, if provided, returns the number of child objects available. Your model objects are expected to update the value of the count key path in a key-value observing compliant method. Optionally, you can also provide a leaf key path using [`leafKeyPath`](nstreecontroller/leafkeypath.md) that specifies a key in your model object that returns [`true`](https://developer.apple.com/documentation/Swift/true) if the object is a leaf node, and [`false`](https://developer.apple.com/documentation/Swift/false) if it is not. Changes to the leaf node value of the child object should be made in a key-value observing compliant manner. Providing the leaf node key path can improve performance, because it prevents the [`NSTreeController`](nstreecontroller.md) from having to examine the child object to determine if it is a leaf node.

For more information about using NSTreeController in your app, see [`Navigating Hierarchical Data Using Outline and Split Views`](navigating-hierarchical-data-using-outline-and-split-views.md).

## Topics

### Managing Sort Descriptors
- [var sortDescriptors: [NSSortDescriptor]](nstreecontroller/sortdescriptors.md)
  An array containing the sort descriptors used to arrange the tree controller’s content.
### Setting the content
- [var content: Any?](nstreecontroller/content.md)
  The tree controller’s content object.
### Arranging Objects
- [var arrangedObjects: NSTreeNode](nstreecontroller/arrangedobjects.md)
  The tree controller’s sorted content objects.
- [func rearrangeObjects()](nstreecontroller/rearrangeobjects.md)
  Use this method to trigger reordering of the tree controller’s content.
### Getting the current selection
- [func setSelectionIndexPath(IndexPath?) -> Bool](nstreecontroller/setselectionindexpath(_:).md)
  Sets the tree controller’s current selection.
- [var selectionIndexPath: IndexPath?](nstreecontroller/selectionindexpath.md)
  The index path of the first selected object.
- [func setSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/setselectionindexpaths(_:).md)
  Sets the tree controller’s current selection to the specified index paths.
- [var selectionIndexPaths: [IndexPath]](nstreecontroller/selectionindexpaths.md)
  An array containing the index paths of the currently selected objects.
- [var selectedObjects: [Any]](nstreecontroller/selectedobjects.md)
  An array containing the currently selected objects in the tree controller’s content.
- [var selectedNodes: [NSTreeNode]](nstreecontroller/selectednodes.md)
  An array containing the tree controller’s selected tree nodes.
### Managing Selections
- [var selectsInsertedObjects: Bool](nstreecontroller/selectsinsertedobjects.md)
  A Boolean value that indicates whether the tree controller automatically selects objects as they are inserted.
- [func addSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/addselectionindexpaths(_:).md)
  Adds the objects at the specified `indexPaths` in the tree controller’s content to the current selection.
- [func removeSelectionIndexPaths([IndexPath]) -> Bool](nstreecontroller/removeselectionindexpaths(_:).md)
  Removes the objects at the specified index paths from the tree controller’s current selection.
- [var avoidsEmptySelection: Bool](nstreecontroller/avoidsemptyselection.md)
  A Boolean value that indicates whether the tree controller requires the content array to attempt to maintain a selection at all times, avoiding an empty selection.
- [var preservesSelection: Bool](nstreecontroller/preservesselection.md)
  A Boolean value that indicates whether the tree controller will attempt to preserve the current selection when the content changes.
- [var alwaysUsesMultipleValuesMarker: Bool](nstreecontroller/alwaysusesmultiplevaluesmarker.md)
  A Boolean value that indicates whether the tree controller always returns the multiple values marker when multiple objects are selected, even if the selected items have the same value.
### Adding, inserting and removing objects
- [func add(Any?)](nstreecontroller/add(_:).md)
  Adds an object to the tree controller’s content after the current selection.
- [func addChild(Any?)](nstreecontroller/addchild(_:).md)
  Adds a child object to the currently selected item.
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
### Specifying model attributes
- [var childrenKeyPath: String?](nstreecontroller/childrenkeypath.md)
  The key path used to find the children in the tree controller’s objects.
- [func childrenKeyPath(for: NSTreeNode) -> String?](nstreecontroller/childrenkeypath(for:).md)
  Returns the key path used to find the children in the specified tree node.
- [var countKeyPath: String?](nstreecontroller/countkeypath.md)
  The key path used to find the number of children for a node.
- [func countKeyPath(for: NSTreeNode) -> String?](nstreecontroller/countkeypath(for:).md)
  Returns the key path that provides the number of children for a specified node.
- [var leafKeyPath: String?](nstreecontroller/leafkeypath.md)
  The key path used by the tree controller to determine if a node is a leaf key.
- [func leafKeyPath(for: NSTreeNode) -> String?](nstreecontroller/leafkeypath(for:).md)
  Returns the key path that specifies whether the node is a leaf node.

## Relationships

### Inherits From
- [NSObjectController](nsobjectcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSEditorRegistration](nseditorregistration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Navigating Hierarchical Data Using Outline and Split Views](navigating-hierarchical-data-using-outline-and-split-views.md)
  Build a structured user interface that simplifies navigation in your app.
- [class NSTreeNode](nstreenode.md)
  A node in a tree of nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller)*