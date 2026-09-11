# encodeRender(to:frameAttributes:sourceImage:sourceDisparity:destinationImage:)

**Framework**: Cinematic  
**Kind**: method

Encode a command to render a shallow depth of field (SDoF) image to a pixel buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst ?+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
func encodeRender(to commandBuffer: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVReadOnlyPixelBuffer, sourceDisparity: CVReadOnlyPixelBuffer? = nil, destinationImage: CVPixelBuffer) -> Bool
```

#### Return Value

Whether encoding the render command was successful

## Parameters

- `commandBuffer`: The metal command buffer on which to encode the command
- `frameAttributes`: Controls the focus distance and aperture of the rendering
- `sourceImage`: A pixel buffer read from the cinematicVideoTrack
- `sourceDisparity`: A pixelbuffer with disparity. Can be nil only when preview rendering of assets before preprocessing (CNAssetInfo.cinematicCapability == .needsPreprocessing). When nil the source disparity and frameAttributes.focusDisparity will be computed internally. Passing nil for other types of assets will return false.
- `destinationImage`: The pixel buffer to which the SDoF image is rendered


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationimage:)-3rknf)*