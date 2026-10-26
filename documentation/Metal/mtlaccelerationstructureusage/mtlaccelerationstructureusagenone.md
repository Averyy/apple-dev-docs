# MTLAccelerationStructureUsageNone

**Framework**: Metal  
**Kind**: case  
**Role**: Enumeration Case

A sentinel value the represents an empty set of options, which is the default behavior for building new acceleration structures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```c
MTLAccelerationStructureUsageNone
```

## See Also

### Applying options
- [static var refit: MTLAccelerationStructureUsage](./refit.md)
  An option that lets you update an acceleration structure after creating it.
- [static var preferFastBuild: MTLAccelerationStructureUsage](./preferfastbuild.md)
  An option that instructs Metal to build an acceleration structure quickly.
- [static var preferFastIntersection: MTLAccelerationStructureUsage](./preferfastintersection.md)
  An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [static var minimizeMemory: MTLAccelerationStructureUsage](./minimizememory.md)
  An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [static var extendedLimits: MTLAccelerationStructureUsage](./extendedlimits.md)
  An option that increases an acceleration structure’s storage capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/mtlaccelerationstructureusagenone)*