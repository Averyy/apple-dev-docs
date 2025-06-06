# TypesettingLanguage

**Framework**: SwiftUI  
**Kind**: struct

Defines how typesetting language is determined for text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct TypesettingLanguage
```

#### Overview

Use a modifier like [`typesettingLanguage(_:isEnabled:)`](view/typesettinglanguage(_:isenabled:).md) to specify the typesetting language.

## Topics

### Getting language behavior
- [static let automatic: TypesettingLanguage](typesettinglanguage/automatic.md)
  Automatic language behavior.
- [static func explicit(Locale.Language) -> TypesettingLanguage](typesettinglanguage/explicit(_:).md)
  Use explicit language.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Preparing views for localization](preparing-views-for-localization.md)
  Specify hints and add strings to localize your SwiftUI views.
- [struct LocalizedStringKey](localizedstringkey.md)
  The key used to look up an entry in a strings file or strings dictionary file.
- [var locale: Locale](environmentvalues/locale.md)
  The current locale that views should use.
- [func typesettingLanguage(_:isEnabled:)](view/typesettinglanguage(_:isenabled:).md)
  Specifies the language for typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/typesettinglanguage)*