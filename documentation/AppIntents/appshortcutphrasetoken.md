# AppShortcutPhraseToken

**Framework**: App Intents  
**Kind**: enum

Dynamic values you can include in the spoken phrases that run your shortcut.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
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

- [func appendLiteral(String)](appshortcutphrase/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
- [func appendInterpolation<Value, Subject>(Subject)](appshortcutphrase/stringinterpolation/appendinterpolation(_:)-5kcab.md)
- [func appendInterpolation(AppShortcutPhraseToken)](appshortcutphrase/stringinterpolation/appendinterpolation(_:)-47gqg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrasetoken)*