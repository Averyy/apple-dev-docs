# isFlipped

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates the graphics context’s flipped state.

**Availability**:
- macOS ?+

## Declaration

```swift
var isFlipped: Bool { get }
```

#### Discussion

The state is determined by sending `flipped` to the receiver’s view that has focus. If no view has focus, returns [`false`](https://developer.apple.com/documentation/Swift/false) unless the receiver is instantiated using [`init(cgContext:flipped:)`](nsgraphicscontext/init(cgcontext:flipped:).md) specifying [`true`](https://developer.apple.com/documentation/Swift/true) as the `flipped` parameter.

## See Also

- [init(cgContext: CGContext, flipped: Bool)](nsgraphicscontext/init(cgcontext:flipped:).md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.
- [var attributes: [NSGraphicsContext.AttributeKey : Any]?](nsgraphicscontext/attributes.md)
  The attributes used to create this instance.
- [NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [NSGraphicsContext.RepresentationFormatName](nsgraphicscontext/representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/isflipped)*