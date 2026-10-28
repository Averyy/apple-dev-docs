# isFlipped

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the graphics context’s flipped state.

**Availability**:
- macOS

## Declaration

```swift
var isFlipped: Bool { get }
```

```objc
@property (readonly, getter=isFlipped) BOOL flipped;
```

## Discussion

The state is determined by sending `flipped` to the receiver’s view that has focus. If no view has focus, returns [`false`](../../Swift/false.md) unless the receiver is instantiated using [`init(cgContext:flipped:)`](./init%28cgcontext,flipped%29-9cbad.md) specifying [`true`](../../Swift/true.md) as the `flipped` parameter.

## See Also

### Related Documentation
- [init(cgContext: CGContext, flipped: Bool)](./init%28cgcontext,flipped%29-9cbad.md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.
### Getting Information About the Context
- [var attributes: [NSGraphicsContext.AttributeKey : Any]?](./attributes.md)
  The attributes used to create this instance.
- [NSGraphicsContext.AttributeKey](./attributekey.md)
  Constants that specify the dictionary keys for the attributes of the graphics context.
- [NSGraphicsContext.RepresentationFormatName](./representationformatname.md)
  Constants that specify values for the representation format name key in a graphic context’s attributes dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/isflipped)*