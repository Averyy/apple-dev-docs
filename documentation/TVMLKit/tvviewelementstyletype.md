# TVViewElementStyleType

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

Describes the different style types for an element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVViewElementStyleType
```

```c
enum TVViewElementStyleType : NSInteger;
```

## Topics

### Constants
- [TVViewElementStyleType.integer](./tvviewelementstyletype/integer.md)
  An [`NSNumber`](../Foundation/nsnumber.md) value.
- [TVViewElementStyleType.double](./tvviewelementstyletype/double.md)
  An [`NSNumber`](../Foundation/nsnumber.md) value.
- [TVViewElementStyleType.point](./tvviewelementstyletype/point.md)
  A [`CGPoint`](../CoreFoundation/cgpoint.md) value.
- [TVViewElementStyleType.string](./tvviewelementstyletype/string.md)
  A [`NSString`](../Foundation/nsstring.md) value.
- [TVViewElementStyleType.color](./tvviewelementstyletype/color.md)
  A [`TVColor`](./tvcolor.md) value.
- [TVViewElementStyleType.URL](./tvviewelementstyletype/url.md)
  A [`NSURL`](../Foundation/nsurl.md) value.
- [TVViewElementStyleType.edgeInsets](./tvviewelementstyletype/edgeinsets.md)
  An [`UIEdgeInsets`](../UIKit/uiedgeinsets.md) value.
### Enumeration Cases
- [TVViewElementStyleType.transform](./tvviewelementstyletype/transform.md)
### Initializers
- [init?(rawValue: Int)](./tvviewelementstyletype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating New Style Properties
- [class func registerStyleName(String, type: TVViewElementStyleType, inherited: Bool)](./tvstylefactory/registerstylename%28_,type,inherited%29.md)
  Creates a new style property of the indicated type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype)*