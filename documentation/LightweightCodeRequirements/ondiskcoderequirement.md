# OnDiskCodeRequirement

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

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

## Overview

[`OnDiskCodeRequirement`](./ondiskcoderequirement.md) objects can only be built using constraints that conform to the [`OnDiskConstraint`](./ondiskconstraint.md) protocol. Specifically [`OnDiskCodeRequirement`](./ondiskcoderequirement.md) objects will be matched against a SecStaticCodeRef. A SecStaticCodeRef may reference any of the following:

- The main executable of a bundle
- A specific file on disk
- The region of a Mach-O pertaining to a specific architecture (e.g. x86_64, arm64, arm64e).

## Topics

### Initializers
- [init(LaunchCodeRequirement) throws](./ondiskcoderequirement/init%28_%29-2lfey.md)
  Convert a [`LaunchCodeRequirement`](./launchcoderequirement.md) to an [`OnDiskCodeRequirement`](./ondiskcoderequirement.md) if possible.
- [init(ProcessCodeRequirement) throws](./ondiskcoderequirement/init%28_%29-9imtm.md)
  Convert a [`ProcessCodeRequirement`](./processcoderequirement.md) to an [`OnDiskCodeRequirement`](./ondiskcoderequirement.md) if possible.
- [init(from: any Decoder) throws](./ondiskcoderequirement/init%28from%29.md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func encode(to: any Encoder) throws](./ondiskcoderequirement/encode%28to%29.md)
  Encodes this value into the given encoder
### Type Methods
- [static func allOf(requirement: () -> [any OnDiskConstraint]) throws -> OnDiskCodeRequirement](./ondiskcoderequirement/allof%28requirement%29.md)
  Create a [`OnDiskCodeRequirement`](./ondiskcoderequirement.md) that requires matching all of the provided constraints.
- [static func anyOf(requirement: () -> [any OnDiskConstraint]) throws -> OnDiskCodeRequirement](./ondiskcoderequirement/anyof%28requirement%29.md)
  Create a [`OnDiskCodeRequirement`](./ondiskcoderequirement.md) that requires matching any of the provided constraints.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking code requirements for code files on disk
- [func SecStaticCodeCheckValidityWithOnDiskRequirement(code: SecStaticCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](./secstaticcodecheckvaliditywithondiskrequirement%28code,flags,requirement%29.md)
  Checks whether static code on disk satisfies a lightweight code requirement.
- [func SecCodeCheckValidityWithOnDiskRequirement(code: SecCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](./seccodecheckvaliditywithondiskrequirement%28code,flags,requirement%29.md)
  Checks whether code on disk satisfies a lightweight code requirement.
- [struct ValidationResult](./validationresult.md)
  A structure that represents the result of testing a lightweight code requirement.
- [func allOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](./allof%28requirement%29-2ocwl.md)
  Creates a constraint that requires code on disk to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](./anyof%28requirement%29-71pff.md)
  Creates a constraint that requires code on disk to satisfy any of the provided constraints.
- [protocol OnDiskConstraint](./ondiskconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- [struct OnDiskCodeSigningFlags](./ondiskcodesigningflags.md)
  A constraint that tests the code-signing flags of a code file on disk.
- [struct OnDiskConstraintBuilder](./ondiskconstraintbuilder.md)
  A custom parameter attribute that constructs on-disk constraints from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement)*