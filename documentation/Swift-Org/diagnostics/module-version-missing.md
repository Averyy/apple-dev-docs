---
url: "https://docs.swift.org/latest/documentation/diagnostics/module-version-missing"
framework: "Swift-Org/diagnostics"
---

# Missing module version (ModuleVersionMissing)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that indicate the compiler cannot resolve an `#if canImport(<ModuleName>, _version: <version>)` directive because the module found was not built with a `-user-module-version` flag.

#### Overview

Developers may conditionalize which code is active in a source file based on the module version number of an imported dependency module, like this:

```swift
import Dependency

#if canImport(Dependency, _version: 1.2)
// Use declarations introduced in version 1.2 of Dependency
#else
// ...
#endif
```

A dependency’s module version must be established by passing the `-user-module-version` flag when compiling the sources of the dependency the module. If no `-user-module-version` flag was specified when the dependency module was built, then the compiler will warn that it cannot resolve the `#if canImport` directive:

```
warning: cannot find user version number for module 'Dependency'; version number ignored [#ModuleVersionMissing]
```

If this diagnostic is emitted, then the `#if canImport` directive implicitly evaluates true.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/module-version-missing)*