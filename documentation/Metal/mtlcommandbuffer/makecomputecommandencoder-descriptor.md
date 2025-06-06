# makeComputeCommandEncoder(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a compute command encoder from a descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func makeComputeCommandEncoder(descriptor computePassDescriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?
```

#### Discussion

Use an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass.

## Parameters

- `computePassDescriptor`: An   instance that configures the   the method returns.

## See Also

- [func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder.md)
  Creates a compute command encoder that uses default settings.
- [func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder(dispatchtype:).md)
  Creates a compute command encoder with a dispatch type.
- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(descriptor:))*