# PushToTalkTransmissionIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that begins or ends an audio transmission with the Push to Talk framework.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS ?+

## Declaration

```swift
protocol PushToTalkTransmissionIntent : SystemIntent
```

#### Overview

Create an app intent that confirms to this protocol to manually start or end an audio transmission that uses the Push to Talk framework. For additional information about transmitting audio with the Push to Talk framework, see [`Push to Talk`](https://developer.apple.com/documentation/PushToTalk).

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

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
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An app intent with a URL representation.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/pushtotalktransmissionintent)*