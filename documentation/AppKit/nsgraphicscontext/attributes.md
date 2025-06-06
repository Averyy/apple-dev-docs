# attributes

**Framework**: AppKit  
**Kind**: property

The attributes used to create this instance.

**Availability**:
- macOS ?+

## Declaration

```swift
var attributes: [NSGraphicsContext.AttributeKey : Any]? { get }
```

#### Discussion

Screen-based graphics contexts do not store attributes, even if you create them using [`init(attributes:)`](nsgraphicscontext/init(attributes:).md).

## See Also

- [NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [NSGraphicsContext.RepresentationFormatName](nsgraphicscontext/representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.
- [var isFlipped: Bool](nsgraphicscontext/isflipped.md)
  A Boolean value that indicates the graphics context’s flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/attributes)*