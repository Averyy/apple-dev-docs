---
url: "https://docs.swift.org/latest/documentation/diagnostics/strict-memory-safety"
framework: "Swift-Org/diagnostics"
---

# Strict memory safety (StrictMemorySafety)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that identify the use of language constructs and library APIs that can undermine memory safety, disabled by default.

## Overview

Strict memory safety can be enabled with the `-strict-memory-safety` compiler flag. Examples of memory-unsafe code in Swift include:

- Use of a function or type annotated with `@unsafe`:

  ```swift
  func getPointee<T>(_ pointer: UnsafeMutablePointer<Int>, as type: T.Type) -> T {
    // reference to unsafe global function 'unsafeBitCast'
    return unsafeBitCast(pointer.pointee, to: type)
  }
  ```
- Use of a function involving an `@unsafe` type:

  ```swift
  func evilMalloc(size: Int) -> Int {
    // use of global function 'malloc' involves unsafe type 'UnsafeMutableRawPointer'
    return Int(bitPattern: malloc(size))
  }
  ```
- Use of an entity that makes use of an unsafe language feature:

  ```swift
  // use of an unowned(unsafe) variable is not memory-safe
  unowned(unsafe) var parentNode: TreeNode<T>
  ```
- Definition of a type whose storage contains unsafe types:

  ```swift
  // struct MyTemporaryBuffer has storage involving unsafe types
  struct MyTemporaryBuffer<T> {
    private var storage: UnsafeBufferPointer<T>
  }
  ```
- Using an `@unsafe` operation to satisfy a safe protocol requirement:

  ```swift
  // conformance of 'MyType' to protocol 'CustomStringConvertible' involves unsafe code
  struct MyType: CustomStringConvertible {
    @unsafe var description: String {
      "I am unsafe!"
    }
  }
  ```

The warnings produced by strict memory safety can be suppressed by acknowledging the unsafe behaior with one of three constructs:

- `unsafe` expressions to acknowledges that there exists memory-unsafe code within the given expression, similar to the way `try` and `await` work for throwing and asynchronous functions:

  ```swift
  func evilMalloc(size: Int) -> Int {
    return unsafe Int(bitPattern: malloc(size))
  }
  ```
- `@unsafe` attribute, which acknowledges that a type or conformance is also unsafe:

  ```swift
  struct MyType: @unsafe CustomStringConvertible {
    @unsafe var description: String {
      "I am unsafe!"
    }
  }
  ```
- `@safe` attribute to indicate that an entity encapsulates the unsafe behavior to provide a safe interface:

  ```swift
  @safe struct MyTemporaryBuffer<T> {
    private var storage: UnsafeBufferPointer<T>
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/strict-memory-safety)*