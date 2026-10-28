# getPixel(_:atX:y:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns by indirection the pixel data for the specified location in the bitmap image representation.

**Availability**:
- macOS

## Declaration

```swift
func getPixel(_ p: UnsafeMutablePointer<Int>, atX x: Int, y: Int)
```

```objc
- (void) getPixel:(NSUInteger[]) p atX:(NSInteger) x y:(NSInteger) y;
```

## Discussion

The origin is in the top-left corner.

## Parameters

- `p`: On return, an array of integers containing raw pixel data in the appropriate order according to the object’s bitmap format. Smaller integer samples, such as 4-bit, are returned as an integer. Floating point values are cast to integer values and returned.
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
- [func setPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./setpixel%28_,atx,y%29.md)
  Sets the bitmap image representation’s pixel at the specified coordinates to the specified raw pixel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/getpixel(_:atx:y:))*