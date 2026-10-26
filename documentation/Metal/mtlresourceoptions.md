# MTLResourceOptions

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

Optional arguments used to set the behavior of a resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct MTLResourceOptions
```

```c
enum MTLResourceOptions : NSUInteger;
```

## Mentions

- [Setting resource storage modes](./setting-resource-storage-modes.md)

## Topics

### Initializing resource options
- [init(rawValue: UInt)](./mtlresourceoptions/init%28rawvalue%29.md)
### Specifying CPU cache modes
- [static var cpuCacheModeWriteCombined: MTLResourceOptions](./mtlresourceoptions/cpucachemodewritecombined.md)
  A write-combined CPU cache mode that is optimized for resources that the CPU writes into, but never reads.
- [MTLResourceCPUCacheModeDefaultCache](./mtlresourceoptions/mtlresourcecpucachemodedefaultcache.md)
  The default CPU cache mode for the resource, which guarantees that read and write operations are executed in the expected order.
### Specifying storage modes
- [static var storageModeShared: MTLResourceOptions](./mtlresourceoptions/storagemodeshared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [static var storageModeManaged: MTLResourceOptions](./mtlresourceoptions/storagemodemanaged.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.
- [static var storageModePrivate: MTLResourceOptions](./mtlresourceoptions/storagemodeprivate.md)
  The resource is only available to the GPU.
- [static var storageModeMemoryless: MTLResourceOptions](./mtlresourceoptions/storagemodememoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
### Specifying hazard tracking
- [static var hazardTrackingModeTracked: MTLResourceOptions](./mtlresourceoptions/hazardtrackingmodetracked.md)
  An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.
- [static var hazardTrackingModeUntracked: MTLResourceOptions](./mtlresourceoptions/hazardtrackingmodeuntracked.md)
  A resource option that instructs Metal to ignore memory hazards for a resource at runtime.
- [MTLResourceHazardTrackingModeDefault](./mtlresourceoptions/mtlresourcehazardtrackingmodedefault.md)
  An option specifying that the default tracking mode should be used.
### Deprecated options
- [static var optionCPUCacheModeWriteCombined: MTLResourceOptions](./mtlresourceoptions/optioncpucachemodewritecombined.md)
  This constant was deprecated in iOS 9.0 and macOS 10.11.
- [MTLResourceOptionCPUCacheModeDefault](./mtlresourceoptions/mtlresourceoptioncpucachemodedefault.md)
  This constant was deprecated in iOS 9.0 and macOS 10.11.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Common resource functionality
- [typealias MTLGPUAddress](./mtlgpuaddress.md)
  A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [protocol MTLAllocation](./mtlallocation.md)
  A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [protocol MTLResource](./mtlresource.md)
  An allocation of memory accessible to a GPU.
- [struct MTLResourceUsage](./mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [struct MTLResourceID](./mtlresourceid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions)*