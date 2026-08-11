# App intent types

**Framework**: App Intents

Build your intents from types that define common behaviors such as opening or deleting items, playing or recording media, and more.

#### Overview

The app intents you create conform to the [`AppIntent`](appintent.md) protocol for basic features, but you can choose other protocols as an alternate starting point. You might choose a different protocol for an intent that offers a specific behavior or supports a particular capability. For example, use the [`OpenIntent`](openintent.md) protocol if your app intent launches your app and displays a specific item. These protocols also conform to the [`AppIntent`](appintent.md) protocol, giving you both the base features and the additional behaviors you need for your specific app intent.

## Topics

### Common actions
- [protocol OpenIntent](openintent.md)
  An app intent that opens and displays a specific item in your app’s interface.
- [struct OpenURLIntent](openurlintent.md)
  An app intent that opens one of your universal links and displays its contents.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
### Search
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that displays a set of search results in the app’s interface.
- [struct StringSearchCriteria](stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [enum StringSearchScope](stringsearchscope.md)
  Constants that describe the types of content your app includes in search results when the search criteria is a string.
### Universal link navigation
- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An interface you add to an app intent type so the system can handle it like a universal link.
- [struct IntentURLRepresentation](intenturlrepresentation.md)
  The type that provides the URL for an app intent.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
  An interface that allows a type to express its contents in a URL representation.
### Media actions
- [protocol AudioPlaybackIntent](audioplaybackintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol AudioRecordingIntent](audiorecordingintent.md)
  An app intent that starts, stops or otherwise modifies audio recording state.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.
- [enum VideoCategory](videocategory.md)
### Communication actions
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
  An intent that begins or ends an audio transmission with the Push to Talk framework.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that displays a set of search results in the app’s interface.
### Controls, widgets, and Live Activities
- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.
- [struct RunSystemShortcutIntent](runsystemshortcutintent.md)
  An app intent you use in widgets to open another app or perform an App Shortcut, custom shortcut, or system action.
### SiriKit intent migration
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [protocol CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
  An interface for replacing a custom SiriKit intent that allows existing shortcuts and donations to continue working.
### System support
- [protocol SystemIntent](systemintent.md)
  Designates intent types provided by App Intents.

## See Also

- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Soup Chef with App Intents: Migrating custom intents](../SiriKit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [protocol AppIntent](appintent.md)
  An interface you use to express app-specific actions and make them available to the rest of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-intent-types)*