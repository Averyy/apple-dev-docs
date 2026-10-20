# TVElementUpdateType

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

Describes any changes to the DOM tree after it has been reparsed.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVElementUpdateType
```

```c
enum TVElementUpdateType : NSInteger;
```

## Topics

### Constants
- [TVElementUpdateType.none](./tvelementupdatetype/none.md)
  The tree structure did not change.
- [TVElementUpdateType.subtree](./tvelementupdatetype/subtree.md)
  A subtree element has been updated without affecting the order of any immediate children.
- [TVElementUpdateType.children](./tvelementupdatetype/children.md)
  The order of child nodes have been updated due to the addition, removal, or replacement of child nodes.
- [TVElementUpdateType.node](./tvelementupdatetype/node.md)
  The current node and its subtree have been modified.
### Enumeration Cases
- [TVElementUpdateType.styles](./tvelementupdatetype/styles.md)
### Initializers
- [init?(rawValue: Int)](./tvelementupdatetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting a View Element
- [var autoHighlightIdentifier: String?](./tvviewelement/autohighlightidentifier.md)
  A string identifying the element that is initially in focus.
- [var attributes: [String : String]?](./tvviewelement/attributes.md)
  The attributes associated with a view element.
- [var children: [TVViewElement]?](./tvviewelement/children.md)
  An array containing the child elements of the element currently being inspected.
- [var isDisabled: Bool](./tvviewelement/isdisabled.md)
  Boolean value indicating whether the current element being inspected is disabled.
- [var identifier: String](./tvviewelement/identifier.md)
  A string containing the unique identifier for an element.
- [var name: String](./tvviewelement/name.md)
  A string containing the element’s name.
- [var parent: TVViewElement?](./tvviewelement/parent.md)
  The parent of the current node.
- [var style: TVViewElementStyle?](./tvviewelement/style.md)
  The style applied to an element.
- [var updateType: TVElementUpdateType](./tvviewelement/updatetype.md)
  The value that describes any changes to the DOM tree after it has been reparsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementupdatetype)*