# startCall

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that starts a call to a person, handle, or named group.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var startCall: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `phone` domain and one of your app’s actions matches the `startCall` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .phone.startCall)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `startCall` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `phone_startCall` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .phone.startCall)
struct StartCallIntent: AudioRecordingIntent, AudioStartingIntent {
    /// Target destination for the outgoing call.
    var destination: <#CallDestination#>

    /// Call mode, either audio or video.
    var audioVisualMode: <#CallAVMode#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

Define a `@UnionValue` enumeration for the `destination` parameter, as in the following example, by typing the first few characters of `phone_destination` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum CallDestination {
    case person(<#PhonePerson#>)
    case people([<#PhonePerson#>])
    case group(<#CallGroup#>)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the start-call intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `destination` | `@UnionValue` | Your app | Target destination for the outgoing call. `CallDestination` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `audioVisualMode` | `@AppEnum(schema: .phone.audioVisualMode)` | Your app | Call mode, either audio or video. `CallAVMode` is a placeholder name for a type that conforms to the [`audioVisualMode`](../phoneenum/audiovisualmode.md) enum schema, which your app defines and implements. |

## See Also

### Actions
- [AppSchema.PhoneIntent](../phoneintent.md)
  Identifies intent schemas in the phone domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/phoneintent/startcall)*