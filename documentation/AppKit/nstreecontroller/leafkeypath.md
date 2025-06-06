# leafKeyPath

**Framework**: AppKit  
**Kind**: property

The key path used by the tree controller to determine if a node is a leaf key.

**Availability**:
- macOS ?+

## Declaration

```swift
var leafKeyPath: String? { get set }
```

#### Discussion

Specifying a key path for this property is optional. If the tree controller is able to determine that a node is a leaf node, it can disable inserting or adding children to those nodes.

## See Also

- [var childrenKeyPath: String?](nstreecontroller/childrenkeypath.md)
  The key path used to find the children in the tree controller’s objects.
- [func childrenKeyPath(for: NSTreeNode) -> String?](nstreecontroller/childrenkeypath(for:).md)
  Returns the key path used to find the children in the specified tree node.
- [var countKeyPath: String?](nstreecontroller/countkeypath.md)
  The key path used to find the number of children for a node.
- [func countKeyPath(for: NSTreeNode) -> String?](nstreecontroller/countkeypath(for:).md)
  Returns the key path that provides the number of children for a specified node.
- [func leafKeyPath(for: NSTreeNode) -> String?](nstreecontroller/leafkeypath(for:).md)
  Returns the key path that specifies whether the node is a leaf node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/leafkeypath)*