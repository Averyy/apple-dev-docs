# customReaction

**Framework**: App Intents  
**Kind**: property

An enum schema for a custom reaction parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var customReaction: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `messages` domain and a parameter type matches the `customReaction` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .messages.customReaction)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `customReaction` schema:

```swift
@AppEnum(schema: .messages.customReaction)
enum Tapback: String {
    case <#Tapback Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var conversationAttribute: some AppSchemaEnum](appschema/messagesenum/conversationattribute.md)
  An enum schema for a conversation attribute parameter.
- [var messageAttribute: some AppSchemaEnum](appschema/messagesenum/messageattribute.md)
  An enum schema for a message attribute parameter.
- [var messageEffect: some AppSchemaEnum](appschema/messagesenum/messageeffect.md)
  An enum schema for a message effect parameter.
- [var messageType: some AppSchemaEnum](appschema/messagesenum/messagetype.md)
  An enum schema for a message type parameter.
- [AppSchema.MessagesEnum](appschema/messagesenum.md)
  Identifies enum schemas in the messages domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/messagesenum/customreaction)*