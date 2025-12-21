# preferFastIntersection

**Framework**: Metal  
**Kind**: property

An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var preferFastIntersection: MTLAccelerationStructureUsage { get }
```

#### Discussion

The acceleration structures you build with this option can increase their build times.

## See Also

- [static var refit: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/refit.md)
  An option that lets you update an acceleration structure after creating it.
- [static var preferFastBuild: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastbuild.md)
  An option that instructs Metal to build an acceleration structure quickly.
- [static var minimizeMemory: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/minimizememory.md)
  An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [static var extendedLimits: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/extendedlimits.md)
  An option that increases an acceleration structure’s storage capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/preferfastintersection)*