---
url: "https://docs.swift.org/latest/documentation/diagnostics/no-use-throwing-unstructured-task"
framework: "Swift-Org/diagnostics"
---

# Unused throwing unstructured task creation (NoUseUnstructuredThrowingTask)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

Creating a throwing unstructured `Task` without storing or discarding its result means any error thrown by the task body will be silently ignored. Resolve this warning by explicitly storing or discarding the task reference.

For example:

```swift
func example() {
  Task { throw MyError() }
}
```

Building this code produces a warning about the unused unstructured task:

```
| func example() {
|   Task { throw MyError() }
|   `- warning: unstructured throwing task created by 'init(name:priority:operation:)' is not used, which may accidentally ignore errors thrown inside the task
|      note: to silence this warning, handle the error inside the task, or store/discard the task value explicitly
| }
```

By storing the task reference and awaiting it, you won’t miss the error thrown by the task operation because awaiting `task.value` will be forced to acknowledge the thrown error with `try`:

```swift
let task = Task { throw MyError() }
try await task.value
```

Alternatively, ignore the thrown error explicitly:

```swift
_ = Task { throw MyError() }
```

### Cancelling unstructured tasks

Another reason to keep references to unstructured tasks is to be able to cancel them explicitly:

```swift
let task = Task { try Task.sleep(for: .seconds(10)) }
task.cancel() // cancel and wake-up the sleeping task
try await task.value
```

## See Also

- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
- [Calling a mutating async actor-isolated method (ActorIsolatedMutatingAsync)](./actor-isolated-mutating-async.md)
- [Calling an actor-isolated method from a synchronous nonisolated context (ActorIsolatedCall)](./actor-isolated-call.md)
- [Captures in a `@Sendable` closure (SendableClosureCaptures)](./sendable-closure-captures.md)
- [Compilation caching (CompilationCaching)](./compilation-caching.md)
  Errors and warnings related to the compiler’s CAS compilation caching.
- [Conforming to `StringInterpolationProtocol` (StringInterpolationConformance)](./string-interpolation-conformance.md)
- [Conversion from `@isolated(any)` function type to synchronous function type (ConversionFromIsolatedAnyToSynchronous)](./conversion-from-isolated-any-to-synchronous.md)
- [Deprecated declaration warnings (DeprecatedDeclaration)](./deprecated-declaration.md)
  Warnings related to deprecated APIs that may be removed in future versions and should be replaced with more current alternatives.
- [Deprecated implementation-only imports (ImplementationOnlyDeprecated)](./implementation-only-deprecated.md)
  Warnings that identify `import` declarations with the `@_implementationOnly` attribute.
- [Dynamic exclusivity (DynamicExclusivity)](./dynamic-exclusivity.md)
  Experimental
- [Embedded Swift language restrictions (EmbeddedRestrictions)](./embedded-restrictions.md)
  Embedded Swift is a subset of the Swift language that that introduces some restrictions on the use of language features to eliminate the need for the Swift runtime. These restrictions are captured by the `EmbeddedRestrictions` diagnostic group.
- [Existential Types and Performance (ExistentialType)](./existential-type.md)


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/no-use-throwing-unstructured-task)*