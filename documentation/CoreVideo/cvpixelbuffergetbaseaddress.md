# CVPixelBufferGetBaseAddress(_:)

**Framework**: Core Video  
**Kind**: func

Returns the base address of the pixel buffer.

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
func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer) -> UnsafeMutableRawPointer?
```

#### Return Value

The base address of the pixel buffer.

#### Discussion

The pointer returned by this function depends on the type of buffer and the conditions under which it was created.

- For chunky buffers, returns a pointer to the pixel at (0,0) in the buffer.
- For planar buffers, returns a pointer to a [`CVPlanarComponentInfo`](cvplanarcomponentinfo.md) structure, or `NULL` if no such structure is present.

Because this function returns `NULL` for some planar buffers, you should call [`CVPixelBufferGetBaseAddressOfPlane(_:_:)`](cvpixelbuffergetbaseaddressofplane(_:_:).md) and [`CVPixelBufferGetBytesPerRowOfPlane(_:_:)`](cvpixelbuffergetbytesperrowofplane(_:_:).md) to get information about a planar buffer.

Retrieving the base address for a pixel buffer requires that the buffer base address be locked using the [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) function.

## Parameters

- `pixelBuffer`: The pixel buffer whose base address you want to obtain.

## See Also

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
- [func CVPixelBufferGetExtendedPixels(CVPixelBuffer, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?)](cvpixelbuffergetextendedpixels(_:_:_:_:_:).md)
  Returns the amount of extended pixel padding in the pixel buffer.
- [func CVPixelBufferGetIOSurface(CVPixelBuffer?) -> Unmanaged<IOSurfaceRef>?](cvpixelbuffergetiosurface(_:).md)
  Returns the IOSurface backing the pixel buffer, or `NULL` if it is not backed by an IOSurface.
- [func CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator?, CFArray?, UnsafeMutablePointer<CFDictionary?>) -> CVReturn](cvpixelbuffercreateresolvedattributesdictionary(_:_:_:).md)
  Resolves an array of `CFDictionary` objects describing various pixel buffer attributes into a single dictionary.
- [func CVPixelBufferGetTypeID() -> CFTypeID](cvpixelbuffergettypeid().md)
  Returns the Core Foundation type identifier of the pixel buffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffergetbaseaddress(_:))*