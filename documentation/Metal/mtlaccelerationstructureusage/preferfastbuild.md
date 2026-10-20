# preferFastBuild

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that instructs Metal to build an acceleration structure quickly.

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

```c
MTLAccelerationStructureUsagePreferFastBuild
```

#### Discussion

Apply this option when you need to reduce the time when creating or refitting an acceleration structure, such as from code that’s sensitive to runtime performance.

> **Note**:  The acceleration structures you build with this option can reduce their intersection performance.

## See Also

### Applying options
- [static var refit: MTLAccelerationStructureUsage](./refit.md)
  An option that lets you update an acceleration structure after creating it.
- [static var preferFastIntersection: MTLAccelerationStructureUsage](./preferfastintersection.md)
  An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [static var minimizeMemory: MTLAccelerationStructureUsage](./minimizememory.md)
  An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [static var extendedLimits: MTLAccelerationStructureUsage](./extendedlimits.md)
  An option that increases an acceleration structure’s storage capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/preferfastbuild)*