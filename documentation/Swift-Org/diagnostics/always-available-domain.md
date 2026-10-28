---
url: "https://docs.swift.org/latest/documentation/diagnostics/always-available-domain"
framework: "Swift-Org/diagnostics"
---

# Always enabled availability domains (AlwaysAvailableDomain)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.

## Overview

Custom availability domains (which are an experimental feature gated by `-enable-experimental-feature CustomAvailability`) may be declared as “permanently enabled” which indicates that the domain is known available at compile time and can never become unavailable in a different configuration. This state is useful for representing feature flags for features which have become permanently enabled.

Restricting a region of code to only being available in a permanently enabled availability domain will result in diagnostics that suggest the removal of the restriction. For example:

```
@available(MyFeature) // warning: '@available' has no effect because 'PermanentlyEnabled' is always available
struct MyFeatureView: View {
  // ...
}
```

## See Also

- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
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
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/always-available-domain)*