# AppShortcutsProvider

**Framework**: App Intents  
**Kind**: protocol

A type alias for the type that provides an app’s preconfigured shortcuts.

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
protocol AppShortcutsProvider
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

> **Note**:  Session 10170: [`Implement App Shortcuts with App Intents`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10170), and session 10169: [`Design App Shortcuts`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10169).

 Session 10170: [`Implement App Shortcuts with App Intents`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10170), and session 10169: [`Design App Shortcuts`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10169).

> **Note**: Apple may extract anonymized App Shortcuts data such as localized phrases, display representation values, and the title and description of related intents. Machine learning models use this data when training to help improve the App Shortcuts experience.

Apple may extract anonymized App Shortcuts data such as localized phrases, display representation values, and the title and description of related intents. Machine learning models use this data when training to help improve the App Shortcuts experience.

## Topics

### Providing App Shortcuts
- [static var appShortcuts: [AppShortcut]](appshortcutsprovider/appshortcuts.md)
- [enum AppShortcutsBuilder](appshortcutsbuilder.md)
  A result builder that allows you to declaratively describe the App Shortcuts that your app provides.
### Configuring shortcut tiles
- [static var shortcutTileColor: ShortcutTileColor](appshortcutsprovider/shortcuttilecolor.md)
  The background color of the tile that Shortcuts displays for each of the app’s App Shortcuts.
- [enum ShortcutTileColor](shortcuttilecolor.md)
  Describes the colors a shortcut tile in the Shortcuts app.
### Updating stored parameters
- [static func updateAppShortcutParameters()](appshortcutsprovider/updateappshortcutparameters.md)
### Type Aliases
- [AppShortcutsProvider.OptionsCollection](appshortcutsprovider/optionscollection.md)
- [AppShortcutsProvider.ParameterPresentation](appshortcutsprovider/parameterpresentation.md)
- [AppShortcutsProvider.Summary](appshortcutsprovider/summary.md)
- [AppShortcutsProvider.Title](appshortcutsprovider/title.md)
### Type Properties
- [static var negativePhrases: NegativeAppShortcutPhrases](appshortcutsprovider/negativephrases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutsprovider)*