# extendedLimits

**Framework**: Metal  
**Kind**: property

A structure usage option that indicates you intend to use larger ray-tracing limits for the acceleration structure.

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

Metal may make performance tradeoffs so that the acceleration structure can support more complex data structures.

|  | Standard limits | Extended limits |
| --- | --- | --- |
| Primitives in primitive acceleration structure | `2^(28)` | `2^(30)` |
| Geometries in primitive acceleration structure | `2^(24)` | `2^(30)` |
| Instances in instance acceleration structure | `2^(24)` | `2^(30)` |
| Visibility mask bits | `8` | `32` |

## See Also

- [static var refit: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/refit.md)
  An option that specifies that you can refit the acceleration structure if the geometry changes.
- [static var preferFastBuild: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastbuild.md)
  An option that specifies that Metal needs to build the acceleration structure quickly, even if that reduces ray-tracing performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/extendedlimits)*