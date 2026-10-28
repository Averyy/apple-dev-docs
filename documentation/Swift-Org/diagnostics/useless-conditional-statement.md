---
url: "https://docs.swift.org/latest/documentation/diagnostics/useless-conditional-statement"
framework: "Swift-Org/diagnostics"
---

# Useless conditional statement (UselessConditionalStatement)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that identify conditional statements (`if`, `while`, and `guard`) whose conditions can never be false.

## Overview

When the condition of an `if`, `while`, or `guard` statement is statically known to always be true, the conditional structure is unnecessary. For `if` and `while`, the body always executes (and a `while` loop with no `break` would never terminate); for `guard`, the `else` branch is unreachable.

## Examples

```
let x = 0
if case _ = x { // warning: 'if' condition is always true
  // ...
}

while case _ = x { // warning: 'while' condition is always true
  break
}

guard case _ = x else { // warning: 'guard' condition is always true, body is unreachable
  fatalError()
}
```

In the examples above, the pattern matching conditions (`case _ = ...`) can never fail.

## See Also

### Related Documentation
- [If Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#If-Statement)
- [Guard Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Guard-Statement)
- [While Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#While-Statement)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/useless-conditional-statement)*