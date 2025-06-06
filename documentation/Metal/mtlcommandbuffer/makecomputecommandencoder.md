# makeComputeCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a compute command encoder that uses default settings.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?
```

#### Discussion

Use an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass. The encoder this method returns dispatches its compute commands serially (see [`MTLDispatchType.serial`](mtldispatchtype/serial.md)). To create a compute command encoder that dispatches commands concurrently (see [`MTLDispatchType.concurrent`](mtldispatchtype/concurrent.md)), use the [`makeComputeCommandEncoder(dispatchType:)`](mtlcommandbuffer/makecomputecommandencoder(dispatchtype:).md) or [`makeComputeCommandEncoder(descriptor:)`](mtlcommandbuffer/makecomputecommandencoder(descriptor:).md) method.

## See Also

- [func makeComputeCommandEncoder(descriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder(descriptor:).md)
  Creates a compute command encoder from a descriptor.
- [func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder(dispatchtype:).md)
  Creates a compute command encoder with a dispatch type.
- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder())*