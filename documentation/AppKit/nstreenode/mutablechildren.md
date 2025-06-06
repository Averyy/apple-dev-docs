# mutableChildren

**Framework**: AppKit  
**Kind**: property

A mutable array that provides read-write access to the receiver’s child nodes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var mutableChildren: NSMutableArray { get }
```

#### Discussion

Nodes that are inserted into this array have their parent nodes set to the receiver. Nodes that are removed from this array automatically have their parent node set to `nil`. The array that is returned is observable using key-value observing.

## See Also

- [var representedObject: Any?](nstreenode/representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](nstreenode/indexpath.md)
  The position of the receiver relative to its root parent.
- [var isLeaf: Bool](nstreenode/isleaf.md)
  A Boolean that indicates whether the receiver is a leaf node.
- [var children: [NSTreeNode]?](nstreenode/children.md)
  An array containing receiver’s child nodes.
- [func descendant(at: IndexPath) -> NSTreeNode?](nstreenode/descendant(at:).md)
  Returns the receiver’s descendant at the specified index path.
- [var parent: NSTreeNode?](nstreenode/parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/mutablechildren)*