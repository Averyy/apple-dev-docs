# encode(to:sourceTexture:minmaxTexture:histogram:histogramOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, minmaxTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) source minmaxTexture:(id<MTLTexture>) minmaxTexture histogram:(id<MTLBuffer>) histogram histogramOffset:(NSUInteger) histogramOffset;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagenormalizedhistogram/encode(to:sourcetexture:minmaxtexture:histogram:histogramoffset:))*