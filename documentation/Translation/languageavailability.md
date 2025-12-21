# LanguageAvailability

**Framework**: Translation  
**Kind**: class

A check for language support and status.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
class LanguageAvailability
```

#### Overview

Use this class to check and see whether the framework supports the language or language pairing you want to offer as a translation. For example, to check if someone’s device supports a translation you can do the following:

```swift
func translationIsSupported(from source: Locale.Language, to target: Locale.Language) async -> Bool {
    let availability = LanguageAvailability()
    let status = await availability.status(from: source, to: target)
    switch status {
    case .installed, .supported:
        return true
    case .unsupported
        return false
    }
}
```

## Topics

### Creating a language availability
- [init()](languageavailability/init.md)
  Creates a language availability.
### Getting supported languages
- [var supportedLanguages: [Locale.Language]](languageavailability/supportedlanguages.md)
  A list of translation languages the framework supports.
### Checking language availability
- [func status(from: Locale.Language, to: Locale.Language?) async -> LanguageAvailability.Status](languageavailability/status(from:to:).md)
  Checks for the installation of a specific language pairing and whether it’s ready for translation.
- [func status(for: String, to: Locale.Language?) async throws -> LanguageAvailability.Status](languageavailability/status(for:to:).md)
  Checks to see if the framework supports the language pairing based off a string of sample text.
- [LanguageAvailability.Status](languageavailability/status.md)
  The availability status for a language or language pairing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability)*