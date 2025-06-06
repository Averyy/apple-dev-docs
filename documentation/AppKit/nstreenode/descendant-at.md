# descendant(at:)

**Framework**: AppKit  
**Kind**: method

Returns the receiver’s descendant at the specified index path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func descendant(at indexPath: IndexPath) -> NSTreeNode?
```

#### Return Value

A tree node, or `nil` if the node does not exist.

## Parameters

- `indexPath`: An index path specifying a descendant of the receiver.

## See Also

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
- [var parent: NSTreeNode?](nstreenode/parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/descendant(at:))*