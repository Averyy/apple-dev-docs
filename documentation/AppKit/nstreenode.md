# NSTreeNode

**Framework**: AppKit  
**Kind**: class

A node in a tree of nodes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSTreeNode
```

#### Overview

[`NSTreeNode`](nstreenode.md) simplifies the creation and management of trees of objects. Each tree node represents a model object. A tree node with `nil` as its parent node is considered the root of the tree.

## Topics

### Creating tree nodes
- [init(representedObject: Any?)](nstreenode/init(representedobject:).md)
  Initializes a newly allocated tree node that represents the specified object.
### Getting information about a node
- [var representedObject: Any?](nstreenode/representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](nstreenode/indexpath.md)
  The position of the receiver relative to its root parent.
- [var isLeaf: Bool](nstreenode/isleaf.md)
  A Boolean that indicates whether the receiver is a leaf node.
- [var children: [NSTreeNode]?](nstreenode/children.md)
  An array containing receiver’s child nodes.
- [var mutableChildren: NSMutableArray](nstreenode/mutablechildren.md)
  A mutable array that provides read-write access to the receiver’s child nodes.
- [func descendant(at: IndexPath) -> NSTreeNode?](nstreenode/descendant(at:).md)
  Returns the receiver’s descendant at the specified index path.
- [var parent: NSTreeNode?](nstreenode/parent.md)
  The receiver’s parent node.
### Sorting the subtree
- [func sort(with: [NSSortDescriptor], recursively: Bool)](nstreenode/sort(with:recursively:).md)
  Sorts the receiver’s subtree using the values of the represented objects with the specified sort descriptors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Navigating Hierarchical Data Using Outline and Split Views](navigating-hierarchical-data-using-outline-and-split-views.md)
  Build a structured user interface that simplifies navigation in your app.
- [class NSTreeController](nstreecontroller.md)
  A bindings-compatible controller that manages a tree of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode)*