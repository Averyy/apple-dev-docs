# encode(to:sourceTexture:regions:numberOfRegions:keypointCount:keypointCountBufferOffset:keypointDataBuffer:keypointDataBufferOffset:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: any MTLCommandBuffer, sourceTexture source: any MTLTexture, regions: UnsafePointer<MTLRegion>, numberOfRegions: Int, keypointCount keypointCountBuffer: any MTLBuffer, keypointCountBufferOffset: Int, keypointDataBuffer: any MTLBuffer, keypointDataBufferOffset: Int)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) source regions:(const MTLRegion *) regions numberOfRegions:(NSUInteger) numberOfRegions keypointCountBuffer:(id<MTLBuffer>) keypointCountBuffer keypointCountBufferOffset:(NSUInteger) keypointCountBufferOffset keypointDataBuffer:(id<MTLBuffer>) keypointDataBuffer keypointDataBufferOffset:(NSUInteger) keypointDataBufferOffset;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefindkeypoints/encode(to:sourcetexture:regions:numberofregions:keypointcount:keypointcountbufferoffset:keypointdatabuffer:keypointdatabufferoffset:))*