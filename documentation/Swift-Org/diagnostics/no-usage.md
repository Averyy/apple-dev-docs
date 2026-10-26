---
url: "https://docs.swift.org/latest/documentation/diagnostics/no-usage"
framework: "Swift-Org/diagnostics"
---

# Unused values (NoUsage)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

These diagnostics are emitted when a value is computed or defined but never used, which often indicates a programming mistake such as a missing assignment or an unintentionally discarded result.

The `NoUsage` group covers a range of unused-value situations like calling a function and ignoring its return value or declaring a variable or constant that is never read.

#### Example

```swift
func sortedCopy(_ array: [Int]) -> [Int] {
    var copy = array
    copy.sort()   // ok: sort() mutates in place
    array.sorted() // warning: result of call to 'sorted()' is unused
    return copy
}
```

#### How to fix

- Use the result, or assign it to `_` to explicitly discard it:

  ```swift
  _ = incrementGlobalCounter() // increment the counter without using the new value
  ```
- If ignoring the return value of a function is intentional and common for callers, then annotate the function with `@discardableResult`:

  ```swift
  private var counter = 0

  @discardableResult // callers may not need to use the new value
  func incrementGlobalCounter() -> Int {
  	counter += 1
    return counter
  }
  ```
- Replace an unused binding with `_`:

  ```swift
  enum NetworkError: Error {
    case requestFailed(statusCode: Int, message: String)
    case timeout
  }

  func handle(_ error: NetworkError) {
    switch error {
    case .requestFailed(let statusCode, _):  // message not needed here
      print("Request failed with status \(statusCode)")
    case .timeout:
      print("Request timed out")
    }
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/no-usage)*