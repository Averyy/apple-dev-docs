# isLeaf

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the receiver is a leaf node.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isLeaf: Bool { get }
```

```objc
@property (readonly, getter=isLeaf) BOOL leaf;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver is a leaf node (has no child nodes), otherwise [`false`](../../Swift/false.md).

## See Also

### Getting information about a node
- [var representedObject: Any?](./representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](./indexpath.md)
  The position of the receiver relative to its root parent.
- [var children: [NSTreeNode]?](./children.md)
  An array containing receiver’s child nodes.
- [var mutableChildren: NSMutableArray](./mutablechildren.md)
  A mutable array that provides read-write access to the receiver’s child nodes.
- [func descendant(at: IndexPath) -> NSTreeNode?](./descendant%28at%29.md)
  Returns the receiver’s descendant at the specified index path.
- [var parent: NSTreeNode?](./parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/isleaf)*