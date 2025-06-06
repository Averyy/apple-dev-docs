# refit

**Framework**: Metal  
**Kind**: property

An option that specifies that you can refit the acceleration structure if the geometry changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var refit: MTLAccelerationStructureUsage { get }
```

#### Discussion

By default, you can’t change an acceleration structure after you create it. Enabling this option allows you to update the acceleration structure if the geometry changes positions. Typically, for refits to work, the change to the geometry must be small.

Enabling this option require Metal to generate a more conservative acceleration structure, which can affect performance.

## See Also

- [static var preferFastBuild: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastbuild.md)
  An option that specifies that Metal needs to build the acceleration structure quickly, even if that reduces ray-tracing performance.
- [static var extendedLimits: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/extendedlimits.md)
  A structure usage option that indicates you intend to use larger ray-tracing limits for the acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/refit)*