# init(unsafeBacking:matching:)

**Framework**: Core Video  
**Kind**: init

Creates a CVPixelBuffer backed by the given `ioSurface`. The CVPixelBuffer will retain the `ioSurface`.  If you are using IOSurface to share CVPixelBuffers between processes and those CVPixelBuffers are allocated via a CVPixelBufferPool, it is important that the CVPixelBufferPool does not reuse CVPixelBuffers whose IOSurfaces are still in use in other processes. CoreVideo and IOSurface will take care of this for if you use IOSurfaceCreateMachPort and IOSurfaceLookupFromMachPort, but NOT if you pass IOSurfaceIDs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(unsafeBacking ioSurface: IOSurface, matching attributes: CVPixelBufferCreationAttributes) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/init(unsafebacking:matching:))*