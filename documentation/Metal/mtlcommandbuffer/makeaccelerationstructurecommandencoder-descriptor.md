# makeAccelerationStructureCommandEncoder(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a ray-tracing acceleration structure command encoder from a descriptor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeAccelerationStructureCommandEncoder(descriptor: MTLAccelerationStructurePassDescriptor) -> any MTLAccelerationStructureCommandEncoder
```

#### Discussion

Use an [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) instance’s methods to set up a single ray-tracing pass.

## Parameters

- `descriptor`: An   instance that configures the   the method returns.

## See Also

- [func makeAccelerationStructureCommandEncoder() -> (any MTLAccelerationStructureCommandEncoder)?](mtlcommandbuffer/makeaccelerationstructurecommandencoder.md)
  Creates a ray-tracing acceleration structure command encoder that uses default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder(descriptor:))*