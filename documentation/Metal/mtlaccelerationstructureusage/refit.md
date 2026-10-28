# refit

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that lets you update an acceleration structure after creating it.

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

```c
MTLAccelerationStructureUsageRefit
```

## Discussion

Apply this option to make a modifiable acceleration structure, which you can update over time, such as for geometry changes. By default, the framework builds immutable acceleration structures for performance. When you apply the [`refit`](./refit.md) option, the framework builds an acceleration structure more conservatively, which can reduce its intersection performance.

> **Note**:  Refitting an acceleration structure generally works better when the geometry changes are relatively small.

## See Also

### Applying options
- [static var preferFastBuild: MTLAccelerationStructureUsage](./preferfastbuild.md)
  An option that instructs Metal to build an acceleration structure quickly.
- [static var preferFastIntersection: MTLAccelerationStructureUsage](./preferfastintersection.md)
  An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [static var minimizeMemory: MTLAccelerationStructureUsage](./minimizememory.md)
  An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [static var extendedLimits: MTLAccelerationStructureUsage](./extendedlimits.md)
  An option that increases an acceleration structure’s storage capacity.
- [MTLAccelerationStructureUsageNone](./mtlaccelerationstructureusagenone.md)
  A sentinel value the represents an empty set of options, which is the default behavior for building new acceleration structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/refit)*