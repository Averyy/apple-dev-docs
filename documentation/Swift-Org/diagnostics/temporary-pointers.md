---
url: "https://docs.swift.org/latest/documentation/diagnostics/temporary-pointers"
framework: "Swift-Org/diagnostics"
---

# Temporary pointers (TemporaryPointers)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

A temporary, or ephemeral, pointer in Swift is a pointer which is introduced by an implicit function argument conversion and is only valid for the lifetime of the function call it appears in. There are a few ways to create a temporary pointer:

- Using an inout-to-pointer conversion by passing an argument with `&`:

  ```swift
  func foo(bar: UnsafePointer<Int>) { /*...*/ }
  var x: Int = 42
  foo(bar: &x)
  ```

  In the example above, the `bar` passed to `foo` is a temporary pointer to `x` which is only valid until `foo` returns.

  Not all inout-to-pointer conversions result in a temporary pointer. Passing global variables and static properties inout can produce non-ephemeral pointers, as long as they are stored and have no observers. Additionally, if they are of a tuple or struct type, their stored members without observers may also be passed inout as non-ephemeral pointers.
- Using a string-to-pointer conversion:

  ```swift
  func foo(bar: UnsafePointer<Int8>) { /*...*/ }
  var x: String = "hello, world!"
  foo(bar: x)
  ```

  In the example above, the `bar` passed to `foo` is a temporary pointer to a buffer containing the UTF-8 code units of `x` which is only valid until `foo` returns.
- Using an array-to-pointer conversion:

  ```swift
  func foo(bar: UnsafePointer<Bool>) { /*...*/ }
  var x: [Bool] = [true, false, true]
  foo(bar: x)
  ```

  In the example above, the `bar` passed to `foo` is a temporary pointer to the elements of `x` which is only valid until `foo` returns.

Temporary pointers may only be passed as arguments to functions which do not store the pointer value or otherwise allow it to escape the function’s scope. The Swift compiler is able to diagnose some, but not all, violations of this rule. Misusing a temporary pointer by allowing it to outlive the enclosing function call results in undefined behavior. For example, consider the following incorrect code:

```swift
var x = 42
let ptr = UnsafePointer(&x)
// Do something with ptr.
```

This code is invalid because the initializer of `UnsafePointer` stores its argument, causing it to outlive the `UnsafePointer` initializer call. Instead, this code should use `withUnsafePointer` to access a pointer to `x` with an explicitly defined scope:

```swift
var x = 42
withUnsafePointer(to: &x) { ptr in
  // Do something with ptr, but don't allow it to escape this closure!
}
```

It’s important to note that the `withUnsafe*` functions can also result in undefined behavior if used improperly. For example, the following incorrect code is equivalent to the original temporary pointer example:

```swift
var x = 42
let ptr = withUnsafePointer(to: &x) { $0 }
// Do something with ptr.
```

This code is invalid because the pointer to `x` is only valid until `withUnsafePointer` returns, but it escapes the closure when it is returned and assigned to `ptr`.

To learn more about correctly using unsafe pointer APIs, see the Swift standard library documentation of `UnsafePointer` and related types.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/temporary-pointers)*