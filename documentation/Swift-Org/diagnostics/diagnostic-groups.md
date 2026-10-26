---
url: "https://docs.swift.org/latest/documentation/diagnostics/diagnostic-groups"
framework: "Swift-Org/diagnostics"
---

# Diagnostic groups

**Framework**: Swift-Org/diagnostics

Detailed explanations for various compiler diagnostics.

#### Overview

Diagnostic groups collect some number of diagnostics together under a common group name. This allows for extra documentation to help explain relevant language concepts, as well as the ability to control the behavior of warnings in a more precise manner (when that group contains warnings):

- `-Werror <group>` - upgrades warnings in the specified group to errors
- `-Wwarning <group>` - indicates that warnings in the specified group should remain warnings, even if they were previously upgraded to errors

As a concrete example, to upgrade deprecated declaration warnings to errors:

```sh
-Werror DeprecatedDeclaration
```

Or upgrade all warnings except deprecated declaration to errors:

```sh
-warnings-as-errors -Wwarning DeprecatedDeclaration
```

#### Groups with warnings

- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
- [Compilation caching (CompilationCaching)](./compilation-caching.md)
- [Conforming to `StringInterpolationProtocol` (StringInterpolationConformance)](./string-interpolation-conformance.md)
- [Deprecated declaration warnings (DeprecatedDeclaration)](./deprecated-declaration.md)
- [Deprecated implementation-only imports (ImplementationOnlyDeprecated)](./implementation-only-deprecated.md)
- [Dynamic exclusivity (DynamicExclusivity)](./dynamic-exclusivity.md)
- [Embedded Swift language restrictions (EmbeddedRestrictions)](./embedded-restrictions.md)
- [Existential Types and Performance (ExistentialType)](./existential-type.md)
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
- [Extraneous @preconcurrency imports (PreconcurrencyImport)](./preconcurrency-import.md)
- [Foreign reference types (ForeignReferenceType)](./foreign-reference-type.md)
- [Implicit Copy On Return (ReturnTypeImplicitCopy)](./return-type-implicit-copy.md)
- [Implicit strong captures of weak capture list items (ImplicitStrongCapture)](./implicit-strong-capture.md)
- [Imported Clang declaration warnings (ClangDeclarationImport)](./clang-declaration-import.md)
- [Inconsistent import access level (InconsistentImportAccess)](./inconsistent-import-access.md)
- [Isolated conformances (IsolatedConformances)](./isolated-conformances.md)
- [Language mode and tools version (ErrorInFutureSwiftVersion)](./error-in-future-swift-version.md)
- [Migrating away from experimental suppressed associated types (OldSuppressedAssociatedTypes)](./old-suppressed-associatedtypes.md)
- [Missing module version (ModuleVersionMissing)](./module-version-missing.md)
- [Module self-import (ModuleSelfImport)](./module-self-import.md)
- [OSLog module (OSLog)](./oslog.md)
- [Option obsoleted by module selectors (OptionObsoletedByModuleSelectors)](./option-obsoleted-by-module-selectors.md)
- [Result builder methods (ResultBuilderMethods)](./result-builder-methods.md)
- [SPI import ignored (SPIImportIgnored)](./spi-import-ignored.md)
- [Semantic copies (SemanticCopies)](./semantic-copies.md)
- [Strict language feature enablement (StrictLanguageFeatures)](./strict-language-features.md)
- [Strict memory safety (StrictMemorySafety)](./strict-memory-safety.md)
- [Unavailable Sendable conformance (UnavailableSendableConformance)](./unavailable-sendable-conformance.md)
- [Unknown warning group (UnknownWarningGroup)](./unknown-warning-group.md)
- [Unnecessary effect markers (UnnecessaryEffectMarker)](./unnecessary-effect-marker.md)
- [Unnecessary unsafe (UnnecessaryUnsafe)](./unnecessary-unsafe.md)
- [Unsupported scoped import (UnsupportedScopedImport)](./unsupported-scoped-import.md)
- [Untyped throws (UntypedThrows)](./untyped-throws.md)
- [Unused import access level (UnusedImportAccess)](./unused-import-access.md)
- [Unused throwing unstructured task creation (NoUseUnstructuredThrowingTask)](./no-use-throwing-unstructured-task.md)
- [Unused values (NoUsage)](./no-usage.md)
- [Use anyAppleOS availability (UseAnyAppleOSAvailability)](./use-any-apple-os-availability.md)
- [Useless availability check (UselessAvailabilityCheck)](./useless-availability-check.md)
- [Useless conditional statement (UselessConditionalStatement)](./useless-conditional-statement.md)
- [Variable never mutated (VariableNeverMutated)](./variable-never-mutated.md)

