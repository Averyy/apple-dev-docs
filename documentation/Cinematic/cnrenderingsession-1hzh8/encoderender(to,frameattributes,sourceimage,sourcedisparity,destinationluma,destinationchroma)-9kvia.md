# encodeRender(to:frameAttributes:sourceImage:sourceDisparity:destinationLuma:destinationChroma:)

**Framework**: Cinematic  
**Kind**: method

Encode a command to render a shallow depth of field (SDoF) image to two metal textures as luma and chroma.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func encodeRender(to commandBuffer: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer, destinationLuma: any MTLTexture, destinationChroma: any MTLTexture) -> Bool
```

#### Return Value

Whether encoding the render command was successful

## Parameters

- `commandBuffer`: The metal command buffer on which to encode the command
- `frameAttributes`: Controls the focus distance and aperture of the rendering
- `sourceImage`: A pixel buffer read from the cinematicVideoTrack
- `sourceDisparity`: A pixel buffer read from the cinematicDisparityTrack
- `destinationLuma`: A metal texture to which the luma of the SDoF image is rendered
- `destinationChroma`: A metal texture to which the chroma of the SDoF image is rendered


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationluma:destinationchroma:)-9kvia)*