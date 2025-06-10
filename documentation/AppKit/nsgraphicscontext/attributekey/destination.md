# destination

**Framework**: AppKit  
**Kind**: property

Specifies the destination.

**Availability**:
- macOS ?+

## Declaration

```swift
static let destination: NSGraphicsContext.AttributeKey
```

#### Discussion

This value can be an instance of [`NSWindow`](nswindow.md) or [`NSBitmapImageRep`](nsbitmapimagerep.md) when creating a graphics context.

When determining the type of a graphics context, this value can be an [`NSMutableData`](https://developer.apple.com/documentation/Foundation/NSMutableData), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object.

## See Also

- [static let representationFormat: NSGraphicsContext.AttributeKey](nsgraphicscontext/attributekey/representationformat.md)
  Specifies the destination file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/attributekey/destination)*