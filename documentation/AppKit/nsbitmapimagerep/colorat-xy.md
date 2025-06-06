# colorAt(x:y:)

**Framework**: AppKit  
**Kind**: method

Returns the color of the pixel at the specified coordinates.

**Availability**:
- macOS ?+

## Declaration

```swift
func colorAt(x: Int, y: Int) -> NSColor?
```

#### Return Value

A color object representing the color at the specified coordinates.

#### Discussion

Calling this method creates a new [`NSColor`](nscolor.md) object. The overhead of object creation means this method is best suited for infrequent color sampling. If you instead need to work with large numbers of pixels, access the bitmap data directly using the [`bitmapData`](nsbitmapimagerep/bitmapdata.md) property or the [`getPixel(_:atX:y:)`](nsbitmapimagerep/getpixel(_:atx:y:).md) method for better performance.

## Parameters

- `x`: The x-axis coordinate.
- `y`: The y-axis coordinate.

## See Also

- [func setColor(NSColor, atX: Int, y: Int)](nsbitmapimagerep/setcolor(_:atx:y:).md)
  Changes the color of the pixel at the specified coordinates.
- [func setPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](nsbitmapimagerep/setpixel(_:atx:y:).md)
  Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.
- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](nsbitmapimagerep/getpixel(_:atx:y:).md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/colorat(x:y:))*