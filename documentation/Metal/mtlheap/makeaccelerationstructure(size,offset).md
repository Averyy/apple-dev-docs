# makeAccelerationStructure(size:offset:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeAccelerationStructure(size: Int, offset: Int) -> (any MTLAccelerationStructure)?
```

```objc
- (id<MTLAccelerationStructure>) newAccelerationStructureWithSize:(NSUInteger) size offset:(NSUInteger) offset;
```

## See Also

### Creating acceleration structure from a heap
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](./makeaccelerationstructure%28size%29.md)
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](./makeaccelerationstructure%28descriptor%29.md)
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor, offset: Int) -> (any MTLAccelerationStructure)?](./makeaccelerationstructure%28descriptor,offset%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/makeaccelerationstructure(size:offset:))*