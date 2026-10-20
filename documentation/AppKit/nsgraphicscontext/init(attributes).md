# init(attributes:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a graphics context using the specified attributes.

**Availability**:
- macOS

## Declaration

```swift
init?(attributes: [NSGraphicsContext.AttributeKey : Any] = [:])
```

```objc
+ (NSGraphicsContext *) graphicsContextWithAttributes:(NSDictionary<NSString *,id> *) attributes;
```

#### Return Value

A new [`NSGraphicsContext`](../nsgraphicscontext.md) object, or `nil` if the object could not be created.

#### Discussion

Use this method to create a graphics context for a window or bitmap destination. If you want to create a graphics context for a PDF or PostScript destination, do not use this method; instead, use the [`NSPrintOperation`](../nsprintoperation.md) class to set up the printing environment needed to generate that type of information.

## Parameters

- `attributes`: A dictionary of values associated with the keys described in [`NSGraphicsContext.AttributeKey`](./attributekey.md). The attributes specify such things as representation format and destination.

## See Also

### Creating a Graphics Context
- [init?(bitmapImageRep: NSBitmapImageRep)](./init%28bitmapimagerep%29.md)
  Creates a new graphics context using the specified bitmap image representation object as the context destination.
- [init(cgContext: CGContext, flipped: Bool)](./init%28cgcontext,flipped%29-9cbad.md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(attributes:))*