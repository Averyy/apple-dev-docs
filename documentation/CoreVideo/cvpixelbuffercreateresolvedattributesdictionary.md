# CVPixelBufferCreateResolvedAttributesDictionary(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Resolves an array of `CFDictionary` objects describing various pixel buffer attributes into a single dictionary.

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
func CVPixelBufferCreateResolvedAttributesDictionary(_ allocator: CFAllocator?, _ attributes: CFArray?, _ resolvedDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

This call is useful when you need to resolve requirements between several potential clients of a buffer.

If two or more dictionaries contain the same key but different values, this function adjusts values where possible so that the output dictionary contains a mutually compatible set of values. For example, if the `attributes` parameter contains dictionaries whose bytes-per-row attributes differ, the `rowBytes` value in the output dictionary is the least common multiple of the input values.

Some mismatched attributes cannot be resolved. Calling this function results in an error if the widths, heights, pixel format allocators, or callbacks in the input dictionaries do not match.

## Parameters

- `allocator`: The allocator to use to create the pixel buffer. Pass   to specify the default allocator.
- `attributes`: An array of Core Foundation dictionaries containing pixel buffer attribute key-value pairs.
- `resolvedDictionaryOut`: On output, the consolidated dictionary. Ownership follows the  .

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
- [func CVPixelBufferGetExtendedPixels(CVPixelBuffer, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<Int>?)](cvpixelbuffergetextendedpixels(_:_:_:_:_:).md)
  Returns the amount of extended pixel padding in the pixel buffer.
- [func CVPixelBufferGetIOSurface(CVPixelBuffer?) -> Unmanaged<IOSurfaceRef>?](cvpixelbuffergetiosurface(_:).md)
  Returns the IOSurface backing the pixel buffer, or `NULL` if it is not backed by an IOSurface.
- [func CVPixelBufferGetTypeID() -> CFTypeID](cvpixelbuffergettypeid().md)
  Returns the Core Foundation type identifier of the pixel buffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreateresolvedattributesdictionary(_:_:_:))*