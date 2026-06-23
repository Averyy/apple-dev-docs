# listType

**Framework**: App Intents  
**Kind**: property

An enum schema for a list type parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var listType: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `reminders` domain and a parameter type matches the `listType` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .reminders.listType)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `listType` schema:

```swift
@AppEnum(schema: .reminders.listType)
enum ListType: String {
    case standard

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .standard: "Standard"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var locationTriggerEvent: some AppSchemaEnum](appschema/remindersenum/locationtriggerevent.md)
  An enum schema for a location trigger event parameter.
- [AppSchema.RemindersEnum](appschema/remindersenum.md)
  Identifies enum schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersenum/listtype)*