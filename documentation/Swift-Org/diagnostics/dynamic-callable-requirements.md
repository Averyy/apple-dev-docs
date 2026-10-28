---
url: "https://docs.swift.org/latest/documentation/diagnostics/dynamic-callable-requirements"
framework: "Swift-Org/diagnostics"
---

# @dynamicCallable implementation requirements (DynamicCallable)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

If a type is marked with the `@dynamicCallable` attribute, it must provide a valid implementation of `dynamicallyCall(withArguments:)`, `dynamicallyCall(withKeywordArguments:)`, or both. If it fails to do so, an error will be reported at compile-time. Note that an implementation of `dynamicallyCall(withKeywordArguments:)` is required to support calls with keyword arguments.

To be considered valid, an implementation of `dynamicallyCall(withArguments:)` must:

- Be an instance method. `static` or `class` implementations are not allowed.
- Have an argument type which conforms to the `ExpressibleByArrayLiteral` protocol. Often, this will be the built in `Array` type.
- The return type of `dynamicallyCall(withArguments:)` may be any valid type.

To be considered valid, an implementation of `dynamicallyCall(withKeywordArguments:)` must:

- Be an instance method. `static` or `class` implementations are not allowed.
- Have an argument type which conforms to the `ExpressibleByDictionaryLiteral` protocol. This can be `Dictionary`, `KeyValuePairs` (which may be used to support duplicated keyword arguments), or some other conforming type.
- The `Key` associated type of the argument type must conform to the `ExpressibleByStringLiteral` protocol. This type is used to represent the dynamic argument keywords.
- The `Value` associated type of the argument type and the return type of `dynamicallyCall(withKeywordArguments:)` may be any valid types.

## See also

- [SE-0216](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0216-dynamic-callable.md)

## See Also

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
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/dynamic-callable-requirements)*