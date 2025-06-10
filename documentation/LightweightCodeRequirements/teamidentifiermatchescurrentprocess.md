# TeamIdentifierMatchesCurrentProcess

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that matches if a process has the same team identifier as the calling process.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TeamIdentifierMatchesCurrentProcess
```

## Topics

### Initializers
- [init()](teamidentifiermatchescurrentprocess/init.md)
  Creates a constraint that matches the current process’s team identifier.
- [init(Bool)](teamidentifiermatchescurrentprocess/init(_:).md)
  Creates a constraint that tests whether a process’s team identifier matches the current process’s team identifier.
- [init(from: any Decoder) throws](teamidentifiermatchescurrentprocess/init(from:).md)
  Create a new constraint by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](teamidentifiermatchescurrentprocess/encode(to:).md)
  Encodes this constraint into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [ProcessConstraint](processconstraint.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool](sectaskvalidateforrequirement(task:requirement:).md)
  Tests whether a task’s executable satisfies a lightweight code requirement.
- [struct ProcessCodeRequirement](processcoderequirement.md)
  A lightweight code requirement that you use to evaluate a running process.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/teamidentifiermatchescurrentprocess)*