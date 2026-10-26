---
url: "https://docs.swift.org/latest/documentation/diagnostics/missing-module-on-known-paths"
framework: "Swift-Org/diagnostics"
---

# Missing module on known path from a dependency (MissingModuleOnKnownPaths)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Notes related to information about a missing module dependency.

#### Overview

This diagnostic group covers notes related to displaying information about a missing module dependency which the compiler is able to locate as present on a search path found in a loaded Swift binary module, but which is not specified to the current compilation.

As one example of a potential missing module diagnostic, suppose an imported module `Foo` is resolved to a Swift binary module which itself depends on module `Bar` and was built with an additional search path where `Bar` is located, and suppose that the client which imports `Foo` does not specify this search path:

```
import Foo
```

The Swift compiler would emit a module-not-found error and a note to inform the user of the missing search path containing `Bar` which was found serialized in `Foo`’s binary Swift module:

```
error: Compilation search paths unable to resolve module dependency: 'Bar' [#MissingModuleOnKnownPaths]
note: 'Bar' can be found using a search path that was specified when building module 'Foo' ('<Search Path>'). This search path was not specified on the current compilation.
```

Some prior versions of the Swift compiler erroneously inherited search paths from loaded binary Swift modules and used them to resolve other, subsequently-encountered module dependencies. All search paths required to resolve direct and transitive module dependencies must be explicitly specified on the compiler invocation which will encounter these dependencies.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/missing-module-on-known-paths)*