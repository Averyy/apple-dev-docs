# LaunchConstraint

**Framework**: LightweightCodeRequirements  
**Kind**: protocol

A protocol to which a lightweight code requirement constraint conforms if you can use it in launch code requirements.

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
protocol LaunchConstraint : Decodable, Encodable, Sendable
```

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [ValidationCategory](validationcategory.md)

## See Also

- [func SecCodeCheckValidityWithProcessRequirement(code: SecCode, flags: SecCSFlags, requirement: ProcessCodeRequirement) -> ValidationResult](seccodecheckvaliditywithprocessrequirement(code:flags:requirement:).md)
  Checks whether the code associated with a running process satisfies a lightweight code requirement.
- [var launchRequirement: LaunchCodeRequirement?](../Foundation/Process/launchRequirement.md)
- [struct LaunchCodeRequirement](launchcoderequirement.md)
  A lightweight code requirement that you use to evaluate the executable for a launching process.
- [func allOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](allof(requirement:)-4gf5f.md)
  Creates a constraint that requires a launching process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](anyof(requirement:)-6nicx.md)
  Creates a constraint that requires a launching process’s executable to satisfy any of the provided constraints.
- [struct LaunchConstraintBuilder](launchconstraintbuilder.md)
  A custom parameter attribute that constructs launch constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/launchconstraint)*