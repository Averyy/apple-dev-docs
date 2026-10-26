---
url: "https://docs.swift.org/latest/documentation/diagnostics/error-in-future-swift-version"
framework: "Swift-Org/diagnostics"
---

# Language mode and tools version (ErrorInFutureSwiftVersion)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Swift language mode and Swift compiler tools version are distinct concepts. One compiler version can support multiple language modes.

There are two related kinds of “Swift version” that are distinct:

- Swift tools version: the version number of the compiler itself. For example, the Swift 5.6 compiler was introduced in March 2022.
- Swift language mode version: the language mode version with which we are providing source compatibility. For example, the Swift 5 language mode is the most current language mode version supported by Swift tools version 5.10.

The Swift tools support multiple Swift language modes. All Swift tools versions between 5.0 and 5.10 support three Swift language modes: 4, 4.2, and 5. The Swift 6.0 compiler supports four Swift language modes: 4, 4.2, 5, and 6. Swift language modes are opt-in; when you use a tools version that supports a new language mode, your code will not build with the new language mode until you set that language mode in your build settings with `-language-mode X`.

A warning suffixed with `this is an error in the Swift 6 language mode` means that once you migrate to that language mode in your code, the warning will be promoted to an error. These warnings primarily come from enabling upcoming features that are enabled by default in that language mode version, but errors may also be staged in as warnings until the next language mode to maintain source compatibility when fixing compiler bugs.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/error-in-future-swift-version)*