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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol AudioPlaybackIntent](audioplaybackintent.md)
  An App Intent that plays, pauses, or otherwise modifies audio playback state when it executes.
- [protocol AudioRecordingIntent](audiorecordingintent.md)
  An app intent that starts, stops or otherwise modifies audio recording state.
- [protocol PlayVideoIntent](playvideointent.md)
  An intent that looks for videos based on a search term, then plays the content.
- [enum VideoCategory](videocategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/cameracaptureintent)*