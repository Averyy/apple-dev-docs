# CVPixelBufferCreateResolvedAttributesDictionary(_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

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

```c
extern CVReturn CVPixelBufferCreateResolvedAttributesDictionary(CFAllocatorRef allocator, CFArrayRef attributes, CFDictionaryRef*resolvedDictionaryOut);
```

## Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

## Discussion

This call is useful when you need to resolve requirements between several potential clients of a buffer.

If two or more dictionaries contain the same key but different values, this function adjusts values where possible so that the output dictionary contains a mutually compatible set of values. For example, if the `attributes` parameter contains dictionaries whose bytes-per-row attributes differ, the `rowBytes` value in the output dictionary is the least common multiple of the input values.

Some mismatched attributes cannot be resolved. Calling this function results in an error if the widths, heights, pixel format allocators, or callbacks in the input dictionaries do not match.

## Parameters

- `allocator`: The allocator to use to create the pixel buffer. Pass `NULL` to specify the default allocator.
- `attributes`: An array of Core Foundation dictionaries containing pixel buffer attribute key-value pairs.
- `resolvedDictionaryOut`: On output, the consolidated dictionary. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

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
- [func CVPixelBufferIsCompatibleWithAttributes(CVPixelBuffer, CFDictionary?) -> Bool](./cvpixelbufferiscompatiblewithattributes%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreateresolvedattributesdictionary(_:_:_:))*