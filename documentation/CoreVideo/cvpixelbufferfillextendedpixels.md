# CVPixelBufferFillExtendedPixels(_:)

**Framework**: Core Video  
**Kind**: func

Fills the extended pixels of the pixel buffer.

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
func CVPixelBufferFillExtendedPixels(_ pixelBuffer: CVPixelBuffer) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

This function replicates edge pixels to fill the entire extended region of the image.

## Parameters

- `pixelBuffer`: The pixel buffer whose extended pixels you want to fill.

## See Also

- [func CVPixelBufferLockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](cvpixelbufferlockbaseaddress(_:_:).md)
  Locks the base address of the pixel buffer.
- [func CVPixelBufferUnlockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](cvpixelbufferunlockbaseaddress(_:_:).md)
  Unlocks the base address of the pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferfillextendedpixels(_:))*