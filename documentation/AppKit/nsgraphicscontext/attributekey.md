# NSGraphicsContext.AttributeKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the dictionary keys for the attributes of the graphics context.

**Availability**:
- macOS

## Declaration

```swift
struct AttributeKey
```

```c
typedef NSString * NSGraphicsContextAttributeKey;
```

#### Discussion

You use these dictionary keys with [`init(attributes:)`](./init%28attributes%29.md) and [`attributes`](./attributes.md).

## Topics

### Attribute Keys
- [static let destination: NSGraphicsContext.AttributeKey](./attributekey/destination.md)
  Specifies the destination.
- [static let representationFormat: NSGraphicsContext.AttributeKey](./attributekey/representationformat.md)
  Specifies the destination file format.
### Initializers
- [init(rawValue: String)](./attributekey/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Information About the Context
- [var attributes: [NSGraphicsContext.AttributeKey : Any]?](./attributes.md)
  The attributes used to create this instance.
- [NSGraphicsContext.RepresentationFormatName](./representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/attributekey)*