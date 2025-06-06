# SecTaskValidateForRequirement(task:requirement:)

**Framework**: LightweightCodeRequirements  
**Kind**: func

Tests whether a task’s executable satisfies a lightweight code requirement.

**Availability**:
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
func SecTaskValidateForRequirement(task: SecTask, requirement: ProcessCodeRequirement) throws -> Bool
```

#### Return Value

If the requirement matches the process, then `true`; `false` if it doesn’t.

#### Discussion

This function throws a value from [`ConstraintError`](constrainterror.md) if it can’t evaluate whether the executable satisfies the lightweight code requirement.

## Parameters

- `task`: An object that represents the running task.
- `requirement`: The lightweight code requirement to test.

## See Also

- [struct ProcessCodeRequirement](processcoderequirement.md)
  A lightweight code requirement that you use to evaluate a running process.
- [func allOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](allof(requirement:)-4k3ay.md)
  Creates a constraint that requires a running process’s executable to satisfy all of the provided constraints.
- [func anyOf(requirement: () -> [any ProcessConstraint]) -> any ProcessConstraint](anyof(requirement:)-vwhn.md)
  Creates a constraint that requires a running process’s executable to satisfy any of the provided constraints.
- [protocol ProcessConstraint](processconstraint.md)
  A protocol to which a lightweight code requirement constraint conforms if you can use it in process code requirements.
- [struct ProcessCodeSigningFlags](processcodesigningflags.md)
  A constraint that matches the current code-signing flags of a process.
- [struct ProcessConstraintBuilder](processconstraintbuilder.md)
  A custom parameter attribute that constructs process constraints from closures.
- [struct TeamIdentifierMatchesCurrentProcess](teamidentifiermatchescurrentprocess.md)
  A constraint that matches if a process has the same team identifier as the calling process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/sectaskvalidateforrequirement(task:requirement:))*