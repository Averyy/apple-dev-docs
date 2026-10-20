# encode(to:sourceTexture:destinationTexture:endpointBuffer:endpointOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, destinationTexture dest: (any MTLTexture)?, endpointBuffer: any MTLBuffer, endpointOffset: Int)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) source destinationTexture:(id<MTLTexture>) dest endpointBuffer:(id<MTLBuffer>) endpointBuffer endpointOffset:(NSUInteger) endpointOffset;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedlines/encode(to:sourcetexture:destinationtexture:endpointbuffer:endpointoffset:))*