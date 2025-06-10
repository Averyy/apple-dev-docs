# MTLDispatchType

**Framework**: Metal  
**Kind**: enum

The type of dispatch method to use when calling encoded functions.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLDispatchType
```

## Topics

### Execution Dispatch Types
- [MTLDispatchType.concurrent](mtldispatchtype/concurrent.md)
  Sets a command encoder to dispatch encoded commands concurrently during your pass.
- [MTLDispatchType.serial](mtldispatchtype/serial.md)
  Sets a command encoder to dispatch encoded commands serially during your pass.
### Initializers
- [init?(rawValue: UInt)](mtldispatchtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLComputePassDescriptor](mtlcomputepassdescriptor.md)
  A description of how to dispatch execution of pass commands and GPU performance sampling.
- [struct MTLDispatchThreadgroupsIndirectArguments](mtldispatchthreadgroupsindirectarguments.md)
  The data layout required for arguments needed to specify the size of threadgroups.
- [class MTLComputePassSampleBufferAttachmentDescriptor](mtlcomputepasssamplebufferattachmentdescriptor.md)
  A configuration that instructs the GPU where to store counter data from the beginning and end of a compute pass.
- [class MTLComputePassSampleBufferAttachmentDescriptorArray](mtlcomputepasssamplebufferattachmentdescriptorarray.md)
  A container that stores an array of sample buffer attachments for a compute pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldispatchtype)*