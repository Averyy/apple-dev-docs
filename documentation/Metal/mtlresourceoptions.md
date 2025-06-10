# MTLResourceOptions

**Framework**: Metal  
**Kind**: struct

Optional arguments used to set the behavior of a resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct MTLResourceOptions
```

## Mentions

- [Setting Resource Storage Modes](setting-resource-storage-modes.md)

## Topics

### Initializing Resource Options
- [init(rawValue: UInt)](mtlresourceoptions/init(rawvalue:).md)
### Specifying CPU Cache Modes
- [static var cpuCacheModeWriteCombined: MTLResourceOptions](mtlresourceoptions/cpucachemodewritecombined.md)
  A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.
### Specifying Storage Modes
- [static var storageModeShared: MTLResourceOptions](mtlresourceoptions/storagemodeshared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [static var storageModeManaged: MTLResourceOptions](mtlresourceoptions/storagemodemanaged.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes must be explicitly synchronized.
- [static var storageModePrivate: MTLResourceOptions](mtlresourceoptions/storagemodeprivate.md)
  The resource is only available to the GPU.
- [static var storageModeMemoryless: MTLResourceOptions](mtlresourceoptions/storagemodememoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
### Specifying Hazard Tracking
- [static var hazardTrackingModeTracked: MTLResourceOptions](mtlresourceoptions/hazardtrackingmodetracked.md)
  An option specifying that Metal prevents hazards when modifying this object’s contents.
- [static var hazardTrackingModeUntracked: MTLResourceOptions](mtlresourceoptions/hazardtrackingmodeuntracked.md)
  An option specifying that the app must prevent hazards when modifying this object’s contents.
### Deprecated Options
- [static var optionCPUCacheModeWriteCombined: MTLResourceOptions](mtlresourceoptions/optioncpucachemodewritecombined.md)
  This constant was deprecated in iOS 9.0 and macOS 10.11.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [protocol MTLAllocation](mtlallocation.md)
  A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [protocol MTLResource](mtlresource.md)
  An allocation of memory accessible to a GPU.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [struct MTLResourceID](mtlresourceid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions)*