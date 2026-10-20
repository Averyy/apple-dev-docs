# CVPixelBufferIsCompatibleWithAttributes(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func CVPixelBufferIsCompatibleWithAttributes(_ pixelBuffer: CVPixelBuffer, _ attributes: CFDictionary?) -> Bool
```

```c
extern Boolean CVPixelBufferIsCompatibleWithAttributes(CVPixelBufferRef pixelBuffer, CFDictionaryRef attributes);
```

#### Discussion

Returns true if given pixel buffer is compatible with pixelBufferAttributes dictionary.

## Parameters

- `pixelBuffer`: PixelBuffer to check for compatibility.
- `attributes`: Creation attributes which pixel buffer should have.

## See Also

### Inspecting Pixel Buffers
- [func CVPixelBufferGetBaseAddress(CVPixelBuffer) -> UnsafeMutableRawPointer?](./cvpixelbuffergetbaseaddress%28_%29.md)
  Returns the base address of the pixel buffer.
- [func CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer, Int) -> UnsafeMutableRawPointer?](./cvpixelbuffergetbaseaddressofplane%28_,_%29.md)
  Returns the base address of the plane at the specified plane index.
- [func CVPixelBufferGetBytesPerRow(CVPixelBuffer) -> Int](./cvpixelbuffergetbytesperrow%28_%29.md)
  Returns the number of bytes per row of the pixel buffer.
- [func CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer, Int) -> Int](./cvpixelbuffergetbytesperrowofplane%28_,_%29.md)
  Returns the number of bytes per row for a plane at the specified index in the pixel buffer.
- [func CVPixelBufferGetHeight(CVPixelBuffer) -> Int](./cvpixelbuffergetheight%28_%29.md)
  Returns the height of the pixel buffer.
- [func CVPixelBufferGetHeightOfPlane(CVPixelBuffer, Int) -> Int](./cvpixelbuffergetheightofplane%28_,_%29.md)
  Returns the height of the plane at planeIndex in the pixel buffer.
- [func CVPixelBufferGetWidth(CVPixelBuffer) -> Int](./cvpixelbuffergetwidth%28_%29.md)
  Returns the width of the pixel buffer.
- [func CVPixelBufferGetWidthOfPlane(CVPixelBuffer, Int) -> Int](./cvpixelbuffergetwidthofplane%28_,_%29.md)
  Returns the width of the plane at a given index in the pixel buffer.
- [func CVPixelBufferIsPlanar(CVPixelBuffer) -> Bool](./cvpixelbufferisplanar%28_%29.md)
  Determines whether the pixel buffer is planar.
- [func CVPixelBufferGetPlaneCount(CVPixelBuffer) -> Int](./cvpixelbuffergetplanecount%28_%29.md)
  Returns number of planes of the pixel buffer.
- [func CVPixelBufferGetDataSize(CVPixelBuffer) -> Int](./cvpixelbuffergetdatasize%28_%29.md)
  Returns the data size for contiguous planes of the pixel buffer.
- [func CVPixelBufferGetPixelFormatType(CVPixelBuffer) -> OSType](./cvpixelbuffergetpixelformattype%28_%29.md)
  Returns the pixel format type of the pixel buffer.
- [func CVPixelBufferGetExtendedPixels(CVPixelBuffer, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?)](./cvpixelbuffergetextendedpixels%28_,_,_,_,_%29.md)
  Returns the amount of extended pixel padding in the pixel buffer.
- [func CVPixelBufferGetIOSurface(CVPixelBuffer?) -> Unmanaged<IOSurfaceRef>?](./cvpixelbuffergetiosurface%28_%29.md)
  Returns the IOSurface backing the pixel buffer, or `NULL` if it is not backed by an IOSurface.
- [func CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator?, CFArray?, UnsafeMutablePointer<CFDictionary?>) -> CVReturn](./cvpixelbuffercreateresolvedattributesdictionary%28_,_,_%29.md)
  Resolves an array of `CFDictionary` objects describing various pixel buffer attributes into a single dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferiscompatiblewithattributes(_:_:))*