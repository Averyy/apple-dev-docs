# convertRect(toImageRect:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Converts an image view rectangle to an image rectangle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func convertRect(toImageRect viewRect: NSRect) -> NSRect
```

```objc
- (NSRect) convertViewRectToImageRect:(NSRect) viewRect;
```

#### Return Value

The rectangle specified in coordinates relative to the image.

## Parameters

- `viewRect`: An rectangle specified in coordinates relative to the image view.

## See Also

### Converting Points and Rectangles
- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](./convertpoint%28toimagepoint%29.md)
  Converts an image view coordinate to an image coordinate.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](./convertimagepoint%28toviewpoint%29.md)
  Converts an image coordinate to an image view coordinate.
- [func convertImageRect(toViewRect: NSRect) -> NSRect](./convertimagerect%28toviewrect%29.md)
  Converts an image rectangle to an image view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertrect(toimagerect:))*