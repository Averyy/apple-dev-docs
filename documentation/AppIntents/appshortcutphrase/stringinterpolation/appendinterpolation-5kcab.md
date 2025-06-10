# appendInterpolation(_:)

**Framework**: App Intents  
**Kind**: method

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
mutating func appendInterpolation<Value, Subject>(_ subject: Subject) where Value : _IntentValue, Value : Sendable, Subject : KeyPath<Intent, IntentParameter<Value>>
```

## See Also

- [func appendLiteral(String)](appshortcutphrase/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
- [func appendInterpolation(AppShortcutPhraseToken)](appshortcutphrase/stringinterpolation/appendinterpolation(_:)-47gqg.md)
- [enum AppShortcutPhraseToken](appshortcutphrasetoken.md)
  Dynamic values you can include in the spoken phrases that run your shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrase/stringinterpolation/appendinterpolation(_:)-5kcab)*