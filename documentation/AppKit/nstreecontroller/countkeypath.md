# countKeyPath

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The key path used to find the number of children for a node.

**Availability**:
- macOS

## Declaration

```swift
var countKeyPath: String? { get set }
```

```objc
@property (copy, nullable) NSString * countKeyPath;
```

#### Discussion

Specifying this key path (if the data is available in the model object) can increase performance, but disables insert and remove functionality.

## See Also

### Specifying model attributes
- [var childrenKeyPath: String?](./childrenkeypath.md)
  The key path used to find the children in the tree controller’s objects.
- [func childrenKeyPath(for: NSTreeNode) -> String?](./childrenkeypath%28for%29.md)
  Returns the key path used to find the children in the specified tree node.
- [func countKeyPath(for: NSTreeNode) -> String?](./countkeypath%28for%29.md)
  Returns the key path that provides the number of children for a specified node.
- [var leafKeyPath: String?](./leafkeypath.md)
  The key path used by the tree controller to determine if a node is a leaf key.
- [func leafKeyPath(for: NSTreeNode) -> String?](./leafkeypath%28for%29.md)
  Returns the key path that specifies whether the node is a leaf node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/countkeypath)*