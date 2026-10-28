# convertPoint(toImagePoint:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Converts an image view coordinate to an image coordinate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func convertPoint(toImagePoint viewPoint: NSPoint) -> NSPoint
```

```objc
- (NSPoint) convertViewPointToImagePoint:(NSPoint) viewPoint;
```

## Return Value

The point specified in coordinates relative to the image.

## Parameters

- `viewPoint`: A point specified in coordinates relative to the image view.

## See Also

### Converting Points and Rectangles
- [func convertRect(toImageRect: NSRect) -> NSRect](./convertrect%28toimagerect%29.md)
  Converts an image view rectangle to an image rectangle.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](./convertimagepoint%28toviewpoint%29.md)
  Converts an image coordinate to an image view coordinate.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](./convertimagerect%28toviewrect%29.md)
  Converts an image rectangle to an image view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertpoint(toimagepoint:))*