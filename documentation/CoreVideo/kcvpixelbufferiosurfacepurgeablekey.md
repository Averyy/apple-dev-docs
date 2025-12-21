# kCVPixelBufferIOSurfacePurgeableKey

**Framework**: Core Video  
**Kind**: var

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 26.0+
- watchOS 8.0+

## Declaration

```swift
let kCVPixelBufferIOSurfacePurgeableKey: CFString
```

#### Discussion

Key sets the IOSurface backed memory allocation for CVPixelBuffer as purgable and volatile.

A purgeable IOSurface is capable of being switched between non-volatile, volatile and empty states using IOSurfaceSetPurgeable.  When in the volatile state, the OS is permitted to instantly change its state to empty and remove all its memory pages.  Clients should set the IOSurfaces to the non-volatile state while they are in use and the volatile state when their need and contents is optional/speculative and OK to discard in response to system memory demand.  See IOSurfaceSetPurgeable for more details.  This key is only effective for CVPixelBuffers that are backed by IOSurface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfacepurgeablekey)*