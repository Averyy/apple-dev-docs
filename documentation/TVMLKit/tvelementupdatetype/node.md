# TVElementUpdateType.node

**Framework**: TVMLKit  
**Kind**: case  
**Role**: Case

The current node and its subtree have been modified.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
case node
```

```c
TVElementUpdateTypeSelf
```

## See Also

### Constants
- [TVElementUpdateType.none](./none.md)
  The tree structure did not change.
- [TVElementUpdateType.subtree](./subtree.md)
  A subtree element has been updated without affecting the order of any immediate children.
- [TVElementUpdateType.children](./children.md)
  The order of child nodes have been updated due to the addition, removal, or replacement of child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype/node)*