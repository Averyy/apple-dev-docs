# init(device:venueDescriptor:depthPixelFormat:colorPixelFormat:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an immersive preview renderer.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
init(device: (any MTLDevice)? = nil, venueDescriptor: VenueDescriptor? = nil, depthPixelFormat: MTLPixelFormat? = nil, colorPixelFormat: MTLPixelFormat? = nil)
```

#### Discussion

The renderer is initialized with optional Metal device and pixel format configurations. If you don’t provide a device, the renderer uses the system default Metal device. You can set the venue descriptor during initialization or update it later through the [`venueDescriptor`](immersivepreviewrenderer/venuedescriptor.md) property.

## Parameters

- `device`: The `MTLDevice` to use.
- `venueDescriptor`: The `VenueDescriptor` to use to render the `ImmersiveVideoFrame`.
- `depthPixelFormat`: The depth pixel format to use.
- `colorPixelFormat`: The pixel format of the color attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivepreviewrenderer/init(device:venuedescriptor:depthpixelformat:colorpixelformat:))*