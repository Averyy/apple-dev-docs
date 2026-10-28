---
url: "https://docs.swift.org/latest/documentation/diagnostics/sendable-closure-captures"
framework: "Swift-Org/diagnostics"
---

# Captures in a `@Sendable` closure (SendableClosureCaptures)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

`@Sendable` closures can be called multiple times concurrently, so any captured values must also be safe to access concurrently. To prevent data races, the compiler prevents capturing mutable values in a `@Sendable` closure.

For example:

```swift
func callConcurrently(
  _ closure: @escaping @Sendable () -> Void
) { ... }

func capture() {
  var result = 0
  result += 1

  callConcurrently {
    print(result)
  }
}
```

The compiler diagnoses the capture of `result` in a `@Sendable` closure:

```
|   callConcurrently {
|     print(result)
|           `- error: reference to captured var 'result' in concurrently-executing code
|   }
| }
```

Because the closure is marked `@Sendable`, the implementation of `callConcurrently` can call `closure` multiple times concurrently. For example, multiple child tasks within a task group can call `closure` concurrently:

```swift
func callConcurrently(
  _ closure: @escaping @Sendable () -> Void
) {
  Task {
    await withDiscardingTaskGroup { group in
      for _ in 0..<10 {
        group.addTask {
          closure()
        }
      }
    }
  }
}
```

If the type of the capture is `Sendable` and the closure only needs the value of the variable at the point of capture, resolve the error by explicitly capturing the variable by value in the closure’s capture list:

```swift
func capture() {
  var result = 0
  result += 1

  callConcurrently { [result] in
    print(result)
  }
}
```

This strategy does not apply to captures with non-`Sendable` type. Consider the following example:

```swift
class MyModel {
  func log() { ... }
}

func capture(model: MyModel) async {
  callConcurrently {
    model.log()
  }
}
```

The compiler diagnoses the capture of `model` in a `@Sendable` closure:

```
| func capture(model: MyModel) async {
|   callConcurrently {
|     model.log()
|     `- error: capture of 'model' with non-Sendable type 'MyModel' in a '@Sendable' closure
|   }
| }
```

If a type with mutable state can be referenced concurrently, but all access to mutable state happens on the main actor, isolate the type to the main actor and mark the methods that don’t access mutable state as `nonisolated`:

```swift
@MainActor
class MyModel {
  nonisolated func log() { ... }
}

func capture(model: MyModel) async {
  callConcurrently {
    model.log()
  }
}
```

The compiler will guarantee that the implementation of `log` does not access any main actor state.

If you manually ensure data-race safety, such as by using an external synchronization mechanism, you can use `nonisolated(unsafe)` to opt out of concurrency checking:

```swift
class MyModel {
  func log() { ... }
}

func capture(model: MyModel) async {
  nonisolated(unsafe) let model = model
  callConcurrently {
    model.log()
  }
}
```

## See Also

- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
- [Calling a mutating async actor-isolated method (ActorIsolatedMutatingAsync)](./actor-isolated-mutating-async.md)
- [Calling an actor-isolated method from a synchronous nonisolated context (ActorIsolatedCall)](./actor-isolated-call.md)
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
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/sendable-closure-captures)*