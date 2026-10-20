# TVElementUpdateType.children

**Framework**: TVMLKit  
**Kind**: case  
**Role**: Case

The order of child nodes have been updated due to the addition, removal, or replacement of child nodes.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
case children
```

```c
TVElementUpdateTypeChildren
```

## See Also

### Constants
- [TVElementUpdateType.none](./none.md)
  The tree structure did not change.
- [TVElementUpdateType.subtree](./subtree.md)
  A subtree element has been updated without affecting the order of any immediate children.
- [TVElementUpdateType.node](./node.md)
  The current node and its subtree have been modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/children)*