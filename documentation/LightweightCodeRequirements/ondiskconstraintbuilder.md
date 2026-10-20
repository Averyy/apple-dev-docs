# OnDiskConstraintBuilder

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

A custom parameter attribute that constructs on-disk constraints from closures.

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
@resultBuilder
struct OnDiskConstraintBuilder
```

## Topics

### Type Methods
- [static func buildBlock([any OnDiskConstraint]...) -> [any OnDiskConstraint]](./ondiskconstraintbuilder/buildblock%28_%29.md)
  Builds flat array from a variadic set of arrays
- [static func buildEither(first: [any OnDiskConstraint]) -> [any OnDiskConstraint]](./ondiskconstraintbuilder/buildeither%28first%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true
- [static func buildEither(second: [any OnDiskConstraint]) -> [any OnDiskConstraint]](./ondiskconstraintbuilder/buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false
- [static func buildExpression(any OnDiskConstraint) -> [any OnDiskConstraint]](./ondiskconstraintbuilder/buildexpression%28_%29-1qla.md)
  Builds an expression within the builder
- [static func buildExpression([any OnDiskConstraint]) -> [any OnDiskConstraint]](./ondiskconstraintbuilder/buildexpression%28_%29-3uyy8.md)
  Builds an expression within the builder
- [static func buildOptional([any OnDiskConstraint]?) -> [any OnDiskConstraint]](./ondiskconstraintbuilder/buildoptional%28_%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true and has no else option

## See Also

### Checking code requirements for code files on disk
- [func SecStaticCodeCheckValidityWithOnDiskRequirement(code: SecStaticCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](./secstaticcodecheckvaliditywithondiskrequirement%28code,flags,requirement%29.md)
  Checks whether static code on disk satisfies a lightweight code requirement.
- [func SecCodeCheckValidityWithOnDiskRequirement(code: SecCode, flags: SecCSFlags, requirement: OnDiskCodeRequirement) -> ValidationResult](./seccodecheckvaliditywithondiskrequirement%28code,flags,requirement%29.md)
  Checks whether code on disk satisfies a lightweight code requirement.
- [struct ValidationResult](./validationresult.md)
  A structure that represents the result of testing a lightweight code requirement.
- [struct OnDiskCodeRequirement](./ondiskcoderequirement.md)
  A lightweight code requirement that you use to evaluate a code file on disk.
- [func allOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](./allof%28requirement%29-2ocwl.md)
  Creates a constraint that requires code on disk to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any OnDiskConstraint]) -> any OnDiskConstraint](./anyof%28requirement%29-71pff.md)
  Creates a constraint that requires code on disk to satisfy any of the provided constraints.
- [protocol OnDiskConstraint](./ondiskconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in on-disk code requirements.
- [struct OnDiskCodeSigningFlags](./ondiskcodesigningflags.md)
  A constraint that tests the code-signing flags of a code file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskconstraintbuilder)*