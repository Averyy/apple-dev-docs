# bitmapData

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A pointer to the bitmap data.

**Availability**:
- macOS

## Declaration

```swift
var bitmapData: UnsafeMutablePointer<UInt8>? { get }
```

```objc
@property (readonly, nullable) unsigned char * bitmapData;
```

## Discussion

For planar data, the value in this property points to the first plane.

## See Also

### Related Documentation
- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](./getpixel%28_,atx,y%29.md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.
### Getting the Bitmap Data
- [func getBitmapDataPlanes(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>)](./getbitmapdataplanes%28_%29.md)
  Returns by indirection bitmap data of the bitmap image representation separated into planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/bitmapdata)*