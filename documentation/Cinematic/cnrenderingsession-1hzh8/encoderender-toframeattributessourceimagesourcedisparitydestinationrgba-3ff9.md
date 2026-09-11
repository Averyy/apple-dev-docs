# encodeRender(to:frameAttributes:sourceImage:sourceDisparity:destinationRGBA:)

**Framework**: Cinematic  
**Kind**: method

Encode a command to render a shallow depth of field (SDoF) image to a metal texture as RGBA.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func encodeRender(to commandBuffer: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer, destinationRGBA: any MTLTexture) -> Bool
```

#### Return Value

Whether encoding the render command was successful

## Parameters

- `commandBuffer`: The metal command buffer on which to encode the command
- `frameAttributes`: Controls the focus distance and aperture of the rendering
- `sourceImage`: A pixel buffer read from the cinematicVideoTrack
- `sourceDisparity`: A pixel buffer read from the cinematicDisparityTrack
- `destinationRGBA`: A metal texture to which the SDoF image is rendered in RGBA format


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationrgba:)-3ff9)*