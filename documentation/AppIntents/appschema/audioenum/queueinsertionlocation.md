# queueInsertionLocation

**Framework**: App Intents  
**Kind**: property

An enum schema for a queue insertion location parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var queueInsertionLocation: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `audio` domain and a parameter type matches the `queueInsertionLocation` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .audio.queueInsertionLocation)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `queueInsertionLocation` schema:

```swift
@AppEnum(schema: .audio.queueInsertionLocation)
enum QueueInsertionLocation: String {
    case next
    case tail

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .next: "Next",
        .tail: "Tail"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var activity: some AppSchemaEnum](appschema/audioenum/activity.md)
  An enum schema for an activity parameter.
- [var affinityState: some AppSchemaEnum](appschema/audioenum/affinitystate.md)
  An enum schema for an affinity state parameter.
- [var appViewIdentifier: some AppSchemaEnum](appschema/audioenum/appviewidentifier.md)
  An enum schema for an app view identifier parameter.
- [var invocationSource: some AppSchemaEnum](appschema/audioenum/invocationsource.md)
  An enum schema for an invocation source parameter.
- [var playbackAttributes: some AppSchemaEnum](appschema/audioenum/playbackattributes.md)
  An enum schema for a playback attributes parameter.
- [AppSchema.AudioEnum](appschema/audioenum.md)
  Identifies enum schemas in the audio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audioenum/queueinsertionlocation)*