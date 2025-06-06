# convertImageRect(toViewRect:)

**Framework**: Quartz  
**Kind**: method

Converts an image rectangle to an image view rectangle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func convertImageRect(toViewRect imageRect: NSRect) -> NSRect
```

#### Return Value

An rectangle specified in coordinates relative to the image view.

## Parameters

- `imageRect`: An rectangle specified in coordinates relative to the image.

## See Also

- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](ikimageview/convertpoint(toimagepoint:).md)
  Converts an image view coordinate to an image coordinate.
- [func convertRect(toImageRect: NSRect) -> NSRect](ikimageview/convertrect(toimagerect:).md)
  Converts an image view rectangle to an image rectangle.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](ikimageview/convertimagepoint(toviewpoint:).md)
  Converts an image coordinate to an image view coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertimagerect(toviewrect:))*