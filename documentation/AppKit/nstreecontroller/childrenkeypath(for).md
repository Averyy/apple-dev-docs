# childrenKeyPath(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the key path used to find the children in the specified tree node.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func childrenKeyPath(for node: NSTreeNode) -> String?
```

```objc
- (NSString *) childrenKeyPathForNode:(NSTreeNode *) node;
```

#### Return Value

A string containing the key path in `node` that provides the child nodes.

## Parameters

- `node`: A tree node in the tree controller’s content.

## See Also

### Specifying model attributes
- [var childrenKeyPath: String?](./childrenkeypath.md)
  The key path used to find the children in the tree controller’s objects.
- [var countKeyPath: String?](./countkeypath.md)
  The key path used to find the number of children for a node.
- [func countKeyPath(for: NSTreeNode) -> String?](./countkeypath%28for%29.md)
  Returns the key path that provides the number of children for a specified node.
- [var leafKeyPath: String?](./leafkeypath.md)
  The key path used by the tree controller to determine if a node is a leaf key.
- [func leafKeyPath(for: NSTreeNode) -> String?](./leafkeypath%28for%29.md)
  Returns the key path that specifies whether the node is a leaf node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/childrenkeypath(for:))*