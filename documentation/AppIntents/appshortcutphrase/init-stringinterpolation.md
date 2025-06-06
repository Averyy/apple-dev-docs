# init(stringInterpolation:)

**Framework**: App Intents  
**Kind**: init

Creates an instance from a string interpolation.

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
init(stringInterpolation: AppShortcutPhrase<Intent>.StringInterpolation)
```

#### Discussion

Most `StringInterpolation` types will store information about the literals and interpolations appended to them in one or more properties. `init(stringInterpolation:)` should use these properties to initialize the instance.

## Parameters

- `stringInterpolation`: An instance of    which has had each segment of the string literal appended   to it.

## See Also

- [init(String)](appshortcutphrase/init(_:).md)
- [init(stringLiteral: String)](appshortcutphrase/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [AppShortcutPhrase.StringInterpolation](appshortcutphrase/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.
- [enum AppShortcutPhraseToken](appshortcutphrasetoken.md)
  Dynamic values you can include in the spoken phrases that run your shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrase/init(stringinterpolation:))*