# ProcessCodeSigningFlags

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that matches the current code-signing flags of a process.

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
struct ProcessCodeSigningFlags
```

## Topics

### Structures
- [ProcessCodeSigningFlags.ValueSet](processcodesigningflags/valueset.md)
  Code signing flags that can be set on a process
### Initializers
- [init(from: any Decoder) throws](processcodesigningflags/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](processcodesigningflags/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [ProcessCodeSigningFlags.DataType](processcodesigningflags/datatype.md)
  The basic input data type for this constraint: `ProcessCodeSigningFlags.ValueSet`
- [ProcessCodeSigningFlags.OutType](processcodesigningflags/outtype.md)
  The type of this constraint: [`ProcessCodeSigningFlags`](processcodesigningflags.md)
### Type Methods
- [static func isSuperset(of: ProcessCodeSigningFlags.DataType) -> ProcessCodeSigningFlags.OutType](processcodesigningflags/issuperset(of:).md)
  Matches when the code signing flags on the process are a superset of the specified flags.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [LaunchConstraint](launchconstraint.md)
- [ProcessConstraint](processconstraint.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct ProcessConstraintBuilder](processconstraintbuilder.md)
  A custom parameter attribute that constructs process constraints from closures.
- [struct TeamIdentifierMatchesCurrentProcess](teamidentifiermatchescurrentprocess.md)
  A constraint that matches if a process has the same team identifier as the calling process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags)*