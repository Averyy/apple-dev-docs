# App Shortcuts

**Framework**: App Intents

Improve the experience of using your app intents and entities in system experiences like Siri, Spotlight, and the Shortcuts app.

#### Overview

App Shortcuts provide a polished experience for your app intents and entities in the Shortcuts app and other system experiences. An App Shortcut combines the action from your app intent with other data, such as a title, image, and spoken phrases that someone might use to run the shortcut. A shortcut can also contain preconfigured parameters, so someone can run the action quickly, and without having to specify additional information. For example, a hiking app might offer an app intent to start a hike, but require you to select a trail before starting the action. Without a shortcut, someone must provide the trail information each time they run the intent. However, a shortcut can simplify this flow by offering to start a hike on the person’s favorite trail.

You create App Shortcuts programmatically in your code, and the compiler generates the information the rest of the system needs to use it. This approach means that the shortcuts you create are available as soon as someone installs your app, and you don’t have to register them yourself. Specify your shortcuts in your code by defining a custom type that adopts the [`AppShortcutsProvider`](appshortcutsprovider.md) protocol. Include this type in your app, app extension, Swift package, or library that you use to manage your intents-related code. Inside this type, construct one or more [`AppShortcut`](appshortcut.md) types using static data. Define your shortcuts in the same place you define the app intents that those shortcuts use.

> **Note**: Apple may extract anonymized App Shortcuts data such as localized phrases, display representation values, and the title and description of related intents. Machine learning models use this data when training to help improve the App Shortcuts experience.

Although the Shortcuts app and other system features find your shortcuts automatically, you can also make them available from your app using tip views. The [`SiriTipView`](siritipview.md) and [`SiriTipUIView`](siritipuiview.md) types display the relevant shortcuts for the app intent you specify. You can also use a [`ShortcutsLink`](shortcutslink.md) or [`ShortcutsUIButton`](shortcutsuibutton.md) to open your app’s page in the Shortcuts app.

## Topics

### App Shortcut management
- [protocol AppShortcutsProvider](appshortcutsprovider.md)
  A type alias for the type that provides an app’s preconfigured shortcuts.
### App Shortcut definition
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
- [protocol AppShortcutsContent](appshortcutscontent.md)
### App Shortcut options
- [struct AppShortcutOptionsCollection](appshortcutoptionscollection.md)
  Represents a collection of options for parameters of an App Shortcut.
- [protocol AppShortcutOptionsCollectionProtocol](appshortcutoptionscollectionprotocol.md)
- [protocol AppShortcutOptionsCollectionSpecification](appshortcutoptionscollectionspecification.md)
- [enum AppShortcutOptionsCollectionSpecificationBuilder](appshortcutoptionscollectionspecificationbuilder.md)
### App Shortcut parameter presentation
- [struct AppShortcutParameterPresentation](appshortcutparameterpresentation.md)
  Describes the presentation of an App Shortcut  for the provided parameter.
- [struct AppShortcutParameterPresentationSummary](appshortcutparameterpresentationsummary.md)
  The summary of the presentation of an App Shortcut parameter.
- [struct AppShortcutParameterPresentationSummaryString](appshortcutparameterpresentationsummarystring.md)
- [struct AppShortcutParameterPresentationTitle](appshortcutparameterpresentationtitle.md)
  A struct that represents the title of the presentation of an App Shortcut.
- [struct AppShortcutParameterPresentationTitleString](appshortcutparameterpresentationtitlestring.md)
### Buttons
- [class ShortcutsUIButton](shortcutsuibutton.md)
  A button that opens the current app’s page in the Shortcuts app.
- [struct ShortcutsLink](shortcutslink.md)
  A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.
- [struct ShortcutsLinkStyle](shortcutslinkstyle.md)
  The styles to apply to buttons you use to open your app’s page in the Shortcuts app.
### Tip views
- [class SiriTipUIView](siritipuiview.md)
  A view that displays the phrase a person uses to invoke an App Shortcut.
- [struct SiriTipView](siritipview.md)
  A SwiftUI view that displays the phrase someone uses to invoke an App Shortcut.
- [struct SiriTipViewStyle](siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.

## See Also

- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities so people can use your app’s content and actions across system experiences.
- [Apple Intelligence and Siri AI](apple-intelligence-and-siri-ai.md)
  Integrate your app with Apple Intelligence and bring it to Siri AI.
- [Spotlight integration](spotlight.md)
  Add your entities to your app’s Spotlight index, and automate the indexing of your content.
- [Widgets, Live Activities, and Controls](widgets-live-activities-and-controls.md)
  Implement interactive widgets, controls, watch complications, and Live Activities using app intents.
- [Hardware interactions](hardware-interactions.md)
  Run your App Shortcuts from the Action button on iPhone or Apple Watch, or launch your own conversational app from the side button on iPhone.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Visual intelligence](visual-intelligence.md)
  Match images to your app’s content and report the results to the Visual Intelligence framework using an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-shortcuts)*