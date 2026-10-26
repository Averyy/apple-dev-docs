---
url: "https://docs.swift.org/latest/documentation/diagnostics/nominal-types"
framework: "Swift-Org/diagnostics"
---

# Nominal types (NominalTypes)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

In Swift, a type is considered a nominal type if it has been explicitly named by a declaration somewhere in code. Examples of nominal types include classes, structures and enumerations. Nominal types are an important concept in Swift because they may conform to protocols, be extended, and have values created using the initializer syntax `MyType()`.

In contrast, non-nominal types do not have these capabilities. Many are obtained by composing other types. Examples include function types like `(Int) -> (String)`, tuple types like `(Int, String)`, metatypes like `Int.Type`, and special types like `Any` and `AnyObject`.

Since a protocol is named by a declaration in code, it may conform to (in other words, refine) other protocols and it may be extended. However, when written as the type of a constant or variable such as `let value: MyProtocol`, the name refers to a distinct, non-nominal existential type that provides a “box” for a value of any concrete type that conforms to the protocol. The existential type itself does not conform to any protocols and cannot be extended, and a value cannot be created using the initializer syntax `MyProtocol()`.

For more on using existential types, see [Protocols as Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols#Protocols-as-Types) in *The Swift Programming Language*.

## See Also

### Related Documentation
- [Protocols as Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols#Protocols-as-Types)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/nominal-types)*