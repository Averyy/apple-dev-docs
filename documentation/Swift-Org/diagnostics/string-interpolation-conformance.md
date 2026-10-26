---
url: "https://docs.swift.org/latest/documentation/diagnostics/string-interpolation-conformance"
framework: "Swift-Org/diagnostics"
---

# Conforming to `StringInterpolationProtocol` (StringInterpolationConformance)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

A type conforming to `ExpressibleByStringInterpolation` uses a helper type called `StringInterpolation` to perform its interpolation. Many types can use `DefaultStringInterpolation`, which implements `String`’s interpolation behavior. Types can also implement custom behavior by providing their own type conforming to `StringInterpolationProtocol`.

In addition to its formal requirements, `init(literalCapacity:interpolationCount:)` and `appendLiteral(_:)`, `StringInterpolationProtocol` has an additional, informal requirement, `appendInterpolation`. String interpolations using `\()` syntax are translated into calls to matching `appendInterpolation` methods.

`StringInterpolationProtocol` conformers must provide at least one `appendInterpolation` method which:

- Is an instance method, as opposed to a `static` or `class` method
- Does not specify a return type, explicitly returns `Void`, or is marked with the `@discardableResult` attribute
- Is at least as accessible as its containing type

There are no restrictions on an `appendInterpolation` method’s argument list, generic parameters, availability, or error-throwing behavior.

If `appendInterpolation` is overloaded, the Swift compiler will choose an appropriate overload using the labels and argument types of each interpolation. When choosing an overload, any accessible `appendInterpolation` instance method may be used, even if it does not meet all of the requirements above. However, if a `StringInterpolationProtocol` conformer doesn’t have any `appendInterpolation` methods which meet all of the requirements, an error will be reported at compile time.

To learn more about customizing string interpolation behavior, see the standard library documentation of the `ExpressibleByStringInterpolation` and `StringInterpolationProtocol` protocols.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/string-interpolation-conformance)*