---
url: "https://docs.swift.org/latest/documentation/diagnostics/deprecated-declaration"
framework: "Swift-Org/diagnostics"
---

# Deprecated declaration warnings (DeprecatedDeclaration)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings related to deprecated APIs that may be removed in future versions and should be replaced with more current alternatives.

## Overview

The `DeprecatedDeclaration` group covers the following warnings:

- Use of a function annotated with `@available(<platform>, deprecated: <version>)`

  ```swift
  @available(iOS, deprecated: 10.0)
  func oldFunction() {
    // This function is deprecated and should not be used.
  }

  oldFunction() // 'oldFunction()' is deprecated
  ```
- Use of a function annotated with `@available(<platform>, deprecated: <version>, renamed: "<new name>")`

  ```swift
  @available(iOS, deprecated: 10.0, renamed: "newFunction")
  func oldFunction() {
    // This function is deprecated and should not be used.
  }

  oldFunction() // 'oldFunction()' is deprecated: renamed to 'newFunction'
  ```
- Use of a type as an instance of a protocol when the type’s conformance to the protocol is marked as deprecated

  ```swift
  struct S {}

  protocol P {}

  @available(*, deprecated)
  extension S: P {}

  func f(_ p: some P) {}

  func test() {
    f(S()) // Conformance of 'S' to 'P' is deprecated
  }
  ```
- When a protocol requirement has a default implementation marked as `deprecated` and the type conforming to the protocol doesn’t provide that requirement

  ```swift
  protocol P {
    func f()
    func g()
  }

  extension P {
    @available(*, deprecated)
    func f() {}
    @available(*, deprecated, message: "write it yourself")
    func g() {}
  }

  struct S: P {} // deprecated default implementation is used to satisfy instance method 'f()' required by protocol 'P'
                // deprecated default implementation is used to satisfy instance method 'g()' required by protocol 'P': write it yourself
  ```
- When a protocol requirement has been deprecated

  ```swift
  struct S: Hashable {
    var hashValue: Int { // 'Hashable.hashValue' is deprecated as a protocol requirement; conform type 'S' to 'Hashable' by implementing 'hash(into:)' instead
      ...
    }
  }
  final class C: Executor {
    func enqueue(_ job: __owned Job) {} // 'Executor.enqueue(Job)' is deprecated as a protocol requirement; conform type 'C' to 'Executor' by implementing 'func enqueue(ExecutorJob)' instead
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
- [Captures in a `@Sendable` closure (SendableClosureCaptures)](./sendable-closure-captures.md)
- [Compilation caching (CompilationCaching)](./compilation-caching.md)
  Errors and warnings related to the compiler’s CAS compilation caching.
- [Conforming to `StringInterpolationProtocol` (StringInterpolationConformance)](./string-interpolation-conformance.md)
- [Conversion from `@isolated(any)` function type to synchronous function type (ConversionFromIsolatedAnyToSynchronous)](./conversion-from-isolated-any-to-synchronous.md)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/deprecated-declaration)*