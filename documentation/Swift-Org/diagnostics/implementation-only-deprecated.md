---
url: "https://docs.swift.org/latest/documentation/diagnostics/implementation-only-deprecated"
framework: "Swift-Org/diagnostics"
---

# Deprecated implementation-only imports (ImplementationOnlyDeprecated)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that identify `import` declarations with the `@_implementationOnly` attribute.

#### Overview

When applied to `import` declarations, the compiler-internal attribute `@_implementationOnly` attempts prevents declarations from the imported module from being exposed in the ABI or public interface of the dependent module. This attribute became deprecated when support for access levels on `import` declarations was introduced with [SE-0409: Access level on imports](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0409-access-level-on-imports.md).

One reason `@_implementationOnly import` is deprecated is that it is unsafe when used in modules that are built *without* [Library evolution](https://www.swift.org/blog/library-evolution/) enabled. For example, suppose the following code were part of a library named `Foo`:

```swift
// Library `Foo`
@_implementationOnly import ImplementationDetail

public struct Bar {
  internal var x: Baz // defined in ImplementationDetail
}
```

If `Foo` is not compiled with library evolution, then the memory layout of values of `Bar` must be known at compile time in clients of `Foo`. However, the `@_implementationOnly import` of `ImplementationDetail` prevents clients from being able to look up `Baz` which is a type that contributes to the layout of `Foo`. As a result, the layout of `Foo` will be miscalculated resulting in undefined behavior.

## See Also

### Related Documentation
- [SE-0409: Access level on imports](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0409-access-level-on-imports.md)
- [Library evolution](https://www.swift.org/blog/library-evolution/)
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
- [Dynamic exclusivity (DynamicExclusivity)](./dynamic-exclusivity.md)
  Experimental
- [Embedded Swift language restrictions (EmbeddedRestrictions)](./embedded-restrictions.md)
  Embedded Swift is a subset of the Swift language that that introduces some restrictions on the use of language features to eliminate the need for the Swift runtime. These restrictions are captured by the `EmbeddedRestrictions` diagnostic group.
- [Existential Types and Performance (ExistentialType)](./existential-type.md)
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/implementation-only-deprecated)*