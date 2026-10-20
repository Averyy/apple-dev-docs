# NSGraphicsContext.RepresentationFormatName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.

**Availability**:
- macOS

## Declaration

```swift
struct RepresentationFormatName
```

```c
typedef NSString * NSGraphicsContextRepresentationFormatName;
```

#### Discussion

You use these constants with the [`representationFormat`](./attributekey/representationformat.md) key.

## Topics

### Format Names
- [static let pdf: NSGraphicsContext.RepresentationFormatName](./representationformatname/pdf.md)
  Destination file format is PDF.
- [static let postScript: NSGraphicsContext.RepresentationFormatName](./representationformatname/postscript.md)
  Destination file format is PostScript.
### Initializers
- [init(rawValue: String)](./representationformatname/init%28rawvalue%29.md)
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
- [NSGraphicsContext.AttributeKey](./attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/representationformatname)*