# convertImagePoint(toViewPoint:)

**Framework**: Quartz  
**Kind**: method

Converts an image coordinate to an image view coordinate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func convertImagePoint(toViewPoint imagePoint: NSPoint) -> NSPoint
```

#### Return Value

A point specified in coordinates relative to the image view.

## Parameters

- `imagePoint`: A point specified in coordinates relative to the image.

## See Also

- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](ikimageview/convertpoint(toimagepoint:).md)
  Converts an image view coordinate to an image coordinate.
- [func convertRect(toImageRect: NSRect) -> NSRect](ikimageview/convertrect(toimagerect:).md)
  Converts an image view rectangle to an image rectangle.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](ikimageview/convertimagerect(toviewrect:).md)
  Converts an image rectangle to an image view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertimagepoint(toviewpoint:))*