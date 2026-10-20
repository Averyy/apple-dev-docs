# parent

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The parent of the current node.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
weak var parent: TVViewElement? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) TVViewElement * parentViewElement;
```

## See Also

### Inspecting a View Element
- [var autoHighlightIdentifier: String?](./autohighlightidentifier.md)
  A string identifying the element that is initially in focus.
- [var attributes: [String : String]?](./attributes.md)
  The attributes associated with a view element.
- [var children: [TVViewElement]?](./children.md)
  An array containing the child elements of the element currently being inspected.
- [var isDisabled: Bool](./isdisabled.md)
  Boolean value indicating whether the current element being inspected is disabled.
- [var identifier: String](./identifier.md)
  A string containing the unique identifier for an element.
- [var name: String](./name.md)
  A string containing the element’s name.
- [var style: TVViewElementStyle?](./style.md)
  The style applied to an element.
- [var updateType: TVElementUpdateType](./updatetype.md)
  The value that describes any changes to the DOM tree after it has been reparsed.
- [enum TVElementUpdateType](../tvelementupdatetype.md)
  Describes any changes to the DOM tree after it has been reparsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement/parent)*