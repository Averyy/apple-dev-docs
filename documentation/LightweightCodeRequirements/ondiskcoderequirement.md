# OnDiskCodeRequirement

**Framework**: LightweightCodeRequirements  
**Kind**: struct

A lightweight code requirement that you use to evaluate a code file on disk.

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
struct OnDiskCodeRequirement
```

#### Overview

[`OnDiskCodeRequirement`](ondiskcoderequirement.md) objects can only be built using constraints that conform to the [`OnDiskConstraint`](ondiskconstraint.md) protocol. Specifically [`OnDiskCodeRequirement`](ondiskcoderequirement.md) objects will be matched against a SecStaticCodeRef. A SecStaticCodeRef may reference any of the following:

- The main executable of a bundle
- A specific file on disk
- The region of a Mach-O pertaining to a specific architecture (e.g. x86_64, arm64, arm64e).

## Topics

### Initializers
- [init(LaunchCodeRequirement) throws](ondiskcoderequirement/init(_:)-2lfey.md)
  Convert a [`LaunchCodeRequirement`](launchcoderequirement.md) to an [`OnDiskCodeRequirement`](ondiskcoderequirement.md) if possible.
- [init(ProcessCodeRequirement) throws](ondiskcoderequirement/init(_:)-9imtm.md)
  Convert a [`ProcessCodeRequirement`](processcoderequirement.md) to an [`OnDiskCodeRequirement`](ondiskcoderequirement.md) if possible.
- [init(from: any Decoder) throws](ondiskcoderequirement/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](ondiskcoderequirement/encode(to:).md)
  Encodes this value into the given encoder
### Type Methods
- [static func allOf(requirement: () -> [any OnDiskConstraint]) throws -> OnDiskCodeRequirement](ondiskcoderequirement/allof(requirement:).md)
  Create a [`OnDiskCodeRequirement`](ondiskcoderequirement.md) that requires matching all of the provided constraints.
- [static func anyOf(requirement: () -> [any OnDiskConstraint]) throws -> OnDiskCodeRequirement](ondiskcoderequirement/anyof(requirement:).md)
  Create a [`OnDiskCodeRequirement`](ondiskcoderequirement.md) that requires matching any of the provided constraints.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func SecStaticCodeCheckValidityWithOnDiskRequirement(code: SecStaticCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](secstaticcodecheckvaliditywithondiskrequirement(code:flags:requirement:).md)
  Checks whether static code on disk satisfies a lightweight code requirement.
- [func SecCodeCheckValidityWithOnDiskRequirement(code: SecCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](seccodecheckvaliditywithondiskrequirement(code:flags:requirement:).md)
  Checks whether code on disk satisfies a lightweight code requirement.
- [struct ValidationResult](validationresult.md)
  A structure that represents the result of testing a lightweight code requirement.
- [func allOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](allof(requirement:)-2ocwl.md)
  Creates a constraint that requires code on disk to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](anyof(requirement:)-71pff.md)
  Creates a constraint that requires code on disk to satisfy any of the provided constraints.
- [protocol OnDiskConstraint](ondiskconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- [struct OnDiskCodeSigningFlags](ondiskcodesigningflags.md)
  A constraint that tests the code-signing flags of a code file on disk.
- [struct OnDiskConstraintBuilder](ondiskconstraintbuilder.md)
  A custom parameter attribute that constructs on-disk constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement)*