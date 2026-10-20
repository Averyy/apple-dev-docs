# playbackAttributes

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for a playback attributes parameter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var playbackAttributes: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `audio` domain and a parameter type matches the `playbackAttributes` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .audio.playbackAttributes)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `playbackAttributes` schema:

```swift
@AppEnum(schema: .audio.playbackAttributes)
enum PlaybackAttributes: String {
    case shuffle
    case repeat

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .shuffle: "Shuffle",
        .repeat: "Repeat"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Types for static parameters
- [var activity: some AppSchemaEnum](./activity.md)
  An enum schema for an activity parameter.
- [var affinityState: some AppSchemaEnum](./affinitystate.md)
  An enum schema for an affinity state parameter.
- [var appViewIdentifier: some AppSchemaEnum](./appviewidentifier.md)
  An enum schema for an app view identifier parameter.
- [var invocationSource: some AppSchemaEnum](./invocationsource.md)
  An enum schema for an invocation source parameter.
- [var queueInsertionLocation: some AppSchemaEnum](./queueinsertionlocation.md)
  An enum schema for a queue insertion location parameter.
- [AppSchema.AudioEnum](../audioenum.md)
  Identifies enum schemas in the audio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audioenum/playbackattributes)*