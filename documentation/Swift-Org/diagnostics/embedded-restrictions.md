---
url: "https://docs.swift.org/latest/documentation/diagnostics/embedded-restrictions"
framework: "Swift-Org/diagnostics"
---

# Embedded Swift language restrictions (EmbeddedRestrictions)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Embedded Swift is a subset of the Swift language that that introduces some restrictions on the use of language features to eliminate the need for the Swift runtime. These restrictions are captured by the `EmbeddedRestrictions` diagnostic group.

#### Overview

The Embedded Swift compilation model can produce extremely small binaries without external dependencies, suitable for restricted environments including embedded (microcontrollers) and baremetal setups (no operating system at all), and low-level environments (firmware, kernels, device drivers, low-level components of userspace OS runtimes). While the vast majority of Swift language features are available in Embedded Swift, there are some language features that require the full Swift standard library and runtime, which are not available in Embedded Swift.

Diagnostics in the `EmbeddedRestrictions` group describe those language features that cannot be used in Embedded Swift. These include:

- `weak` and `unowned` references, because Embedded Swift uses a simplified reference-counting model that cannot support them. For example:

  ```
  class Node {
    weak var parent: Node?    // error: attribute 'weak' cannot be used in Embedded Swift
  }
  ```
- Dynamic casts to a type involving a protocol are not supported, because Embedded Swift does not include runtime metadata about protocol conformances. For example:

  ```
  protocol P: AnyObject { }
  func casting(object: AnyObject) {
    if let p = object as? P { // error: cannot perform a dynamic cast to a type involving protocol 'P' in Embedded Swift
      // ...
    }
  }
  ```
- Non-final generic methods in a class, which are prohibited because they cannot be specialized for every possible call site. For example:

  ```
  class MyGenericClass<T> {
    func f<U>(value: U) { } // warning: generic instance method 'f(value:)' in a class must be 'final' in Embedded Swift

    func g() { } // okay, not generic relative to the class itself

    class func h() where T: P { } // warning: generic class method 'h()' in a class must be 'final' in Embedded Swift
  }
  ```
- Generic methods used on values of protocol type, which are prohibited because they cannot be specialized for every possible call site. For example:

  ```
  protocol P: AnyObject {
    func doNothing()
    func doSomething<T>(on value: T)
  }

  func testGenerics<Value: P>(value: value, i: Int) {
    value.doNothing()        // okay
    value.doSomething(on: i) // okay, always specialized
  }

  func testValuesOfProtocolType(value: any P, i: Int) {
    value.doNothing()        // okay
    value.doSomething(on: i) // warning: cannot use generic instance method 'doSomething(on:)' on a value of type 'any P' in Embedded Swift
  }
  ```

## See Also

### Related Documentation
- [A Vision for Embedded Swift](https://github.com/swiftlang/swift-evolution/blob/main/visions/embedded-swift.md)
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
- [Existential Types and Performance (ExistentialType)](./existential-type.md)
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/embedded-restrictions)*