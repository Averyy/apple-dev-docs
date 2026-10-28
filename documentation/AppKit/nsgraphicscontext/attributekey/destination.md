# destination

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Specifies the destination.

**Availability**:
- macOS

## Declaration

```swift
static let destination: NSGraphicsContext.AttributeKey
```

```c
extern NSGraphicsContextAttributeKey NSGraphicsContextDestinationAttributeName;
```

## Discussion

This value can be an instance of [`NSWindow`](../../nswindow.md) or [`NSBitmapImageRep`](../../nsbitmapimagerep.md) when creating a graphics context.

When determining the type of a graphics context, this value can be an [`NSMutableData`](../../../Foundation/nsmutabledata.md), [`NSString`](../../../Foundation/nsstring.md), or [`NSURL`](../../../Foundation/nsurl.md) object.

## See Also

### Attribute Keys
- [static let representationFormat: NSGraphicsContext.AttributeKey](./representationformat.md)
  Specifies the destination file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/attributekey/destination)*