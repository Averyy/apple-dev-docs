# encodeRender(to:frameAttributes:sourceImage:sourceDisparity:destinationLuma:destinationChroma:)

**Framework**: Cinematic  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func encodeRender(to commandBuffer: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer, destinationLuma: any MTLTexture, destinationChroma: any MTLTexture) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationluma:destinationchroma:))*