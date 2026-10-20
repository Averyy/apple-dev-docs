# makeComputeCommandEncoder(dispatchType:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLComputeCommandEncoder>) computeCommandEncoderWithDispatchType:(MTLDispatchType) dispatchType;
```

#### Discussion

Use an [`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass.

## Parameters

- `dispatchType`: An [`MTLDispatchType`](../mtldispatchtype.md) instance that indicates whether the compute pass the encoder creates runs commands serially or concurrently.

## See Also

### Creating compute encoders
- [func makeComputeCommandEncoder(descriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?](./makecomputecommandencoder%28descriptor%29.md)
  Creates a compute command encoder from a descriptor.
- [func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?](./makecomputecommandencoder%28%29.md)
  Creates a compute command encoder that uses default settings.
- [enum MTLDispatchType](../mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(dispatchtype:))*