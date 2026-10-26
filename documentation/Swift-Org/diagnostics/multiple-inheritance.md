---
url: "https://docs.swift.org/latest/documentation/diagnostics/multiple-inheritance"
framework: "Swift-Org/diagnostics"
---

# Multiple inheritance (MultipleInheritance)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

In some programming languages, a class can inherit the interface of multiple base classes. Known as multiple inheritance, this feature can add significant complexity to the language and is unsupported in Swift. Instead, Swift allows composition of interfaces using protocols.

Consider the following example:

```swift
protocol Utensil {
    var name: String { get }
}

protocol ServingUtensil: Utensil {
    func serve()
}

extension ServingUtensil {
    func serve() { /* Default implementation. */ }
}

protocol Fork: Utensil {
    func spear()
}

protocol Spoon: Utensil {
    func scoop()
}

struct CarvingFork: ServingUtensil, Fork { /* ... */ }
struct Spork: Spoon, Fork { /* ... */ }
struct Ladle: ServingUtensil, Spoon { /* ... */ }
```

Swift protocols can declare interfaces that must be implemented by each conforming type (like abstract class members in other programming languages such as C# or Java), and they can also provide overridable default implementations for those requirements in protocol extensions.

When class inheritance and protocol conformances are used together, subclasses inherit protocol conformances from base classes, introducing additional complexity. For example, the default implementation of a protocol requirement not overridden in the conforming base class also cannot be overridden in any subclass ([GitHub issue #42725](https://github.com/apple/swift/issues/42725)).

To learn more about defining and adopting protocols, see the [Protocols](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols) section in *The Swift Programming Language*. To learn more about class inheritance, see the [Inheritance](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/inheritance) section in *The Swift Programming Language*.

## See Also

### Related Documentation
- [GitHub issue #42725](https://github.com/apple/swift/issues/42725)
- [Inheritance](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/inheritance)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/multiple-inheritance)*