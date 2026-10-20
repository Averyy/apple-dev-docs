# setPixel(_:atX:y:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.

**Availability**:
- macOS

## Declaration

```swift
func setPixel(_ p: UnsafeMutablePointer<Int>, atX x: Int, y: Int)
```

```objc
- (void) setPixel:(NSUInteger[]) p atX:(NSInteger) x y:(NSInteger) y;
```

## Parameters

- `p`: An array of integers representing the raw pixel values. The values must be in an order appropriate to the object’s bitmap format. Small pixel sample values should be passed as an integer value. Floating point values should be cast `int[]`.
- `x`: The x-axis coordinate of the pixel.
- `y`: The y-axis coordinate of the pixel.

## See Also

### Related Documentation
- [var bitmapFormat: NSBitmapImageRep.Format](./bitmapformat.md)
  The format of the bitmap image representation.
### Managing Pixel Values
- [func setColor(NSColor, atX: Int, y: Int)](./setcolor%28_,atx,y%29.md)
  Changes the color of the pixel at the specified coordinates.
- [func colorAt(x: Int, y: Int) -> NSColor?](./colorat%28x,y%29.md)
  Returns the color of the pixel at the specified coordinates.
- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./getpixel%28_,atx,y%29.md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/setpixel(_:atx:y:))*