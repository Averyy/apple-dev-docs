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

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct AppShortcut](appshortcut.md)
  A type that defines a preconfigured shortcut for a specific app intent.
- [struct AppShortcutPhrase](appshortcutphrase.md)
  A spoken phrase that causes the system to run the corresponding App Shortcut.
- [struct NegativeAppShortcutPhrase](negativeappshortcutphrase.md)
  An object that represents a negative phrase.
- [struct NegativeAppShortcutPhrases](negativeappshortcutphrases.md)
  This is a set of negative phrases, which will all be added to the app-level negative training set. All the training data specified here, will be used to completely bypass your app
- [NSAppIconActionTintColorName](../BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/NSAppIconActionTintColorName.md)
  The tint color to apply to text and symbols in the App Shortcuts platter.
- [NSAppIconComplementingColorNames](../BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon/NSAppIconComplementingColorNames.md)
  The names of the colors to use for the background of the App Shortcuts platter.
- [enum AppShortcutsBuilder](appshortcutsbuilder.md)
  A result builder that allows you to declaratively describe the App Shortcuts that your app provides.
- [enum ShortcutTileColor](shortcuttilecolor.md)
  Describes the colors a shortcut tile in the Shortcuts app.
- [protocol AppShortcutsContent](appshortcutscontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrasetoken)*