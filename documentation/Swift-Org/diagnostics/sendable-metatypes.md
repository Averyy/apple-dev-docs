---
url: "https://docs.swift.org/latest/documentation/diagnostics/sendable-metatypes"
framework: "Swift-Org/diagnostics"
---

# Sendable metatypes (SendableMetatypes)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

Types that are shared in concurrent code generally need to conform to `Sendable`. The same is true in generic code when sharing parameters of a generic parameter `T`. For example, the given code will produce an error under strict concurrency checking

```swift
func doSomethingElsewhere<T>(_ value: T) {
  Task { @concurrent in
    print(value) // warning: capture of non-Sendable type 'T'
  }
}
```

because `value` can have a non-Sendable type that is not safe to share. To address this potential data race, the type `T` can be marked as `Sendable`:

```swift
func doSomethingElsewhere<T: Sendable>(_ value: T) {
  Task { @concurrent in
    print(value)
  }
}
```

The same issue can occur when passing the type `T` itself, rather than a value of type `T`. The compiler will indicate such problems by noting that the metatype of `T`, spelled `T.Type`, is not `Sendable`:

```swift
protocol P {
  static func doSomething()
}

func doSomethingStatic<T: P>(_: T.Type) {
  Task { @concurrent in
    T.doSomething() // warning: capture of non-Sendable type 'T.Type' in an isolated closure
  }
}
```

In these cases, the type parameter should be required to conform to the `SendableMetatype` protocol, e.g.,

```swift
func doSomethingStatic<T: P & SendableMetatype>(_: T.Type) {
  Task { @concurrent in
    T.doSomething()
  }
}
```

The `SendableMetatype` requirement allows the function to share the type `T` in concurrent code. To maintain data race safety, it prevents callers from using isolated conformances in the call. For example, the following code will be rejected due to a data race:

```swift
@MainActor
class C: @MainActor P {
  static func doSomething() { }
}

@MainActor
func test(c: C) {
  doSomethingStatic(C.self) // error: main actor-isolated conformance of 'C' to 'P' cannot satisfy conformance requirement for a 'Sendable' type parameter
}

```

The conformance of `C` to `P` can only be used on the main actor, so it cannot be provided to `doSomethingStatic`, which calls the conformance from a different concurrent task.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/sendable-metatypes)*