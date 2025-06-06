# representedObject

**Framework**: AppKit  
**Kind**: property

The object the tree node represents.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var representedObject: Any? { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/representedobject)*