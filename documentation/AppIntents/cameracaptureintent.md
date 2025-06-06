# CameraCaptureIntent

**Framework**: App Intents  
**Kind**: protocol

Designates intent that will launch an activity that uses device’s camera to capture photos or videos. Marking your intent with this protocol makes it available as a possible action for Camera quick action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
protocol CameraCaptureIntent : SystemIntent
```

## Topics

### Associated Types
- [associatedtype AppContext : Decodable, Encodable, Sendable = Never](cameracaptureintent/appcontext-swift.associatedtype.md)
  Container type used for storing and retrieving app specific information that can be accessed whenever (and wherever) this intent gets run
### Type Properties
- [static var appContext: Self.AppContext?](cameracaptureintent/appcontext-swift.type.property.md)
  An app context that an app can use to pass necessary information to the sandboxed capture extension. The system will retrieve this app context when necessary and inject it for use during
### Type Methods
- [static func updateAppContext(Self.AppContext?) async throws](cameracaptureintent/updateappcontext(_:).md)
  Whenever the in-app context for this intent changes any process containing this intent can call this method to provide updated state to the system.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cameracaptureintent)*