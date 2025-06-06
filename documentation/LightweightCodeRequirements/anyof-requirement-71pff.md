# anyOf(requirement:)

**Framework**: LightweightCodeRequirements  
**Kind**: func

Creates a constraint that requires code on disk to satisfy any of the provided constraints.

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
func anyOf(@OnDiskConstraintBuilder requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint
```

## See Also

- [func SecStaticCodeCheckValidityWithOnDiskRequirement(code: SecStaticCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](secstaticcodecheckvaliditywithondiskrequirement(code:flags:requirement:).md)
  Checks whether static code on disk satisfies a lightweight code requirement.
- [func SecCodeCheckValidityWithOnDiskRequirement(code: SecCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](seccodecheckvaliditywithondiskrequirement(code:flags:requirement:).md)
  Checks whether code on disk satisfies a lightweight code requirement.
- [struct ValidationResult](validationresult.md)
  A structure that represents the result of testing a lightweight code requirement.
- [struct OnDiskCodeRequirement](ondiskcoderequirement.md)
  A lightweight code requirement that you use to evaluate a code file on disk.
- [func allOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](allof(requirement:)-2ocwl.md)
  Creates a constraint that requires code on disk to satisfy all of the provided constraints.
- [protocol OnDiskConstraint](ondiskconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- [struct OnDiskCodeSigningFlags](ondiskcodesigningflags.md)
  A constraint that tests the code-signing flags of a code file on disk.
- [struct OnDiskConstraintBuilder](ondiskconstraintbuilder.md)
  A custom parameter attribute that constructs on-disk constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/anyof(requirement:)-71pff)*