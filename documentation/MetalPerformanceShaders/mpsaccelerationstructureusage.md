# MPSAccelerationStructureUsage

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

Options that describe how an acceleration structure will be used.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
struct MPSAccelerationStructureUsage
```

```c
enum MPSAccelerationStructureUsage : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./mpsaccelerationstructureusage/init%28rawvalue%29.md)
### Type Properties
- [static var frequentRebuild: MPSAccelerationStructureUsage](./mpsaccelerationstructureusage/frequentrebuild.md)
  Option indicating that the acceleration structure will be rebuilt frequently.
- [static var preferCPUBuild: MPSAccelerationStructureUsage](./mpsaccelerationstructureusage/prefercpubuild.md)
- [static var preferGPUBuild: MPSAccelerationStructureUsage](./mpsaccelerationstructureusage/prefergpubuild.md)
- [static var refit: MPSAccelerationStructureUsage](./mpsaccelerationstructureusage/refit.md)
  Option that enables support for refitting the acceleration structure after it has been built.
### Enumeration Cases
- [MPSAccelerationStructureUsageNone](./mpsaccelerationstructureusage/mpsaccelerationstructureusagenone.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructureusage)*