## Topics

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
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.
- [Extraneous @preconcurrency imports (PreconcurrencyImport)](./preconcurrency-import.md)
  Warnings that diagnose `@preconcurrency import` declarations that don’t need `@preconcurrency`, experimental and disabled by default.
- [Foreign reference types (ForeignReferenceType)](./foreign-reference-type.md)
  Warnings related to foreign reference types imported from C and C++.
- [Getting non-Sendable values out of actors (NonSendableExitingActor)](./getting-non-sendable-values-out-of-actors.md)
- [Implicit Copy On Return (ReturnTypeImplicitCopy)](./return-type-implicit-copy.md)
- [Implicit strong captures of weak capture list items (ImplicitStrongCapture)](./implicit-strong-capture.md)
- [Imported Clang declaration warnings (ClangDeclarationImport)](./clang-declaration-import.md)
  Covers all warnings related to malformed APIs that are imported into Swift from C, C++, and Obj-C headers.
- [Inconsistent import access level (InconsistentImportAccess)](./inconsistent-import-access.md)
- [Isolated conformances (IsolatedConformances)](./isolated-conformances.md)
- [Language mode and tools version (ErrorInFutureSwiftVersion)](./error-in-future-swift-version.md)
- [Migrating away from experimental suppressed associated types (OldSuppressedAssociatedTypes)](./old-suppressed-associatedtypes.md)
  [SE-503](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0503-suppressed-associated-types.md) officially introduced the ability to define protocols with associated types that are `~Copyable` and/or `~Escapable` (i.e., “suppressed”), which relaxes the requirement on types conforming to that protocol. During the evolution process, a prototype version of this feature existed under the experimental feature named `SuppressedAssociatedTypes`. **That experimental feature is now deprecated** and is source-incompatible with the accepted version detailed in SE-503.
- [Missing module on known path from a dependency (MissingModuleOnKnownPaths)](./missing-module-on-known-paths.md)
  Notes related to information about a missing module dependency.
- [Missing module version (ModuleVersionMissing)](./module-version-missing.md)
  Warnings that indicate the compiler cannot resolve an `#if canImport(<ModuleName>, _version: <version>)` directive because the module found was not built with a `-user-module-version` flag.
- [Module not testable (ModuleNotTestable)](./module-not-testable.md)
- [Module self-import (ModuleSelfImport)](./module-self-import.md)
- [Multiple inheritance (MultipleInheritance)](./multiple-inheritance.md)
- [Nominal types (NominalTypes)](./nominal-types.md)
- [Non-Sendable types and Objective-C interoperability (NonSendableObjCInterop)](./non-sendable-types-and-objective-c-interoperability.md)
- [Non-Sendable values in async conformances and overrides (NonSendableInAsyncConformanceOrOverride)](./non-sendable-values-in-async-conformances-and-overrides.md)
- [OSLog module (OSLog)](./oslog.md)
  The `OSLog` module defines logging facilities that integrate with the Swift compiler. This module is provided by the platform vendor and integrates with the system logging facilities. The Swift `OSLog` module should provide a module-scope variable declaration that specifies which section the logging strings should be emitted into. For example:
- [Option obsoleted by module selectors (OptionObsoletedByModuleSelectors)](./option-obsoleted-by-module-selectors.md)
  Warnings that indicate a compiler option has been obsoleted by the module selectors feature ([SE-0491](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0491-module-selectors.md)).
