# MTLHazardTrackingMode

**Framework**: Metal  
**Kind**: enum

The options you use to specify the hazard tracking mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLHazardTrackingMode
```

## Topics

### Specifying the Tracking Mode
- [MTLHazardTrackingMode.default](mtlhazardtrackingmode/default.md)
  An option specifying that the default tracking mode should be used.
- [MTLHazardTrackingMode.untracked](mtlhazardtrackingmode/untracked.md)
  An option specifying that the app must prevent hazards when modifying this object’s contents.
- [MTLHazardTrackingMode.tracked](mtlhazardtrackingmode/tracked.md)
  An option specifying that Metal prevents hazards when modifying this object’s contents.
### Initializers
- [init?(rawValue: UInt)](mtlhazardtrackingmode/init(rawvalue:).md)

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
- [enum MTLStorageMode](mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlhazardtrackingmode)*