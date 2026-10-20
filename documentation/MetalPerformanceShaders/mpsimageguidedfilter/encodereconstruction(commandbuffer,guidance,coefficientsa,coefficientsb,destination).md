# encodeReconstruction(commandBuffer:guidance:coefficientsA:coefficientsB:destination:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- macOS 10.15.4+
- tvOS 13.2+
- visionOS 1.0+

## Declaration

```swift
func encodeReconstruction(commandBuffer: any MTLCommandBuffer, guidance guidanceTexture: any MTLTexture, coefficientsA coefficientsTextureA: any MTLTexture, coefficientsB coefficientsTextureB: any MTLTexture, destination destinationTexture: any MTLTexture)
```

```objc
- (void) encodeReconstructionToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer guidanceTexture:(id<MTLTexture>) guidanceTexture coefficientsTextureA:(id<MTLTexture>) coefficientsTextureA coefficientsTextureB:(id<MTLTexture>) coefficientsTextureB destinationTexture:(id<MTLTexture>) destinationTexture;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageguidedfilter/encodereconstruction(commandbuffer:guidance:coefficientsa:coefficientsb:destination:))*