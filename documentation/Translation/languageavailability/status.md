# LanguageAvailability.Status

**Framework**: Translation  
**Kind**: enum

The availability status for a language or language pairing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
enum Status
```

#### Overview

A language must download and install before you can use it in a translation.

## Topics

### Operators
- [static func == (LanguageAvailability.Status, LanguageAvailability.Status) -> Bool](languageavailability/status/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [LanguageAvailability.Status.installed](languageavailability/status/installed.md)
  A language or language pairing the framework supports, has downloaded and made ready for use in a translation.
- [LanguageAvailability.Status.supported](languageavailability/status/supported.md)
  A language or language pairing the framework supports but can’t yet use.
- [LanguageAvailability.Status.unsupported](languageavailability/status/unsupported.md)
  A language or language pairing the framework doesn’t support.
### Instance Properties
- [var hashValue: Int](languageavailability/status/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](languageavailability/status/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](languageavailability/status/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func status(from: Locale.Language, to: Locale.Language?) async -> LanguageAvailability.Status](languageavailability/status(from:to:).md)
  Checks to see if a specific language pairing is installed and ready for translation.
- [func status(for: String, to: Locale.Language?) async throws -> LanguageAvailability.Status](languageavailability/status(for:to:).md)
  Checks to see if a language pairing is supported based off a string of sample text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/status)*