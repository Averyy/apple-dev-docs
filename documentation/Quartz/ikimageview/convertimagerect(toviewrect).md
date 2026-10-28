# convertImageRect(toViewRect:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Converts an image rectangle to an image view rectangle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func convertImageRect(toViewRect imageRect: NSRect) -> NSRect
```

```objc
- (NSRect) convertImageRectToViewRect:(NSRect) imageRect;
```

## Return Value

An rectangle specified in coordinates relative to the image view.

## Parameters

- `imageRect`: An rectangle specified in coordinates relative to the image.

## See Also

### Converting Points and Rectangles
- [func convertPoint(toImagePoint: NSPoint) -> NSPoint](./convertpoint%28toimagepoint%29.md)
  Converts an image view coordinate to an image coordinate.
- [func convertRect(toImageRect: NSRect) -> NSRect](./convertrect%28toimagerect%29.md)
  Converts an image view rectangle to an image rectangle.
- [func convertImagePoint(toViewPoint: NSPoint) -> NSPoint](./convertimagepoint%28toviewpoint%29.md)
  Converts an image coordinate to an image view coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/convertimagerect(toviewrect:))*