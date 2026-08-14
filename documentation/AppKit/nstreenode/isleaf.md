# isLeaf

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the receiver is a leaf node.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isLeaf: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is a leaf node (has no child nodes), otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var representedObject: Any?](nstreenode/representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](nstreenode/indexpath.md)
  The position of the receiver relative to its root parent.
- [var children: [NSTreeNode]?](nstreenode/children.md)
  An array containing receiver’s child nodes.
- [var mutableChildren: NSMutableArray](nstreenode/mutablechildren.md)
  A mutable array that provides read-write access to the receiver’s child nodes.
- [func descendant(at: IndexPath) -> NSTreeNode?](nstreenode/descendant(at:).md)
  Returns the receiver’s descendant at the specified index path.
- [var parent: NSTreeNode?](nstreenode/parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/isleaf)*