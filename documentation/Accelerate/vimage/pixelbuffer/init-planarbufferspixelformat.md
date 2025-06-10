# init(planarBuffers:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init

Returns an initialized buffer by copying the specified planar buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(planarBuffers: [vImage.PixelBuffer<Format.PlanarPixelFormat>], pixelFormat: Format.Type = Format.self)
```

#### Discussion

> **Note**:  The number of planar buffers must equal the `Format.planeCount`. All planar buffers must be the same size.

## Parameters

- `planarBuffers`: An array that contains the source planar buffers.
- `pixelFormat`: The pixel format of the initialized buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(planarbuffers:pixelformat:))*