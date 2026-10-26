---
url: "https://docs.swift.org/latest/documentation/diagnostics/foreign-reference-type"
framework: "Swift-Org/diagnostics"
---

# Foreign reference types (ForeignReferenceType)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings related to foreign reference types imported from C and C++.

#### Overview

Swift imports C and C++ types annotated with `SWIFT_SHARED_REFERENCE` as *foreign reference types* (FRTs). Their memory is managed in a similar manner to native Swift classes: the compiler automatically inserts calls to retain and release operations that maintain an FRT’s reference count.

When a Swift program calls a foreign function returning an FRT, the compiler relies on ownership convention annotations to determine whether it needs to insert a retain call on behalf of the Swift program:

- `SWIFT_RETURNS_RETAINED` means the FRT is returned as an owned object (+1 reference count)
- `SWIFT_RETURNS_UNRETAINED` means the FRT is returned as an unowned object (+0 reference count)

Without these annotations, the compiler can generate code with a superfluous or missing retain call that leads to memory leaks and errors, so it emits the following warning:

```
warning: cannot infer ownership of foreign reference value returned by 'returnsFRT()'
```

#### Fixing the warning

To address these warnings, you should add the appropriate annotation to your C or C++ function declaration:

```cpp
// Returns a retained (+1) object
SWIFT_RETURNS_RETAINED MyFRT* createObject();

// Returns an unretained (+0) object
SWIFT_RETURNS_UNRETAINED MyFRT* getExistingObject();
```

Objective-C and Objective-C++ methods can be similarly annotated:

```objc
// Returns a retained (+1) object
- (MyFRT *)createObject SWIFT_RETURNS_RETAINED;

// Returns an unretained (+0) object
- (MyFRT *)getExistingObject SWIFT_RETURNS_UNRETAINED;
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/foreign-reference-type)*