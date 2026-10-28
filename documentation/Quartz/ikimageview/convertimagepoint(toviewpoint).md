# convertImagePoint(toViewPoint:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Converts an image coordinate to an image view coordinate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func convertImagePoint(toViewPoint imagePoint: NSPoint) -> NSPoint
```

```objc
- (NSPoint) convertImagePointToViewPoint:(NSPoint) imagePoint;
```

## Return Value

A point specified in coordinates relative to the image view.

## Parameters

- `imagePoint`: A point specified in coordinates relative to the image.

## See Also

### Converting Points and Rectangles
- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](./convertpoint%28toimagepoint%29.md)
  Converts an image view coordinate to an image coordinate.
- [func convertRect(toImageRect: NSRect) -> NSRect](./convertrect%28toimagerect%29.md)
  Converts an image view rectangle to an image rectangle.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](./convertimagerect%28toviewrect%29.md)
  Converts an image rectangle to an image view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertimagepoint(toviewpoint:))*