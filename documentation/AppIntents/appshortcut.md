# AppShortcut

**Framework**: App Intents  
**Kind**: struct

A type that defines a preconfigured shortcut for a specific app intent.

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
struct AppShortcut
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

> **Note**:  Session 10170: [`Implement App Shortcuts with App Intents`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10170), and session 10169: [`Design App Shortcuts`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10169).

> **Note**: Apple may extract anonymized App Shortcuts data such as localized phrases, display representation values, and the title and description of related intents. Machine learning models use this data when training to help improve the App Shortcuts experience.

## Topics

### Creating an app shortcut
- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String)](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-8yntq.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.
- [init<Intent, Value, Parameter, ParameterKeyPath>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String, parameterPresentation: AppShortcutParameterPresentation<Intent, Value, Parameter, ParameterKeyPath>)](appshortcut/init(intent:phrases:shorttitle:systemimagename:parameterpresentation:).md)
  Initializes an App Shortcut with phrases that run the app intent, a title, an image, and specified parameters.
- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource?, systemImageName: String?)](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-2hk1x.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcut)*