# allOf(requirement:)

**Framework**: LightweightCodeRequirements  
**Kind**: func

Creates a constraint that requires a launching process’s executable to satisfy all of the provided constraints.

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
func allOf(@LaunchConstraintBuilder requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint
```

## See Also

- [func SecCodeCheckValidityWithProcessRequirement(code: SecCode, flags: SecCSFlags, requirement: ProcessCodeRequirement) -> ValidationResult](seccodecheckvaliditywithprocessrequirement(code:flags:requirement:).md)
  Checks whether the code associated with a running process satisfies a lightweight code requirement.
- [var launchRequirement: LaunchCodeRequirement?](../foundation/process/4322522-launchrequirement.md)
- [struct LaunchCodeRequirement](launchcoderequirement.md)
  A lightweight code requirement that you use to evaluate the executable for a launching process.
- [func anyOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](anyof(requirement:)-6nicx.md)
  Creates a constraint that requires a launching process’s executable to satisfy any of the provided constraints.
- [protocol LaunchConstraint](launchconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in launch code requirements.
- [struct LaunchConstraintBuilder](launchconstraintbuilder.md)
  A custom parameter attribute that constructs launch constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/allof(requirement:)-4gf5f)*