# children

**Framework**: AppKit  
**Kind**: property

An array containing receiver’s child nodes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var children: [NSTreeNode]? { get }
```

## See Also

- [var representedObject: Any?](nstreenode/representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](nstreenode/indexpath.md)
  The position of the receiver relative to its root parent.
- [var isLeaf: Bool](nstreenode/isleaf.md)
  A Boolean that indicates whether the receiver is a leaf node.
- [var mutableChildren: NSMutableArray](nstreenode/mutablechildren.md)
  A mutable array that provides read-write access to the receiver’s child nodes.
- [func descendant(at: IndexPath) -> NSTreeNode?](nstreenode/descendant(at:).md)
  Returns the receiver’s descendant at the specified index path.
- [var parent: NSTreeNode?](nstreenode/parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/children)*