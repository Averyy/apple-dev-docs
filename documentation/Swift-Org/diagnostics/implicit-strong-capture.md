---
url: "https://docs.swift.org/latest/documentation/diagnostics/implicit-strong-capture"
framework: "Swift-Org/diagnostics"
---

# Implicit strong captures of weak capture list items (ImplicitStrongCapture)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

When you use a `weak` or `unowned` capture list item in a closure, but that object is implicitly captured as a strong reference in an outer escaping closure, the compiler emits a warning. This warning highlights cases that can cause unexpected reference cycles or unintended object lifetime extension.

For example, consider a hypothetical `DataService` class that uses a callback-based API to fetch data from the network, store the response model into a cache, and finally notify clients of an update:

```swift
final class DataService: Sendable {
  func fetchData(using cache: Cache) {
    networkService.fetch { responseData in
      let result = DataModel(responseData)
      cache.store(result) { [weak self] in
        self?.notifyClients(with: result)
      }
    }
  }
}
```

Here, `self` might appear to be weakly retained during the call to `fetch`, since it’s only captured weakly in the inner closure. However, the presence of the capture list item causes the outer closure to capture a strong reference to `self`. To highlight this, the compiler emits a warning noting the ownership mismatch:

```
| final class DataService: Sendable {
|   func fetchData(using cache: Cache) {
|     networkService.fetch { responseData in
|                          |- note: 'self' implicitly strongly captured here
|                          `- note: add 'self' as a capture list item to silence
|       let result = DataModel(responseData)
|       cache.store(result) { [weak self] in
|                                   |- warning: 'weak' ownership of capture 'self' differs from implicitly-captured strong reference in outer scope
|                                   `- note: explicitly assign the capture list item to silence
|         self?.notifyClients(with: result)
|       }
```

To resolve the warning, add an explicit capture list item to the outer closure specifying the intended ownership. You can also silence the warning by explicitly assigning a value to the inner closure’s capture list item (e.g. `[weak x = x]`).

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/implicit-strong-capture)*