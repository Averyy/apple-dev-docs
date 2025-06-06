# convertPoint(toImagePoint:)

**Framework**: Quartz  
**Kind**: method

Converts an image view coordinate to an image coordinate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func convertPoint(toImagePoint viewPoint: NSPoint) -> NSPoint
```

#### Return Value

The point specified in coordinates relative to the image.

## Parameters

- `viewPoint`: A point specified in coordinates relative to the image view.

## See Also

- [func convertRect(toImageRect: NSRect) -> NSRect](ikimageview/convertrect(toimagerect:).md)
  Converts an image view rectangle to an image rectangle.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](ikimageview/convertimagepoint(toviewpoint:).md)
  Converts an image coordinate to an image view coordinate.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](ikimageview/convertimagerect(toviewrect:).md)
  Converts an image rectangle to an image view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertpoint(toimagepoint:))*