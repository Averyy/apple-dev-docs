# AppShortcutPhraseToken

**Framework**: App Intents  
**Kind**: enum

Dynamic values you can include in the spoken phrases that run your shortcut.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum AppShortcutPhraseToken
```

## Topics

### Getting the tokens
- [AppShortcutPhraseToken.applicationName](appshortcutphrasetoken/applicationname.md)
### Operators
- [static func == (AppShortcutPhraseToken, AppShortcutPhraseToken) -> Bool](appshortcutphrasetoken/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](appshortcutphrasetoken/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](appshortcutphrasetoken/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](appshortcutphrasetoken/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(String)](appshortcutphrase/init(_:).md)
- [init(stringLiteral: String)](appshortcutphrase/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: AppShortcutPhrase<Intent>.StringInterpolation)](appshortcutphrase/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [AppShortcutPhrase.StringInterpolation](appshortcutphrase/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrasetoken)*