# attributes

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The attributes associated with a view element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var attributes: [String : String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,NSString *> * attributes;
```

#### Discussion

All of the attributes are defined as key-value pairs.

## See Also

### Inspecting a View Element
- [var autoHighlightIdentifier: String?](./autohighlightidentifier.md)
  A string identifying the element that is initially in focus.
- [var children: [TVViewElement]?](./children.md)
  An array containing the child elements of the element currently being inspected.
- [var isDisabled: Bool](./isdisabled.md)
  Boolean value indicating whether the current element being inspected is disabled.
- [var identifier: String](./identifier.md)
  A string containing the unique identifier for an element.
- [var name: String](./name.md)
  A string containing the element’s name.
- [var parent: TVViewElement?](./parent.md)
  The parent of the current node.
- [var style: TVViewElementStyle?](./style.md)
  The style applied to an element.
- [var updateType: TVElementUpdateType](./updatetype.md)
  The value that describes any changes to the DOM tree after it has been reparsed.
- [enum TVElementUpdateType](../tvelementupdatetype.md)
  Describes any changes to the DOM tree after it has been reparsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement/attributes)*