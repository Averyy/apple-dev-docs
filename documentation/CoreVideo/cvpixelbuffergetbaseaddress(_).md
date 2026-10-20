# CVPixelBufferGetBaseAddress(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

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

```c
extern void *CVPixelBufferGetBaseAddress(CVPixelBufferRef pixelBuffer);
```

#### Return Value

The base address of the pixel buffer.

#### Discussion

The pointer returned by this function depends on the type of buffer and the conditions under which it was created.

- For chunky buffers, returns a pointer to the pixel at (0,0) in the buffer.
- For planar buffers, returns a pointer to a [`CVPlanarComponentInfo`](./cvplanarcomponentinfo.md) structure, or `NULL` if no such structure is present.

Because this function returns `NULL` for some planar buffers, you should call [`CVPixelBufferGetBaseAddressOfPlane(_:_:)`](./cvpixelbuffergetbaseaddressofplane%28_,_%29.md) and [`CVPixelBufferGetBytesPerRowOfPlane(_:_:)`](./cvpixelbuffergetbytesperrowofplane%28_,_%29.md) to get information about a planar buffer.

Retrieving the base address for a pixel buffer requires that the buffer base address be locked using the [`CVPixelBufferLockBaseAddress(_:_:)`](./cvpixelbufferlockbaseaddress%28_,_%29.md) function.

## Parameters

- `pixelBuffer`: The pixel buffer whose base address you want to obtain.

## See Also

### Inspecting Pixel Buffers
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
- [func CVPixelBufferIsCompatibleWithAttributes(CVPixelBuffer, CFDictionary?) -> Bool](./cvpixelbufferiscompatiblewithattributes%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffergetbaseaddress(_:))*