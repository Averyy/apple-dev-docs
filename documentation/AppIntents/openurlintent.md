# OpenURLIntent

**Framework**: App Intents  
**Kind**: struct

An intent that opens a universal link.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct OpenURLIntent
```

#### Overview

Return an `OpenURLIntent` as the [`IntentResult`](intentresult.md) of another app intent’s [`perform()`](appintent/perform().md) method or use place the intent on a button that appears on an interactive widget or Live Activity.

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Initializers
- [init()](openurlintent/init.md)
  Creates an app intent.
- [init(URL)](openurlintent/init(_:).md)
- [init(urlRepresentable: some URLRepresentableEnum) throws](openurlintent/init(urlrepresentable:)-53fa0.md)
- [init(urlRepresentable: some URLRepresentableEntity) async throws](openurlintent/init(urlrepresentable:)-8r4bl.md)
### Instance Properties
- [var $url: IntentParameter<URL>](openurlintent/$url.md)
- [var url: URL](openurlintent/url.md)
### Type Aliases
- [OpenURLIntent.PerformResult](openurlintent/performresult.md)
- [OpenURLIntent.SummaryContent](openurlintent/summarycontent.md)
  The type of parameter summary representing this intent.
### Type Properties
- [static var title: LocalizedStringResource](openurlintent/title.md)
  A short, localized, human-readable string that describes the app intent using a verb and a noun in title case.
- [static var urlRepresentation: OpenURLIntent.URLRepresentation](openurlintent/urlrepresentation.md)
### Default Implementations
- [AppIntent Implementations](openurlintent/appintent-implementations.md)
- [PersistentlyIdentifiable Implementations](openurlintent/persistentlyidentifiable-implementations.md)
- [URLRepresentableIntent Implementations](openurlintent/urlrepresentableintent-implementations.md)

## Relationships

### Conforms To
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SystemIntent](systemintent.md)
- [URLRepresentableIntent](urlrepresentableintent.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent)*