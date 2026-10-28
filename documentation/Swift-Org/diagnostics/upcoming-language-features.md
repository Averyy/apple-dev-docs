---
url: "https://docs.swift.org/latest/documentation/diagnostics/upcoming-language-features"
framework: "Swift-Org/diagnostics"
---

# Upcoming language features

**Framework**: Swift-Org/diagnostics

Upcoming language features enable new (but potentially source breaking) functionality that be enabled by default in an upcoming language mode.

## Overview

Upcoming language features allow the incremental adoption of language features that would otherwise only be available in a new language mode, without having to fully migrate to that mode. They can be enabled on the command line with `-enable-upcoming-feature <feature>`.

Some upcoming features have an additional “migration” mode, where the compiler will emit warnings with fix-its to help migrate to that mode. This can be enabled with `-enable-upcoming-feature <feature>:migrate`.

## Topics

- [Existential any (ExistentialAny)](./existential-any.md)
  `any` existential type syntax.
- [Member import visibility (MemberImportVisibility)](./member-import-visibility.md)
  Enables errors for uses of members that cannot be accessed because their defining module is not directly imported.
- [nonisolated(nonsending) by Default (NonisolatedNonsendingByDefault)](./nonisolated-nonsending-by-default.md)
  Runs nonisolated async functions on the caller’s actor by default.

## See Also

- [Diagnostic groups](./diagnostic-groups.md)
  Detailed explanations for various compiler diagnostics.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/upcoming-language-features)*