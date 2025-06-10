# MTLCPUCacheMode

**Framework**: Metal  
**Kind**: enum

Options for the CPU cache mode that define the CPU mapping of the resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLCPUCacheMode
```

## Topics

### Specifying the Cache Mode
- [MTLCPUCacheMode.defaultCache](mtlcpucachemode/defaultcache.md)
  The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.
- [MTLCPUCacheMode.writeCombined](mtlcpucachemode/writecombined.md)
  A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.
### Initializers
- [init?(rawValue: UInt)](mtlcpucachemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cpuCacheMode: MTLCPUCacheMode](mtlresource/cpucachemode.md)
  The CPU cache mode that defines the CPU mapping of the resource.
- [var storageMode: MTLStorageMode](mtlresource/storagemode.md)
  The location and access permissions of the resource.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlresource/hazardtrackingmode.md)
  A mode that determines whether Metal tracks and synchronizes resource access.
- [var resourceOptions: MTLResourceOptions](mtlresource/resourceoptions.md)
  The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [enum MTLStorageMode](mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.
- [enum MTLHazardTrackingMode](mtlhazardtrackingmode.md)
  The options you use to specify the hazard tracking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcpucachemode)*