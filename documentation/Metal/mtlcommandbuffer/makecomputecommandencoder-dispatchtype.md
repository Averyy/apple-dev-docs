# makeComputeCommandEncoder(dispatchType:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a compute command encoder with a dispatch type.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?
```

#### Discussion

Use an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass.

## Parameters

- `dispatchType`: An   instance that indicates whether the compute pass the encoder creates runs commands serially or concurrently.

## See Also

- [func makeComputeCommandEncoder(descriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder(descriptor:).md)
  Creates a compute command encoder from a descriptor.
- [func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder.md)
  Creates a compute command encoder that uses default settings.
- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(dispatchtype:))*