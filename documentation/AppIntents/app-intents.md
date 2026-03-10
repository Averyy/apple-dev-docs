# App intents

**Framework**: App Intents

Define the custom actions your app exposes to the system using specialized intents.

#### Overview

Use app intents to express your app’s capabilities to the system. An app intent includes the code you need to perform an action, and expresses the data you require from the system. The system exposes your actions directly from the Shortcuts app and in system experiences like Siri.

To define an action, create a type that adopts the [`AppIntent`](appintent.md) protocol, or a related protocol that provides the specific behavior you need. Annotate any key properties with the `@Parameter` property wrapper to let the system know you need the associated information to perform the action.

The system uses intent attributes like [`title`](appintent/title.md) and [`description`](appintent/description.md) to inform people about your intent’s functionality in the Shortcuts app. Supplement this information with [`IntentDescription`](intentdescription.md) metadata, and provide additional context through human-readable explanations of your intent’s functionality, including category information and search keywords. This metadata helps your intents appear in interfaces like the Shortcuts app and improves their discoverability.

For more information about features App Intents enables, see [`Making actions and content discoverable and widely available`](making-actions-and-content-discoverable-and-widely-available.md).

## Topics

### General actions
- [protocol AppIntent](appintent.md)
  An interface for providing an app-specific capability that people invoke from system experiences like Siri and the Shortcuts app.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
### Specialized actions
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
- [protocol ForegroundContinuableIntent](foregroundcontinuableintent.md)
  A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.
- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.
- [protocol SnippetIntent](snippetintent.md)
  An app intent that presents an interactive snippet onscreen.
- [protocol SystemIntent](systemintent.md)
  Designates intent types provided by App Intents.
- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)
- [protocol UISceneAppIntent](uisceneappintent.md)
- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An app intent with a URL representation.
### Media actions
- [protocol AudioPlaybackIntent](audioplaybackintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol AudioRecordingIntent](audiorecordingintent.md)
  An app intent that starts, stops or otherwise modifies audio recording state.
- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.
### Communication actions
- [protocol PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
  An intent that begins or ends an audio transmission with the Push to Talk framework.
### Controls, widgets, and Live Activities
- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.
### SiriKit intent migration
- [protocol CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
  An interface for replacing a custom SiriKit intent that allows existing shortcuts and donations to continue working.

## See Also

- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.
- [Intent infrastructure](intent-infrastructure.md)
  Provide supplemental context for your intents, and create infrastructure to make app intents reusable across your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-intents)*