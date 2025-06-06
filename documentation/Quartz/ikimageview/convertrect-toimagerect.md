# convertRect(toImageRect:)

**Framework**: Quartz  
**Kind**: method

Converts an image view rectangle to an image rectangle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func convertRect(toImageRect viewRect: NSRect) -> NSRect
```

#### Return Value

The rectangle specified in coordinates relative to the image.

## Parameters

- `viewRect`: An rectangle specified in coordinates relative to the image view.

## See Also

- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](ikimageview/convertpoint(toimagepoint:).md)
  Converts an image view coordinate to an image coordinate.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](ikimageview/convertimagepoint(toviewpoint:).md)
  Converts an image coordinate to an image view coordinate.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](ikimageview/convertimagerect(toviewrect:).md)
  Converts an image rectangle to an image view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertrect(toimagerect:))*