# getPixel(_:atX:y:)

**Framework**: AppKit  
**Kind**: method

Returns by indirection the pixel data for the specified location in the bitmap image representation.

**Availability**:
- macOS ?+

## Declaration

```swift
func getPixel(_ p: UnsafeMutablePointer<Int>, atX x: Int, y: Int)
```

#### Discussion

The origin is in the top-left corner.

## Parameters

- `p`: On return, an array of integers containing raw pixel data in the appropriate order according to the object’s bitmap format. Smaller integer samples, such as 4-bit, are returned as an integer. Floating point values are cast to integer values and returned.
- `x`: The x-axis coordinate of the pixel.
- `y`: The y-axis coordinate of the pixel.

## See Also

- [var bitmapFormat: NSBitmapImageRep.Format](nsbitmapimagerep/bitmapformat.md)
  The format of the bitmap image representation.
- [func setColor(NSColor, atX: Int, y: Int)](nsbitmapimagerep/setcolor(_:atx:y:).md)
  Changes the color of the pixel at the specified coordinates.
- [func colorAt(x: Int, y: Int) -> NSColor?](nsbitmapimagerep/colorat(x:y:).md)
  Returns the color of the pixel at the specified coordinates.
- [func setPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](nsbitmapimagerep/setpixel(_:atx:y:).md)
  Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/getpixel(_:atx:y:))*