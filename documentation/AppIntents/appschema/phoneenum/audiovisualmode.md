# audioVisualMode

**Framework**: App Intents  
**Kind**: property

An enum schema for an audio visual mode parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var audioVisualMode: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `phone` domain and a parameter type matches the `audioVisualMode` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .phone.audioVisualMode)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `audioVisualMode` schema:

```swift
@AppEnum(schema: .phone.audioVisualMode)
enum CallAVMode: String {
    case audio
    case video

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .audio: "Audio",
        .video: "Video"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [AppSchema.PhoneEnum](appschema/phoneenum.md)
  Identifies enum schemas in the phone domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/phoneenum/audiovisualmode)*