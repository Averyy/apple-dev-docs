# SecCodeCheckValidityWithProcessRequirement(code:flags:requirement:)

**Framework**: LightweightCodeRequirements  
**Kind**: func

Checks whether the code associated with a running process satisfies a lightweight code requirement.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func SecCodeCheckValidityWithProcessRequirement(code: SecCode, flags: SecCSFlags, requirement: ProcessCodeRequirement) -> ValidationResult
```

#### Discussion

Returns a validation result which indicates whether the code signature is valid, whether it matches the requirement, and if not one of those two, then why not.

## See Also

- [var launchRequirement: LaunchCodeRequirement? { get set }](../Foundation/Process/launchRequirement.md)
- [struct LaunchCodeRequirement](launchcoderequirement.md)
  A lightweight code requirement that you use to evaluate the executable for a launching process.
- [func allOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](allof(requirement:)-4gf5f.md)
  Creates a constraint that requires a launching process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any LaunchConstraint]) -> any LaunchConstraint](anyof(requirement:)-6nicx.md)
  Creates a constraint that requires a launching process’s executable to satisfy any of the provided constraints.
- [protocol LaunchConstraint](launchconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in launch code requirements.
- [struct LaunchConstraintBuilder](launchconstraintbuilder.md)
  A custom parameter attribute that constructs launch constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/seccodecheckvaliditywithprocessrequirement(code:flags:requirement:))*