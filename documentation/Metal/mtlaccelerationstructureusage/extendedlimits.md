# extendedLimits

**Framework**: Metal  
**Kind**: property

An option that increases an acceleration structure’s storage capacity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var extendedLimits: MTLAccelerationStructureUsage { get }
```

#### Discussion

The acceleration structures you build with this option can affect their performance because they support more data complexity.

|  | Standard limits | Extended limits |
| --- | --- | --- |
| Primitives in primitive acceleration structure | `2^(28)` | `2^(30)` |
| Geometries in primitive acceleration structure | `2^(24)` | `2^(30)` |
| Instances in instance acceleration structure | `2^(24)` | `2^(30)` |
| Visibility mask bits | `8` | `32` |

## See Also

- [static var refit: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/refit.md)
  An option that lets you update an acceleration structure after creating it.
- [static var preferFastBuild: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastbuild.md)
  An option that instructs Metal to build an acceleration structure quickly.
- [static var preferFastIntersection: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastintersection.md)
  An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [static var minimizeMemory: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/minimizememory.md)
  An option that instructs Metal to prioritize building an acceleration structure that needs less memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/extendedlimits)*