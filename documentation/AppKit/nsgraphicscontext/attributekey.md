# NSGraphicsContext.AttributeKey

**Framework**: AppKit  
**Kind**: struct

Constants that specify the dictionary keys for the attributes of the graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AttributeKey
```

#### Discussion

You use these dictionary keys with [`init(attributes:)`](nsgraphicscontext/init(attributes:).md) and [`attributes`](nsgraphicscontext/attributes.md).

## Topics

### Attribute Keys
- [static let destination: NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey/destination.md)
  Specifies the destination.
- [static let representationFormat: NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey/representationformat.md)
  Specifies the destination file format.
### Initializers
- [init(rawValue: String)](nsgraphicscontext/attributekey/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var attributes: [NSGraphicsContext.AttributeKey : Any]?](nsgraphicscontext/attributes.md)
  The attributes used to create this instance.
- [NSGraphicsContext.RepresentationFormatName](nsgraphicscontext/representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.
- [var isFlipped: Bool](nsgraphicscontext/isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/attributekey)*