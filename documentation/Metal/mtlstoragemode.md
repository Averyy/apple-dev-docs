# MTLStorageMode

**Framework**: Metal  
**Kind**: enum

Options for the memory location and access permissions for a resource.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLStorageMode
```

## Mentions

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)

#### Overview

For more guidance on how to choose storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

## Topics

### Storage Mode Options
- [MTLStorageMode.shared](mtlstoragemode/shared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageMode.managed](mtlstoragemode/managed.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes must be explicitly synchronized.
- [MTLStorageMode.private](mtlstoragemode/private.md)
  The resource is only available to the GPU.
- [MTLStorageMode.memoryless](mtlstoragemode/memoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
### Initializers
- [init?(rawValue: UInt)](mtlstoragemode/init(rawvalue:).md)

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
- [enum MTLCPUCacheMode](mtlcpucachemode.md)
  Options for the CPU cache mode that define the CPU mapping of the resource.
- [enum MTLHazardTrackingMode](mtlhazardtrackingmode.md)
  The options you use to specify the hazard tracking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode)*