# converting(to:renderingIntent:)

**Framework**: AppKit  
**Kind**: method

Converts the bitmap image representation to the specified color space.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func converting(to targetSpace: NSColorSpace, renderingIntent: NSColorRenderingIntent) -> NSBitmapImageRep?
```

#### Return Value

An [`NSBitmapImageRep`](nsbitmapimagerep.md), or `nil`, if the conversion fails. If the original [`NSBitmapImageRep`](nsbitmapimagerep.md) already uses that color space, it is returned as is.

## Parameters

- `targetSpace`: The new color space.
- `renderingIntent`: The rendering intent specifies how to handle colors that are not located within the target color space. The supported values are  .

## See Also

- [func retagging(with: NSColorSpace) -> NSBitmapImageRep?](nsbitmapimagerep/retagging(with:).md)
  Changes the color space tag of the bitmap image representation.
- [var colorSpace: NSColorSpace](nsbitmapimagerep/colorspace.md)
  The color space of the bitmap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/converting(to:renderingintent:))*