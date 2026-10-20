# encodeIntersection(commandBuffer:intersectionType:rayBuffer:rayBufferOffset:intersectionBuffer:intersectionBufferOffset:rayCount:accelerationStructure:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayCount: Int, accelerationStructure: MPSAccelerationStructure)
```

```objc
- (void) encodeIntersectionToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer intersectionType:(MPSIntersectionType) intersectionType rayBuffer:(id<MTLBuffer>) rayBuffer rayBufferOffset:(NSUInteger) rayBufferOffset intersectionBuffer:(id<MTLBuffer>) intersectionBuffer intersectionBufferOffset:(NSUInteger) intersectionBufferOffset rayCount:(NSUInteger) rayCount accelerationStructure:(MPSAccelerationStructure *) accelerationStructure;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raybuffer:raybufferoffset:intersectionbuffer:intersectionbufferoffset:raycount:accelerationstructure:))*