# TeamIdentifierMatchesCurrentProcess

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

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
- [init()](./teamidentifiermatchescurrentprocess/init%28%29.md)
  Creates a constraint that matches the current process’s team identifier.
- [init(Bool)](./teamidentifiermatchescurrentprocess/init%28_%29.md)
  Creates a constraint that tests whether a process’s team identifier matches the current process’s team identifier.
- [init(from: any Decoder) throws](./teamidentifiermatchescurrentprocess/init%28from%29.md)
  Create a new constraint by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](./teamidentifiermatchescurrentprocess/encode%28to%29.md)
  Encodes this constraint into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [ProcessConstraint](./processconstraint.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking code requirements for running processes
- [func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool](./sectaskvalidateforrequirement%28task,requirement%29.md)
  Tests whether a task’s executable satisfies a lightweight code requirement.
- [struct ProcessCodeRequirement](./processcoderequirement.md)
  A lightweight code requirement that you use to evaluate a running process.
- [func allOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](./allof%28requirement%29-4k3ay.md)
  Creates a constraint that requires a running process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](./anyof%28requirement%29-vwhn.md)
  Creates a constraint that requires a running process’s executable to satisfy any of the provided constraints.
- [protocol ProcessConstraint](./processconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.
- [struct ProcessCodeSigningFlags](./processcodesigningflags.md)
  A constraint that matches the current code-signing flags of a process.
- [struct ProcessConstraintBuilder](./processconstraintbuilder.md)
  A custom parameter attribute that constructs process constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/teamidentifiermatchescurrentprocess)*