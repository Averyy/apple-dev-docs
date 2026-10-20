# encodeIntersection(commandBuffer:intersectionType:rayBuffer:rayBufferOffset:rayIndexBuffer:rayIndexBufferOffset:intersectionBuffer:intersectionBufferOffset:rayIndexCountBuffer:rayIndexCountBufferOffset:accelerationStructure:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+ - Deprecated in 17.0
- iPadOS 13.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.15+ - Deprecated in 14.0
- tvOS 13.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func encodeIntersection(commandBuffer: any MTLCommandBuffer, intersectionType: MPSIntersectionType, rayBuffer: any MTLBuffer, rayBufferOffset: Int, rayIndexBuffer: any MTLBuffer, rayIndexBufferOffset: Int, intersectionBuffer: any MTLBuffer, intersectionBufferOffset: Int, rayIndexCountBuffer: any MTLBuffer, rayIndexCountBufferOffset: Int, accelerationStructure: MPSAccelerationStructure)
```

```objc
- (void) encodeIntersectionToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer intersectionType:(MPSIntersectionType) intersectionType rayBuffer:(id<MTLBuffer>) rayBuffer rayBufferOffset:(NSUInteger) rayBufferOffset rayIndexBuffer:(id<MTLBuffer>) rayIndexBuffer rayIndexBufferOffset:(NSUInteger) rayIndexBufferOffset intersectionBuffer:(id<MTLBuffer>) intersectionBuffer intersectionBufferOffset:(NSUInteger) intersectionBufferOffset rayIndexCountBuffer:(id<MTLBuffer>) rayIndexCountBuffer rayIndexCountBufferOffset:(NSUInteger) rayIndexCountBufferOffset accelerationStructure:(MPSAccelerationStructure *) accelerationStructure;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrayintersector/encodeintersection(commandbuffer:intersectiontype:raybuffer:raybufferoffset:rayindexbuffer:rayindexbufferoffset:intersectionbuffer:intersectionbufferoffset:rayindexcountbuffer:rayindexcountbufferoffset:accelerationstructure:))*