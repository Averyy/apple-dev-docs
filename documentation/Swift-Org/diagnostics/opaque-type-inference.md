---
url: "https://docs.swift.org/latest/documentation/diagnostics/opaque-type-inference"
framework: "Swift-Org/diagnostics"
---

# Underlying type inference for opaque result types (OpaqueTypeInference)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Opaque result types are a useful tool for abstracting the return type of a function or subscript, or type of a property. Although the concrete underlying type of an opaque type is hidden from clients, it is still inferred by the compiler, which enforces certain usage requirements:

- Property declarations with opaque types must have an initializer expression or getter, and functions or subscripts returning opaque types must have at least one `return` statement:

```swift
let x: some Equatable // error: property declares an opaque return type, but has no initializer expression from which to infer an underlying type
let y: some Equatable = 42 // OK
let z: some Equatable { // Also OK
  return "hello, " + "world!"
}

func foo() -> some Equatable { // error: function declares an opaque return type, but has no return statements in its body from which to infer an underlying type
  fatalError("Unimplemented")
}

func bar() -> some Equatable { // OK
  fatalError("Unimplemented")
  return 42
}
```

- The underlying type of an opaque type must be unique. In other words, if a function or subscript returns an opaque type, it must return values of the same underlying type from every `return` statement in its body.

```swift
func foo(bar: Bool) -> some Equatable { // error: function declares an opaque return type, but the return statements in its body do not have matching underlying types
  if bar {
    return "hello, world!" // note: return statement has underlying type 'String'
  } else {
    return 1 // note: return statement has underlying type 'Int'
  }
}

func bar(baz: Bool) -> some Equatable { // OK, both branches of the if statement return a value of the same underlying type, Int.
  if baz {
    return 100
  } else {
    return 200
  }
}
```

- Functions returning opaque types may be recursive. However, such functions must have at least one `return` statement that returns a concrete underlying type as opposed to the function’s own opaque result type. Additionally, recursive calls may not be used to create an infinitely recursive opaque type.

```swift
func foo(_ x: Int) -> some Equatable { // error: function declares an opaque return type, but has no return statements in its body from which to infer an underlying type
  // Not allowed because there aren't any non-recursive returns to infer the underlying type from.
  return foo(x+1)
}

struct EquatableWrapper<T: Equatable>: Equatable { var value: T }
func foo() -> some Equatable { // error: function opaque return type was inferred as 'EquatableWrapper<some Equatable>', which defines the opaque type in terms of itself
  // Not allowed because the use of EquatableWrapper creates an infinitely recursive underlying type: EquatableWrapper<EquatableWrapper<EquatableWrapper<...>>>...>
  return EquatableWrapper(value: foo())
}

func bar(_ x: Int) -> some Equatable { // OK, the underlying type can be inferred from the second return statement.
  if x > 0 {
    return bar(x-1)
  } else {
    return x
  }
}
```

To learn more about opaque result types, see the [Opaque Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/opaquetypes) section of *The Swift Programming Language*.

## See Also

### Related Documentation
- [Opaque Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/opaquetypes)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/opaque-type-inference)*