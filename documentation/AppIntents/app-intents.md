# App intents

**Framework**: App Intents

Define the custom actions your app exposes to the system, and incorporate support for existing SiriKit intents.

#### Overview

Use app intents to express your app’s capabilities to the system. An app intent includes the code you need to perform an action, and expresses the data you require from the system. The system exposes your actions directly from the Shortcuts app and in system experiences like Siri.

To define an action, create a type that adopts the [`AppIntent`](appintent.md) protocol, or a related protocol that provides the specific behavior you need. Annotate any key properties with the `@Parameter` property wrapper to let the system know you need the associated information to perform the action.

For more information about features App Intents enables, see [`Making actions and content discoverable and widely available`](making-actions-and-content-discoverable-and-widely-available.md).

## Topics

### Actions
- [protocol AppIntent](appintent.md)
  An interface for providing an app-specific capability that people invoke from system experiences like Siri and the Shortcuts app.
- [protocol AudioPlaybackIntent](audioplaybackintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol AudioRecordingIntent](audiorecordingintent.md)
  An app intent that starts, stops or otherwise modifies audio recording state.
- [protocol AudioStartingIntent](audiostartingintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol CameraCaptureIntent](cameracaptureintent.md)
  Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.
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
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
  An intent that begins or ends an audio transmission with the Push to Talk framework.
- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An app intent with a URL representation.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.
- [protocol SystemIntent](systemintent.md)
  Designates intent types provided by App Intents.
### Controls, widgets, and Live Activities
- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.
### Siri and Apple Intelligence
- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
  Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.
### SiriKit intent migration
- [protocol CustomIntentMigratedAppIntent](customintentmigratedappintent.md)
  An interface for replacing a custom SiriKit intent that allows existing shortcuts and donations to continue working.
### Dependency management
- [class AppDependencyManager](appdependencymanager.md)
  An object that manages the registration and initialization of an app intent’s dependencies.
- [class AppDependency](appdependency.md)
  A property wrapper that resolves a registered dependency at runtime.
### Supplementary content
- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.
### Results
- [protocol IntentResult](intentresult.md)
  A type that contains the result of performing an action, and includes optional information to deliver back to the initiator.
- [struct IntentResultContainer](intentresultcontainer.md)
  An object that represents the output of a completed intent.
- [protocol OpensIntent](opensintent.md)
  The result of performing an action that delivers an app intent back to the initiator of the action.
- [protocol ProvidesDialog](providesdialog.md)
  The result of performing an action that delivers a dialog back to the initiator of the action.
- [protocol ReturnsValue](returnsvalue.md)
  The result of performing an action that delivers a value back to the initiator.
- [protocol ShowsSnippetView](showssnippetview.md)
  The result of performing an action that delivers a view back to the initiator of the action.
- [protocol ResultsCollection](resultscollection.md)
  A protocol representing a collection of returned items with support for sectioning.
### Extensions
- [protocol AppIntentsExtension](appintentsextension.md)
  An interface for managing an extension’s configuration.

## See Also

- [Intent discovery](intent-discovery.md)
  Donate your app’s intents to the system to help it identify trends and predict future behaviors.
- [App Shortcuts](app-shortcuts.md)
  Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-intents)*