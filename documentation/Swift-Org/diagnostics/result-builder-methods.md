---
url: "https://docs.swift.org/latest/documentation/diagnostics/result-builder-methods"
framework: "Swift-Org/diagnostics"
---

# Result builder methods (ResultBuilderMethods)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

To be useful as a result builder, a result builder type must provide a sufficient subset of function-building methods that enable the transformation of various statement kinds (`if`, `switch`, `for`..`in`, etc.). The following example result builder illustrates the various function-building methods one can define:

```swift
@resultBuilder
struct ExampleResultBuilder {
  /// The type of individual statement expressions in the transformed function,
  /// which defaults to Component if buildExpression() is not provided.
  typealias Expression = ...

  /// The type of a partial result, which will be carried through all of the
  /// build functions.
  typealias Component = ...

  /// The type of the final returned result, which defaults to Component if
  /// buildFinalResult() is not provided.
  typealias Result = ...

  /// Required by every result builder to build combined results from
  /// statement blocks.
  static func buildBlock(_ components: Component...) -> Component { ... }

  /// If declared, provides contextual type information for statement
  /// expressions to translate them into partial results.
  static func buildExpression(_ expression: Expression) -> Component { ... }

  /// Enables support for `if` statements that do not have an `else`.
  static func buildOptional(_ component: Component?) -> Component { ... }

  /// With buildEither(second:), enables support for 'if-else' and 'switch'
  /// statements by folding conditional results into a single result.
  static func buildEither(first component: Component) -> Component { ... }

  /// With buildEither(first:), enables support for 'if-else' and 'switch'
  /// statements by folding conditional results into a single result.
  static func buildEither(second component: Component) -> Component { ... }

  /// Enables support for..in loops in a result builder by combining the
  /// results of all iterations into a single result.
  static func buildArray(_ components: [Component]) -> Component { ... }

  /// If declared, this will be called on the partial result of an 'if
  /// #available' block to allow the result builder to erase type
  /// information.
  static func buildLimitedAvailability(_ component: Component) -> Component { ... }

  /// If declared, this will be called on the partial result from the outermost
  /// block statement to produce the final returned result.
  static func buildFinalResult(_ component: Component) -> Result { ... }
}
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/result-builder-methods)*