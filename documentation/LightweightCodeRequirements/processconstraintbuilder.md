# ProcessConstraintBuilder

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

A custom parameter attribute that constructs process constraints from closures.

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
struct ProcessConstraintBuilder
```

## Topics

### Type Methods
- [static func buildBlock([any ProcessConstraint]...) -> [any ProcessConstraint]](./processconstraintbuilder/buildblock%28_%29.md)
  Builds flat array from a variadic set of arrays
- [static func buildEither(first: [any ProcessConstraint]) -> [any ProcessConstraint]](./processconstraintbuilder/buildeither%28first%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true
- [static func buildEither(second: [any ProcessConstraint]) -> [any ProcessConstraint]](./processconstraintbuilder/buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false
- [static func buildExpression([any ProcessConstraint]) -> [any ProcessConstraint]](./processconstraintbuilder/buildexpression%28_%29-6zrmh.md)
  Builds an expression within the builder
- [static func buildExpression(any ProcessConstraint) -> [any ProcessConstraint]](./processconstraintbuilder/buildexpression%28_%29-7rglu.md)
  Builds an expression within the builder
- [static func buildOptional([any ProcessConstraint]?) -> [any ProcessConstraint]](./processconstraintbuilder/buildoptional%28_%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true and has no else option.

## See Also

### Checking code requirements for running processes
- [func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool](./sectaskvalidateforrequirement%28task,requirement%29.md)
  Tests whether a task’s executable satisfies a lightweight code requirement.
- [struct ProcessCodeRequirement](./processcoderequirement.md)
  A lightweight code requirement that you use to evaluate a running process.
- [func allOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](./allof%28requirement%29-4k3ay.md)
  Creates a constraint that requires a running process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](./anyof%28requirement%29-vwhn.md)
  Creates a constraint that requires a running process’s executable to satisfy any of the provided constraints.
- [protocol ProcessConstraint](./processconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.
- [struct ProcessCodeSigningFlags](./processcodesigningflags.md)
  A constraint that matches the current code-signing flags of a process.
- [struct TeamIdentifierMatchesCurrentProcess](./teamidentifiermatchescurrentprocess.md)
  A constraint that matches if a process has the same team identifier as the calling process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/processconstraintbuilder)*