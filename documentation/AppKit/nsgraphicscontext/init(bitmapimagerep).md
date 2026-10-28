# init(bitmapImageRep:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new graphics context using the specified bitmap image representation object as the context destination.

**Availability**:
- macOS

## Declaration

```swift
init?(bitmapImageRep bitmapRep: NSBitmapImageRep)
```

```objc
+ (NSGraphicsContext *) graphicsContextWithBitmapImageRep:(NSBitmapImageRep *) bitmapRep;
```

## Return Value

The created [`NSGraphicsContext`](../nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Discussion

This method accepts only single plane [`NSBitmapImageRep`](../nsbitmapimagerep.md) instances. It is the equivalent of using [`init(attributes:)`](./init%28attributes%29.md) and passing `bitmapRep` as the value for the dictionary’s [`destination`](./attributekey/destination.md) key.

## Parameters

- `bitmapRep`: The [`NSBitmapImageRep`](../nsbitmapimagerep.md) object to use as the destination.

## See Also

### Creating a Graphics Context
- [init?(attributes: [NSGraphicsContext.AttributeKey : Any])](./init%28attributes%29.md)
  Creates a graphics context using the specified attributes.
- [init(cgContext: CGContext, flipped: Bool)](./init%28cgcontext,flipped%29-9cbad.md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(bitmapimagerep:))*