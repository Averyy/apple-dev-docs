# AppShortcutsContent

**Framework**: App Intents  
**Kind**: protocol

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
protocol AppShortcutsContent
```

## Topics

### Instance Properties
- [var appShortcuts: [AppShortcut]](appshortcutscontent/appshortcuts.md)

## See Also

- [struct AppShortcut](appshortcut.md)
  A type that defines a preconfigured shortcut for a specific app intent.
- [struct AppShortcutPhrase](appshortcutphrase.md)
  A spoken phrase that causes the system to run the corresponding App Shortcut.
- [enum AppShortcutPhraseToken](appshortcutphrasetoken.md)
  Dynamic values you can include in the spoken phrases that run your shortcut.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutscontent)*