- [Overlapping accesses, but operation requires exclusive access (ExclusivityViolation)](./exclusivity-violation.md)
- [Performance Hints (PerformanceHints)](./performance-hints.md)
- [Property wrapper implementation requirements (PropertyWrappers)](./property-wrapper-requirements.md)
- [Protocol conformances crossing into actor-isolated code (ConformanceIsolation)](./conformance-isolation.md)
- [Protocol types cannot conform to protocols (ProtocolTypeNonConformance)](./protocol-type-non-conformance.md)
- [Result builder methods (ResultBuilderMethods)](./result-builder-methods.md)
- [SPI import ignored (SPIImportIgnored)](./spi-import-ignored.md)
- [Semantic copies (SemanticCopies)](./semantic-copies.md)
  Experimental
- [Sendable metatypes (SendableMetatypes)](./sendable-metatypes.md)
- [Sending closure risks causing data races (SendingClosureRisksDataRace)](./sending-closure-risks-data-race.md)
- [Sending value risks causing data races (SendingRisksDataRace)](./sending-risks-data-race.md)
- [Strict language feature enablement (StrictLanguageFeatures)](./strict-language-features.md)
  Warnings for unrecognized feature names in `-enable-upcoming-feature` or `enable-experimental-feature`.
- [Strict memory safety (StrictMemorySafety)](./strict-memory-safety.md)
  Warnings that identify the use of language constructs and library APIs that can undermine memory safety, disabled by default.
- [Temporary pointers (TemporaryPointers)](./temporary-pointers.md)
- [Unable to conform to Sendable with a non-Sendable superclass (NonSendableSuperclass)](./non-sendable-superclass.md)
- [Unavailable Sendable conformance (UnavailableSendableConformance)](./unavailable-sendable-conformance.md)
- [Underlying type inference for opaque result types (OpaqueTypeInference)](./opaque-type-inference.md)
- [Unknown warning group (UnknownWarningGroup)](./unknown-warning-group.md)
  Warnings for unrecognized warning groups specified in `-Wwarning` or `-Werror`.
- [Unnecessary effect markers (UnnecessaryEffectMarker)](./unnecessary-effect-marker.md)
- [Unnecessary unsafe (UnnecessaryUnsafe)](./unnecessary-unsafe.md)
- [Unrecognized availability platforms (AvailabilityUnrecognizedName)](./availability-unrecognized-name.md)
  Warnings that identify unrecognized platform names in `@available` attributes and `if #available` statements.
- [Unsafe mutable global and static variables (MutableGlobalVariable)](./mutable-global-variable.md)
- [Unsupported scoped import (UnsupportedScopedImport)](./unsupported-scoped-import.md)
- [Untyped throws (UntypedThrows)](./untyped-throws.md)
  A Swift function can declare that it can throw an error using `throws`, optionally providing a specific thrown error type:
- [Unused import access level (UnusedImportAccess)](./unused-import-access.md)
- [Unused throwing unstructured task creation (NoUseUnstructuredThrowingTask)](./no-use-throwing-unstructured-task.md)
- [Unused values (NoUsage)](./no-usage.md)
- [Use anyAppleOS availability (UseAnyAppleOSAvailability)](./use-any-apple-os-availability.md)
  An opt-in warning that suggests replacing a group of per-platform `@available` specifications with a single `anyAppleOS` specification when the platforms share the same introduced version.
- [Useless availability check (UselessAvailabilityCheck)](./useless-availability-check.md)
  Warnings that identify `if #available` queries that are guaranteed to succeed because an enclosing scope already restricts availability.
- [Useless conditional statement (UselessConditionalStatement)](./useless-conditional-statement.md)
  Warnings that identify conditional statements (`if`, `while`, and `guard`) whose conditions can never be false.
- [Using protocol members with references to `Self` or `Self`-rooted associated types (ExistentialMemberAccess)](./existential-member-access-limitations.md)
  Protocol requirements and protocol extension members may be accessed via a conformance constraint on a generic parameter, an opaque result type, or via the protocol type itself:
- [Variable never mutated (VariableNeverMutated)](./variable-never-mutated.md)
  Warnings that identify local `var` bindings which are never mutated after initialization and could instead be declared with `let`.

## See Also

- [Upcoming language features](./upcoming-language-features.md)
  Upcoming language features enable new (but potentially source breaking) functionality that be enabled by default in an upcoming language mode.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/diagnostic-groups)*