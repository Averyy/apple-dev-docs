# CVPixelBufferUnlockBaseAddress(_:_:)

**Framework**: Core Video  
**Kind**: func

Unlocks the base address of the pixel buffer.

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
func CVPixelBufferUnlockBaseAddress(_ pixelBuffer: CVPixelBuffer, _ unlockFlags: CVPixelBufferLockFlags) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

You must call the [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) function before accessing pixel data with the CPU, and call the [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md) function afterward. If you include the [`readOnly`](cvpixelbufferlockflags/readonly.md) value in the `lockFlags` parameter when locking the buffer, you must also include it when unlocking the buffer.

> ❗ **Important**:  When accessing pixel data with the GPU, locking is not necessary and can impair performance.

## Parameters

- `pixelBuffer`: The pixel buffer whose base address you want to unlock.
- `unlockFlags`: Either   or  ; see   for discussion.

## See Also

- [func CVPixelBufferFillExtendedPixels(CVPixelBuffer) -> CVReturn](cvpixelbufferfillextendedpixels(_:).md)
  Fills the extended pixels of the pixel buffer.
- [func CVPixelBufferLockBaseAddress(CVPixelBuffer, CVPixelBufferLockFlags) -> CVReturn](cvpixelbufferlockbaseaddress(_:_:).md)
  Locks the base address of the pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferunlockbaseaddress(_:_:))*