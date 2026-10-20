# encodeRegression(commandBuffer:source:guidance:weights:destinationCoefficientsA:destinationCoefficientsB:)

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
func encodeRegression(commandBuffer: any MTLCommandBuffer, source sourceTexture: any MTLTexture, guidance guidanceTexture: any MTLTexture, weights weightsTexture: (any MTLTexture)?, destinationCoefficientsA destinationCoefficientsTextureA: any MTLTexture, destinationCoefficientsB destinationCoefficientsTextureB: any MTLTexture)
```

```objc
- (void) encodeRegressionToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) sourceTexture guidanceTexture:(id<MTLTexture>) guidanceTexture weightsTexture:(id<MTLTexture>) weightsTexture destinationCoefficientsTextureA:(id<MTLTexture>) destinationCoefficientsTextureA destinationCoefficientsTextureB:(id<MTLTexture>) destinationCoefficientsTextureB;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageguidedfilter/encoderegression(commandbuffer:source:guidance:weights:destinationcoefficientsa:destinationcoefficientsb:))*