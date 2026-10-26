---
url: "https://docs.swift.org/latest/documentation/diagnostics/unnecessary-unsafe"
framework: "Swift-Org/diagnostics"
---

# Unnecessary unsafe (UnnecessaryUnsafe)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

This warning is emitted when an `unsafe` marker appears on an expression that contains no unsafe operations. The marker may have been added preemptively or the unsafe operation it was needed for may no longer be considered unsafe.

This group is a subgroup of [Unnecessary effect markers (UnnecessaryEffectMarker)](./unnecessary-effect-marker.md).

#### Example

Some APIs with ‘unsafe’ in their names are actually annotated with `@safe`. For example, invoking `Array.withUnsafeBytes(_:)` does not require an `unsafe` marker when `-strict-memory-safety` is specified:

```swift
func process(_ values: [UInt8]) {
  // warning: no unsafe operations occur within 'unsafe' expression
  unsafe values.withUnsafeBytes { _ in
    print("Processing \(values.count) bytes")
  }
}
```

The call to `withUnsafeBytes(_:)` by itself is safe and the closure body performs no unsafe operations, so the outer `unsafe` is unnecessary. The unsafe operation would be using the buffer’s pointer inside the closure, which can be acknowledged closer to the source of the unsafety.

#### How to fix

Remove the `unsafe` marker from the outer expression. If a use inside the closure is the actually-unsafe operation, mark only that use:

```swift
func process(_ values: [UInt8]) {
  values.withUnsafeBytes { buffer in
    let first = unsafe buffer.first ?? 0
    print("First byte: \(first)")
  }
}
```

## See Also

### Related Documentation
- [Unnecessary effect markers (UnnecessaryEffectMarker)](./unnecessary-effect-marker.md)
- [Strict memory safety (StrictMemorySafety)](./strict-memory-safety.md)
  Warnings that identify the use of language constructs and library APIs that can undermine memory safety, disabled by default.
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/unnecessary-unsafe)*