# ComputeNodeGraph.Port.Options

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Flags that modify how a port’s value is treated during compilation and execution.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct Options
```

## Topics

### Type Properties
- [static let argument: ComputeNodeGraph.Port.Options](./options/argument.md)
  Port is an argument to a runtime function.
- [static let compile: ComputeNodeGraph.Port.Options](./options/compile.md)
  Port affects compilation.
- [static let constant: ComputeNodeGraph.Port.Options](./options/constant.md)
  Port is constant and doesn’t need to be changeable.
- [static let externalReference: ComputeNodeGraph.Port.Options](./options/externalreference.md)
  The port references a value outside of the graph, such as by filename
- [static let optional: ComputeNodeGraph.Port.Options](./options/optional.md)
  The value of this port is optional (may be nil)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/options)*