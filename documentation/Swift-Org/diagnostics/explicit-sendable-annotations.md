---
url: "https://docs.swift.org/latest/documentation/diagnostics/explicit-sendable-annotations"
framework: "Swift-Org/diagnostics"
---

# Explicit `Sendable` annotations on public type declarations (ExplicitSendable)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Adds a warning for any public types without a `Sendable` annotation.

#### Overview

When enabled, the compiler will emit a warning if a public type has none of the following:

- A conformance to `Sendable` protocol;
- An unavailable conformance to `Sendable` protocol;
- `~Sendable` conformance to suppress the inference.

For example, given a simple public type:

```
public struct S {
    let x: Int
}
```

As it has no `Sendable` annotations, this diagnostic group will add the following warning:

```
1 | public struct S {
  |               |- warning: public struct 'S' does not specify whether it is 'Sendable' or not [#ExplicitSendable]
  |               |- note: consider making struct 'S' conform to the 'Sendable' protocol
  |               `- note: make struct 'S' explicitly non-Sendable to suppress this warning
2 |     let x: Int
3 | }
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/explicit-sendable-annotations)*