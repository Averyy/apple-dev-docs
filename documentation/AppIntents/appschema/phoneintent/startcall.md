# startCall

**Framework**: App Intents  
**Kind**: property

An intent schema that starts a call to a person, handle, or named group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var startCall: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `phone` domain and one of your app’s actions matches the `startCall` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .phone.startCall)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `startCall` schema:

```swift
@AppIntent(schema: .phone.startCall)
struct StartCallIntent: AudioRecordingIntent, AudioStartingIntent {
    var destination: <#CallDestination#>
    var audioVisualMode: <#CallAVMode#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [AppSchema.PhoneIntent](appschema/phoneintent.md)
  Identifies intent schemas in the phone domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/phoneintent/startcall)*