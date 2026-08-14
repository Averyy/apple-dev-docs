# TVViewElementStyleType

**Framework**: TVMLKit  
**Kind**: enum

Describes the different style types for an element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
enum TVViewElementStyleType
```

## Topics

### Constants
- [TVViewElementStyleType.integer](tvviewelementstyletype/integer.md)
  An [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) value.
- [TVViewElementStyleType.double](tvviewelementstyletype/double.md)
  An [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) value.
- [TVViewElementStyleType.point](tvviewelementstyletype/point.md)
  A [`CGPoint`](https://developer.apple.com/documentation/corefoundation/cgpoint) value.
- [TVViewElementStyleType.string](tvviewelementstyletype/string.md)
  A [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) value.
- [TVViewElementStyleType.color](tvviewelementstyletype/color.md)
  A [`TVColor`](tvcolor.md) value.
- [TVViewElementStyleType.URL](tvviewelementstyletype/url.md)
  A [`NSURL`](https://developer.apple.com/documentation/foundation/nsurl) value.
- [TVViewElementStyleType.edgeInsets](tvviewelementstyletype/edgeinsets.md)
  An [`UIEdgeInsets`](https://developer.apple.com/documentation/uikit/uiedgeinsets) value.
### Enumeration Cases
- [TVViewElementStyleType.transform](tvviewelementstyletype/transform.md)
### Initializers
- [init?(rawValue: Int)](tvviewelementstyletype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class func registerStyleName(String, type: TVViewElementStyleType, inherited: Bool)](tvstylefactory/registerstylename(_:type:inherited:).md)
  Creates a new style property of the indicated type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyletype)*