# bitmapData

**Framework**: AppKit  
**Kind**: property

A pointer to the bitmap data.

**Availability**:
- macOS ?+

## Declaration

```swift
var bitmapData: UnsafeMutablePointer<UInt8>? { get }
```

#### Discussion

For planar data, the value in this property points to the first plane.

## See Also

- [func getPixel(UnsafeMutablePointer<Int>, atX: Int, y: Int)](nsbitmapimagerep/getpixel(_:atx:y:).md)
  Returns by indirection the pixel data for the specified location in the bitmap image representation.
- [func getBitmapDataPlanes(UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>)](nsbitmapimagerep/getbitmapdataplanes(_:).md)
  Returns by indirection bitmap data of the bitmap image representation separated into planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/bitmapdata)*