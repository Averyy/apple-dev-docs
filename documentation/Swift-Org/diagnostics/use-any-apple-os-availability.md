---
url: "https://docs.swift.org/latest/documentation/diagnostics/use-any-apple-os-availability"
framework: "Swift-Org/diagnostics"
---

# Use anyAppleOS availability (UseAnyAppleOSAvailability)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

An opt-in warning that suggests replacing a group of per-platform `@available` specifications with a single `anyAppleOS` specification when the platforms share the same introduced version.

## Overview

`anyAppleOS` is a meta-platform that covers all Apple platforms using unified versioning starting at 26.0. When a declaration is available on at least `macOS`, `iOS`, `tvOS`, and `watchOS` at the same introduced version, a single `anyAppleOS` specification expresses the same intent more concisely.

This warning is opt-in and disabled by default. Enable it with:

```
-Wwarning UseAnyAppleOSAvailability
```

or promote it to an error with `-Werror UseAnyAppleOSAvailability`.

## Examples

Short-form grouped availability:

```swift
@available(macOS 26, iOS 26, tvOS 26, watchOS 26, *)
func foo() {} // warning: use '@available(anyAppleOS 26, *)' instead of platform specific '@available' attributes with the same version

// Suggested replacement
@available(anyAppleOS 26, *)
func foo() {}
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/use-any-apple-os-availability)*