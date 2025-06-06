# preferFastBuild

**Framework**: Metal  
**Kind**: property

An option that specifies that Metal needs to build the acceleration structure quickly, even if that reduces ray-tracing performance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var preferFastBuild: MTLAccelerationStructureUsage { get }
```

#### Discussion

Typically, you specify this option for acceleration structures that you need to create or refit inside performance-sensitive code.

## See Also

- [static var refit: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/refit.md)
  An option that specifies that you can refit the acceleration structure if the geometry changes.
- [static var extendedLimits: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/extendedlimits.md)
  A structure usage option that indicates you intend to use larger ray-tracing limits for the acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/preferfastbuild)*