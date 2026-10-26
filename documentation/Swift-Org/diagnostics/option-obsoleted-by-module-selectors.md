---
url: "https://docs.swift.org/latest/documentation/diagnostics/option-obsoleted-by-module-selectors"
framework: "Swift-Org/diagnostics"
---

# Option obsoleted by module selectors (OptionObsoletedByModuleSelectors)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that indicate a compiler option has been obsoleted by the module selectors feature (`0491-module-selectors.md`).

#### Overview

The module selectors feature superseded certain compiler options related to controlling the contents of generated `.swiftinterface` files. When one of these obsoleted options is passed to the compiler, it is ignored and a warning is emitted:

```
warning: ignoring '<option>'; this option has been obsoleted by module selectors (add '-disable-module-selectors-in-module-interface' to restore original behavior) [#OptionObsoletedByModuleSelectors]
```

To silence the warning, remove the obsoleted option from your build settings. If you need the original behavior that the option provided, pass `-disable-module-selectors-in-module-interface` instead.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/option-obsoleted-by-module-selectors)*