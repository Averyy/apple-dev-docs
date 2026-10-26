---
url: "https://docs.swift.org/latest/documentation/diagnostics/useless-availability-check"
framework: "Swift-Org/diagnostics"
---

# Useless availability check (UselessAvailabilityCheck)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that identify `if #available` queries that are guaranteed to succeed because an enclosing scope already restricts availability.

#### Overview

When an `if #available` query checks for an availability that is already implied by the availability of an enclosing scope (such as a containing declaration’s `@available` attribute or another `if #available` block), the check is unnecessary and the guard will always succeed at runtime.

```
@available(macOS 26.4, *)
struct WeatherView: View {
  var body: some View {
    if #available(macOS 26.0, *) { // warning: unnecessary check for 'macOS'; enclosing scope ensures guard will always be true
      // ...
    }
  }
}
```

The `if #available` check above can be removed because `WeatherView` is already restricted to `macOS 26.4` or newer, which implies `macOS 26.0` or newer.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/useless-availability-check)*