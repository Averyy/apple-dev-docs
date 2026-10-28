# descendant(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s descendant at the specified index path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func descendant(at indexPath: IndexPath) -> NSTreeNode?
```

```objc
- (NSTreeNode *) descendantNodeAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

A tree node, or `nil` if the node does not exist.

## Parameters

- `indexPath`: An index path specifying a descendant of the receiver.

## See Also

### Getting information about a node
- [var representedObject: Any?](./representedobject.md)
  The object the tree node represents.
- [var indexPath: IndexPath](./indexpath.md)
  The position of the receiver relative to its root parent.
- [var isLeaf: Bool](./isleaf.md)
  A Boolean that indicates whether the receiver is a leaf node.
- [var children: [NSTreeNode]?](./children.md)
  An array containing receiver’s child nodes.
- [var mutableChildren: NSMutableArray](./mutablechildren.md)
  A mutable array that provides read-write access to the receiver’s child nodes.
- [var parent: NSTreeNode?](./parent.md)
  The receiver’s parent node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreenode/descendant(at:))*