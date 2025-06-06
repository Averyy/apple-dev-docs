# ProcessConstraint

**Framework**: LightweightCodeRequirements  
**Kind**: protocol

A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.

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
protocol ProcessConstraint : Decodable, Encodable, Sendable
```

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [CodeDirectoryHash](codedirectoryhash.md)
- [EntitlementsQuery](entitlementsquery.md)
- [InfoPlistHash](infoplisthash.md)
- [IsInitProcess](isinitprocess.md)
- [IsSIPProtected](issipprotected.md)
- [PlatformType](platformtype.md)
- [ProcessCodeSigningFlags](processcodesigningflags.md)
- [SigningIdentifier](signingidentifier.md)
- [TeamIdentifier](teamidentifier.md)
- [TeamIdentifierMatchesCurrentProcess](teamidentifiermatchescurrentprocess.md)
- [ValidationCategory](validationcategory.md)

## See Also

- [func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool](sectaskvalidateforrequirement(task:requirement:).md)
  Tests whether a task’s executable satisfies a lightweight code requirement.
- [struct ProcessCodeRequirement](processcoderequirement.md)
  A lightweight code requirement that you use to evaluate a running process.
- [func allOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](allof(requirement:)-4k3ay.md)
  Creates a constraint that requires a running process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](anyof(requirement:)-vwhn.md)
  Creates a constraint that requires a running process’s executable to satisfy any of the provided constraints.
- [struct ProcessCodeSigningFlags](processcodesigningflags.md)
  A constraint that matches the current code-signing flags of a process.
- [struct ProcessConstraintBuilder](processconstraintbuilder.md)
  A custom parameter attribute that constructs process constraints from closures.
- [struct TeamIdentifierMatchesCurrentProcess](teamidentifiermatchescurrentprocess.md)
  A constraint that matches if a process has the same team identifier as the calling process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processconstraint)*