# ProcessCodeRequirement

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A lightweight code requirement that you use to evaluate a running process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct ProcessCodeRequirement
```

#### Overview

[`ProcessCodeRequirement`](processcoderequirement.md) objects can only be built using constraints that conform to the [`ProcessConstraint`](processconstraint.md) protocol.

## Topics

### Initializers
- [init(OnDiskCodeRequirement) throws](processcoderequirement/init(_:)-1va02.md)
  Convert an [`OnDiskCodeRequirement`](ondiskcoderequirement.md) to a [`ProcessCodeRequirement`](processcoderequirement.md) if possible.
- [init(LaunchCodeRequirement) throws](processcoderequirement/init(_:)-4gkz2.md)
  Convert a [`LaunchCodeRequirement`](launchcoderequirement.md) to a [`ProcessCodeRequirement`](processcoderequirement.md) if possible.
- [init(from: any Decoder) throws](processcoderequirement/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](processcoderequirement/encode(to:).md)
  Encodes this value into the given encoder
### Type Methods
- [static func allOf(requirement: () -> [any ProcessConstraint]) throws -> ProcessCodeRequirement](processcoderequirement/allof(requirement:).md)
  Create a [`ProcessCodeRequirement`](processcoderequirement.md) that requires matching all of the provided constraints.
- [static func anyOf(requirement: () -> [any ProcessConstraint]) throws -> ProcessCodeRequirement](processcoderequirement/anyof(requirement:).md)
  Create a [`ProcessCodeRequirement`](processcoderequirement.md) that requires matching any of the provided constraints.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool](sectaskvalidateforrequirement(task:requirement:).md)
  Tests whether a task’s executable satisfies a lightweight code requirement.
- [func allOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](allof(requirement:)-4k3ay.md)
  Creates a constraint that requires a running process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](anyof(requirement:)-vwhn.md)
  Creates a constraint that requires a running process’s executable to satisfy any of the provided constraints.
- [protocol ProcessConstraint](processconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.
- [struct ProcessCodeSigningFlags](processcodesigningflags.md)
  A constraint that matches the current code-signing flags of a process.
- [struct ProcessConstraintBuilder](processconstraintbuilder.md)
  A custom parameter attribute that constructs process constraints from closures.
- [struct TeamIdentifierMatchesCurrentProcess](teamidentifiermatchescurrentprocess.md)
  A constraint that matches if a process has the same team identifier as the calling process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcoderequirement)*