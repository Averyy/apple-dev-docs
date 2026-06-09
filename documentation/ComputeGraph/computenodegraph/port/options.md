# ComputeNodeGraph.Port.Options

**Framework**: ComputeGraph  
**Kind**: struct

Flags that modify how a port’s value is treated during compilation and execution.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
struct Options
```

## Topics

### Type Properties
- [static let argument: ComputeNodeGraph.Port.Options](computenodegraph/port/options/argument.md)
  Port is an argument to a runtime function.
- [static let compile: ComputeNodeGraph.Port.Options](computenodegraph/port/options/compile.md)
  Port affects compilation.
- [static let constant: ComputeNodeGraph.Port.Options](computenodegraph/port/options/constant.md)
  Port is constant and doesn’t need to be changeable.
- [static let externalReference: ComputeNodeGraph.Port.Options](computenodegraph/port/options/externalreference.md)
  The port references a value outside of the graph, such as by filename
- [static let optional: ComputeNodeGraph.Port.Options](computenodegraph/port/options/optional.md)
  The value of this port is optional (may be nil)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/options)*