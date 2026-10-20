# retagging(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the color space tag of the bitmap image representation.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func retagging(with newSpace: NSColorSpace) -> NSBitmapImageRep?
```

```objc
- (NSBitmapImageRep *) bitmapImageRepByRetaggingWithColorSpace:(NSColorSpace *) newSpace;
```

#### Return Value

An [`NSBitmapImageRep`](../nsbitmapimagerep.md), or `nil`, if the conversion fails. If the original [`NSBitmapImageRep`](../nsbitmapimagerep.md) already uses that color space, it is returned as is.

#### Discussion

This method will definitely fail if you pass a color space that has a different color space model than the receiver. That is, if your original image is sRGB, you can only retag with some other RGB colorspace.

## Parameters

- `newSpace`: The desired color space.

## See Also

### Managing Color Spaces
- [func converting(to: NSColorSpace, renderingIntent: NSColorRenderingIntent) -> NSBitmapImageRep?](./converting%28to,renderingintent%29.md)
  Converts the bitmap image representation to the specified color space.
- [var colorSpace: NSColorSpace](./colorspace.md)
  The color space of the bitmap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/retagging(with:))*