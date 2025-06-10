# NSGraphicsContext.RepresentationFormatName

**Framework**: AppKit  
**Kind**: struct

Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
struct RepresentationFormatName
```

#### Discussion

You use these constants with the [`representationFormat`](nsgraphicscontext/attributekey/representationformat.md) key.

## Topics

### Format Names
- [static let pdf: NSGraphicsContext.RepresentationFormatName](nsgraphicscontext/representationformatname/pdf.md)
  Destination file format is PDF.
- [static let postScript: NSGraphicsContext.RepresentationFormatName](nsgraphicscontext/representationformatname/postscript.md)
  Destination file format is PostScript.
### Initializers
- [init(rawValue: String)](nsgraphicscontext/representationformatname/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var attributes: [NSGraphicsContext.AttributeKey : Any]?](nsgraphicscontext/attributes.md)
  The attributes used to create this instance.
- [NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [var isFlipped: Bool](nsgraphicscontext/isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/representationformatname)*