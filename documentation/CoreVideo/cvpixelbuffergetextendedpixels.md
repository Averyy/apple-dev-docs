# CVPixelBufferGetExtendedPixels(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Returns the amount of extended pixel padding in the pixel buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>?, _ extraColumnsOnRight: UnsafeMutablePointer<Int>?, _ extraRowsOnTop: UnsafeMutablePointer<Int>?, _ extraRowsOnBottom: UnsafeMutablePointer<Int>?)
```

#### Discussion

## Parameters

- `pixelBuffer`: The pixel buffer whose extended pixel size you want to obtain.
- `extraColumnsOnLeft`: On output, the pixel row padding to the left.  Pass   if you do not want this information.
- `extraColumnsOnRight`: On output, the pixel row padding to the right. Pass   if you do not want this information.
- `extraRowsOnTop`: On output, the pixel row padding to the top.  Pass   if you do not want this information.
- `extraRowsOnBottom`: On output, the pixel row padding to the bottom. Pass   if you do not want this information.

## See Also

- [func CVPixelBufferGetBaseAddress(CVPixelBuffer) -> UnsafeMutableRawPointer?](cvpixelbuffergetbaseaddress(_:).md)
  Returns the base address of the pixel buffer.
- [func CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer, Int) -> UnsafeMutableRawPointer?](cvpixelbuffergetbaseaddressofplane(_:_:).md)
  Returns the base address of the plane at the specified plane index.
- [func CVPixelBufferGetBytesPerRow(CVPixelBuffer) -> Int](cvpixelbuffergetbytesperrow(_:).md)
  Returns the number of bytes per row of the pixel buffer.
- [func CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer, Int) -> Int](cvpixelbuffergetbytesperrowofplane(_:_:).md)
  Returns the number of bytes per row for a plane at the specified index in the pixel buffer.
- [func CVPixelBufferGetHeight(CVPixelBuffer) -> Int](cvpixelbuffergetheight(_:).md)
  Returns the height of the pixel buffer.
- [func CVPixelBufferGetHeightOfPlane(CVPixelBuffer, Int) -> Int](cvpixelbuffergetheightofplane(_:_:).md)
  Returns the height of the plane at planeIndex in the pixel buffer.
- [func CVPixelBufferGetWidth(CVPixelBuffer) -> Int](cvpixelbuffergetwidth(_:).md)
  Returns the width of the pixel buffer.
- [func CVPixelBufferGetWidthOfPlane(CVPixelBuffer, Int) -> Int](cvpixelbuffergetwidthofplane(_:_:).md)
  Returns the width of the plane at a given index in the pixel buffer.
- [func CVPixelBufferIsPlanar(CVPixelBuffer) -> Bool](cvpixelbufferisplanar(_:).md)
  Determines whether the pixel buffer is planar.
- [func CVPixelBufferGetPlaneCount(CVPixelBuffer) -> Int](cvpixelbuffergetplanecount(_:).md)
  Returns number of planes of the pixel buffer.
- [func CVPixelBufferGetDataSize(CVPixelBuffer) -> Int](cvpixelbuffergetdatasize(_:).md)
  Returns the data size for contiguous planes of the pixel buffer.
- [func CVPixelBufferGetPixelFormatType(CVPixelBuffer) -> OSType](cvpixelbuffergetpixelformattype(_:).md)
  Returns the pixel format type of the pixel buffer.
- [func CVPixelBufferGetIOSurface(CVPixelBuffer?) -> Unmanaged<IOSurfaceRef>?](cvpixelbuffergetiosurface(_:).md)
  Returns the IOSurface backing the pixel buffer, or `NULL` if it is not backed by an IOSurface.
- [func CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator?, CFArray?, UnsafeMutablePointer<CFDictionary?>) -> CVReturn](cvpixelbuffercreateresolvedattributesdictionary(_:_:_:).md)
  Resolves an array of `CFDictionary` objects describing various pixel buffer attributes into a single dictionary.
- [func CVPixelBufferGetTypeID() -> CFTypeID](cvpixelbuffergettypeid().md)
  Returns the Core Foundation type identifier of the pixel buffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffergetextendedpixels(_:_:_:_:_:))*