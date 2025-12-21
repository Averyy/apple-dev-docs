# OnDiskCodeSigningFlags

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A constraint that tests the code-signing flags of a code file on disk.

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
struct OnDiskCodeSigningFlags
```

## Topics

### Structures
- [OnDiskCodeSigningFlags.ValueSet](ondiskcodesigningflags/valueset.md)
  Code signing flags that can be set on code on disk.
### Type Aliases
- [OnDiskCodeSigningFlags.DataType](ondiskcodesigningflags/datatype.md)
  The basic input data type for this constraint: `OnDiskCodeSigningFlags.ValueSet`
- [OnDiskCodeSigningFlags.OutType](ondiskcodesigningflags/outtype.md)
  The type of this constraint: [`OnDiskCodeSigningFlags`](ondiskcodesigningflags.md)
### Type Methods
- [static func isSuperset(of: OnDiskCodeSigningFlags.DataType) -> OnDiskCodeSigningFlags.OutType](ondiskcodesigningflags/issuperset(of:).md)
  Matches when the code signing flags on the file/slice are a superset of the specified flags.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [OnDiskConstraint](ondiskconstraint.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func anyOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](anyof(requirement:)-71pff.md)
  Creates a constraint that requires code on disk to satisfy any of the provided constraints.
- [protocol OnDiskConstraint](ondiskconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- [struct OnDiskConstraintBuilder](ondiskconstraintbuilder.md)
  A custom parameter attribute that constructs on-disk constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags)*