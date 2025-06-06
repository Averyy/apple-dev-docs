# setPixel(_:atX:y:)

**Framework**: AppKit  
**Kind**: method

Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.

**Availability**:
- macOS ?+

## Declaration

```swift
func setPixel(_ p: UnsafeMutablePointer<Int>, atX x: Int, y: Int)
```

## Parameters

- `p`: An array of integers representing the raw pixel values. The values must be in an order appropriate to the object’s bitmap format. Small pixel sample values should be passed as an integer value. Floating point values should be cast  .
- `x`: The x-axis coordinate of the pixel.
- `y`: The y-axis coordinate of the pixel.

## See Also

- [var bitmapFormat: NSBitmapImageRep.Format](nsbitmapimagerep/bitmapformat.md)
  The format of the bitmap image representation.
- [func setColor(NSColor, atX: Int, y: Int)](nsbitmapimagerep/setcolor(_:atx:y:).md)
  Changes the color of the pixel at the specified coordinates.
- [func colorAt(x: Int, y: Int) -> NSColor?](nsbitmapimagerep/colorat(x:y:).md)
  Returns the color of the pixel at the specified coordinates.
- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](nsbitmapimagerep/getpixel(_:atx:y:).md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/setpixel(_:atx:y:))*