# makeAccelerationStructureCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a ray-tracing acceleration structure command encoder that uses default settings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeAccelerationStructureCommandEncoder() -> (any MTLAccelerationStructureCommandEncoder)?
```

#### Discussion

Use an [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) instance’s methods to set up a single ray-tracing pass.

## See Also

- [func makeAccelerationStructureCommandEncoder(descriptor: MTLAccelerationStructurePassDescriptor) -> any MTLAccelerationStructureCommandEncoder](mtlcommandbuffer/makeaccelerationstructurecommandencoder(descriptor:).md)
  Creates a ray-tracing acceleration structure command encoder from a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder())*