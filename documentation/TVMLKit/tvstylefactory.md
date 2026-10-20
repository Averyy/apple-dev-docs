# TVStyleFactory

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

An object used to register custom style properties.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVStyleFactory
```

```objc
@interface TVStyleFactory : NSObject
```

## Topics

### Creating New Style Properties
- [class func registerStyleName(String, type: TVViewElementStyleType, inherited: Bool)](./tvstylefactory/registerstylename%28_,type,inherited%29.md)
  Creates a new style property of the indicated type.
- [enum TVViewElementStyleType](./tvviewelementstyletype.md)
  Describes the different style types for an element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom Styles
- [class TVViewElementStyle](./tvviewelementstyle.md)
  A style applied to a view element.
- [class TVColor](./tvcolor.md)
  The color data used by styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvstylefactory)*