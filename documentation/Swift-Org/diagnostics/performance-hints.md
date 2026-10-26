---
url: "https://docs.swift.org/latest/documentation/diagnostics/performance-hints"
framework: "Swift-Org/diagnostics"
---

# Performance Hints (PerformanceHints)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

The `PerformanceHints` diagnostic group provides opt-in guidance for identifying language constructs and code patterns that carry non-obvious runtime performance costs. The diagnostics are intended to help developers writing performance-critical code make informed decisions about the abstractions they use and to surface hidden costs that may not be apparent from the source code alone to a non-expert Swift programmer.

This diagnostic group is **off by default**. It can be enabled as warnings with `-Wwarning PerformanceHints`, or escalated to errors with `-Werror PerformanceHints`.

#### Sub-groups

The `PerformanceHints` group contains the following sub-groups, each of which can also be enabled or controlled independently:

- [Existential Types and Performance (ExistentialType)](./existential-type.md): Warns on use of existential types (`any Protocol`), which incur heap allocation, reference counting, exclusivity enforcement, and dynamic dispatch overhead.
- [Implicit Copy On Return (ReturnTypeImplicitCopy)](./return-type-implicit-copy.md): Warns when functions or closures return `Array` or `Dictionary` values, which leads to implicit heap-allocated copies of the collections.
- [Untyped throws (UntypedThrows)](./untyped-throws.md): Warns on untyped `throws` declarations, where the use of `any Error` incurs a heap allocation on each `throw`.

For example, to enable only the `UntypedThrows` checks as warnings:

```
-Wwarning UntypedThrows
```

Or to enable all performance hints as errors but keep `UntypedThrows` as a warning:

```
-Werror PerformanceHints -Wwarning UntypedThrows
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/performance-hints)*