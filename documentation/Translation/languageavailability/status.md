# LanguageAvailability.Status

**Framework**: Translation  
**Kind**: enum

The availability status for a language or language pairing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
enum Status
```

#### Overview

A language must download and install before you can use it in a translation.

## Topics

### Enumeration Cases
- [LanguageAvailability.Status.installed](languageavailability/status/installed.md)
  The framework supports the language or language pairing and has it downloaded and ready for use in a translation.
- [LanguageAvailability.Status.supported](languageavailability/status/supported.md)
  The framework supports the language or language pairing, but can’t yet use it.
- [LanguageAvailability.Status.unsupported](languageavailability/status/unsupported.md)
  The framework doesn’t support the language or language pairing.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func status(from: Locale.Language, to: Locale.Language?) async -> LanguageAvailability.Status](languageavailability/status(from:to:).md)
  Checks for the installation of a specific language pairing and whether it’s ready for translation.
- [func status(for: String, to: Locale.Language?) async throws -> LanguageAvailability.Status](languageavailability/status(for:to:).md)
  Checks to see if the framework supports the language pairing based off a string of sample text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/status)*