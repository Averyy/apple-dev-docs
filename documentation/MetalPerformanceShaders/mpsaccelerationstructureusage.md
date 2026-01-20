# MPSAccelerationStructureUsage

**Framework**: Metal Performance Shaders  
**Kind**: struct

Options that describe how an acceleration structure will be used.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSAccelerationStructureUsage
```

## Topics

### Initializers
- [init(rawValue: UInt)](mpsaccelerationstructureusage/init(rawvalue:).md)
### Type Properties
- [static var frequentRebuild: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/frequentrebuild.md)
  Option indicating that the acceleration structure will be rebuilt frequently.
- [static var preferCPUBuild: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/prefercpubuild.md)
- [static var preferGPUBuild: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/prefergpubuild.md)
- [static var refit: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/refit.md)
  Option that enables support for refitting the acceleration structure after it has been built.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructureusage)*