# setColor(_:atX:y:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the color of the pixel at the specified coordinates.

**Availability**:
- macOS

## Declaration

```swift
func setColor(_ color: NSColor, atX x: Int, y: Int)
```

```objc
- (void) setColor:(NSColor *) color atX:(NSInteger) x y:(NSInteger) y;
```

## Parameters

- `color`: A color object representing the color to be set.
- `x`: The x-axis coordinate of the pixel.
- `y`: The y-axis coordinate of the pixel.

## See Also

### Managing Pixel Values
- [func colorAt(x: Int, y: Int) -> NSColor?](./colorat%28x,y%29.md)
  Returns the color of the pixel at the specified coordinates.
- [func setPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./setpixel%28_,atx,y%29.md)
  Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.
- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./getpixel%28_,atx,y%29.md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/setcolor(_:atx:y:))*