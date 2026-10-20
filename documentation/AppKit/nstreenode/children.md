# children

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing receiver’s child nodes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var children: [NSTreeNode]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSTreeNode *> * childNodes;
```

## See Also

### Getting information about a node
- [var representedObject: Any?](./representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](./indexpath.md)
  The position of the receiver relative to its root parent.
- [var isLeaf: Bool](./isleaf.md)
  A Boolean that indicates whether the receiver is a leaf node.
- [var mutableChildren: NSMutableArray](./mutablechildren.md)
  A mutable array that provides read-write access to the receiver’s child nodes.
- [func descendant(at: IndexPath) -> NSTreeNode?](./descendant%28at%29.md)
  Returns the receiver’s descendant at the specified index path.
- [var parent: NSTreeNode?](./parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/children)*