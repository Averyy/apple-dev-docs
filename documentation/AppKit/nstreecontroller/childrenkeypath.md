# childrenKeyPath

**Framework**: AppKit  
**Kind**: property

The key path used to find the children in the tree controller’s objects.

**Availability**:
- macOS ?+

## Declaration

```swift
var childrenKeyPath: String? { get set }
```

#### Discussion

The default value of this property is `nil`.

## See Also

- [func childrenKeyPath(for: NSTreeNode) -> String?](nstreecontroller/childrenkeypath(for:).md)
  Returns the key path used to find the children in the specified tree node.
- [var countKeyPath: String?](nstreecontroller/countkeypath.md)
  The key path used to find the number of children for a node.
- [func countKeyPath(for: NSTreeNode) -> String?](nstreecontroller/countkeypath(for:).md)
  Returns the key path that provides the number of children for a specified node.
- [var leafKeyPath: String?](nstreecontroller/leafkeypath.md)
  The key path used by the tree controller to determine if a node is a leaf key.
- [func leafKeyPath(for: NSTreeNode) -> String?](nstreecontroller/leafkeypath(for:).md)
  Returns the key path that specifies whether the node is a leaf node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/childrenkeypath)*