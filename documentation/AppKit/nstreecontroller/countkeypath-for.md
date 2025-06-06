# countKeyPath(for:)

**Framework**: AppKit  
**Kind**: method

Returns the key path that provides the number of children for a specified node.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func countKeyPath(for node: NSTreeNode) -> String?
```

#### Return Value

A string containing the key path in `node` that provides the number of children.

## Parameters

- `node`: A tree node in the tree controller’s content.

## See Also

- [var childrenKeyPath: String?](nstreecontroller/childrenkeypath.md)
  The key path used to find the children in the tree controller’s objects.
- [func childrenKeyPath(for: NSTreeNode) -> String?](nstreecontroller/childrenkeypath(for:).md)
  Returns the key path used to find the children in the specified tree node.
- [var countKeyPath: String?](nstreecontroller/countkeypath.md)
  The key path used to find the number of children for a node.
- [var leafKeyPath: String?](nstreecontroller/leafkeypath.md)
  The key path used by the tree controller to determine if a node is a leaf key.
- [func leafKeyPath(for: NSTreeNode) -> String?](nstreecontroller/leafkeypath(for:).md)
  Returns the key path that specifies whether the node is a leaf node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/countkeypath(for:))*