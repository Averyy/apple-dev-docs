# makeComputeCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a compute command encoder that uses default settings.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?
```

```objc
- (id<MTLComputeCommandEncoder>) computeCommandEncoder;
```

## Discussion

Use an [`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass. The encoder this method returns dispatches its compute commands serially (see [`MTLDispatchType.serial`](../mtldispatchtype/serial.md)). To create a compute command encoder that dispatches commands concurrently (see [`MTLDispatchType.concurrent`](../mtldispatchtype/concurrent.md)), use the [`makeComputeCommandEncoder(dispatchType:)`](./makecomputecommandencoder%28dispatchtype%29.md) or [`makeComputeCommandEncoder(descriptor:)`](./makecomputecommandencoder%28descriptor%29.md) method.

## See Also

### Creating compute encoders
- [func makeComputeCommandEncoder(descriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?](./makecomputecommandencoder%28descriptor%29.md)
  Creates a compute command encoder from a descriptor.
- [func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?](./makecomputecommandencoder%28dispatchtype%29.md)
  Creates a compute command encoder with a dispatch type.
- [enum MTLDispatchType](../mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder())*