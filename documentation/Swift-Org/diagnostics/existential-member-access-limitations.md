---
url: "https://docs.swift.org/latest/documentation/diagnostics/existential-member-access-limitations"
framework: "Swift-Org/diagnostics"
---

# Using protocol members with references to `Self` or `Self`-rooted associated types (ExistentialMemberAccess)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Protocol requirements and protocol extension members may be accessed via a conformance constraint on a generic parameter, an opaque result type, or via the protocol type itself:

## Overview

```swift
// An appropriately constrained generic parameter.
func foo<T: CustomStringConvertible>(arg: T) {
  let description: String = arg.description
}

do {
  // An appropriately constrained opaque result type.
  func foo() -> some CustomStringConvertible { true }

  let description: String = foo().description
}

// The protocol type.
func foo(arg: CustomStringConvertible) {
  let description: String = arg.description
}
```

While the former two options enable full access to the protocol interface, not all members may be accessible when the protocol is used as a type and not a constraint. Specifically, a protocol member cannot be accessed on a protocol type when its type signature contains a reference to `Self` or a `Self`-rooted associated type. Accessing such members on a protocol type is not supported because today the compiler does not have a well-defined meaning and means of representation for  `Self` and  `Self`-rooted associated types with respect to a protocol type  `P`.  As a result, the following code is not allowed:

```swift
protocol Shape {
  func matches(_ other: Self) -> Bool
}

func foo(_ shape: Shape) {
  // error: member 'matches' cannot be used on value of protocol type 'Shape'; use a generic constraint instead
  shape.matches(shape)
}

func foo(_ arg: Identifiable) {
  // error: member 'id' cannot be used on value of protocol type 'Identifiable'; use a generic constraint instead
  _ = arg.id
}
```

An exception to this limitation are members that contain `Self` only in [covariant](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)) position (such as a method result type), where  `Self` can be safely substituted with the protocol or protocol composition type used to access the member — a representable supertype. On the other hand, resorting to this ploy in contravariant parameter type position, like allowing one to pass a type-erased value to a method that accepts `Self`, is not type-safe and would expose the opportunity to pass in an argument of non-matching type.

```swift
protocol Shape {
  func duplicate() -> Self
}

func duplicateShape(_ shape: Shape) -> Shape {
  return shape.duplicate // OK, produces a value of type 'Shape'
}
```

Most use cases involving usage of protocol members that fall under the above restriction can instead be supported by constrained generics, opaque result types, or manual type-erasing wrappers. To learn more, see the sections on [Protocols](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols), [Generics](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics), and [Opaque Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/opaquetypes) in the Language Guide. For a better understanding of existential types in particular, and an in-depth exploration of the relationships among these built-in abstraction models, we recommend reading [Improving the UI of generics](https://forums.swift.org/t/improving-the-ui-of-generics/22814).

## See Also

### Related Documentation
- [Generics](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics)
- [Improving the UI of generics](https://forums.swift.org/t/improving-the-ui-of-generics/22814)
- [Opaque Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/opaquetypes)
- [Protocols](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/existential-member-access-limitations)*