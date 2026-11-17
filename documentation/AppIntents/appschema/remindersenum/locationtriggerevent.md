# locationTriggerEvent

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for a location trigger event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var locationTriggerEvent: some AppSchemaEnum { get }
```

## Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `reminders` domain and a parameter type matches the `locationTriggerEvent` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum(schema: .reminders.locationTriggerEvent)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `locationTriggerEvent` schema. You can create a type that conforms to the schema by adding the `@AppEnum` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_locationTriggerEvent` and select it from the code-completion suggestions:

```swift
@AppEnum(schema: .reminders.locationTriggerEvent)
enum LocationTriggerEvent: String {
    case arrive
    case depart

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .arrive: "Arrive",
        .depart: "Depart"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Types for static parameters
- [var listType: some AppSchemaEnum](./listtype.md)
  An enum schema for a list type.
- [AppSchema.RemindersEnum](../remindersenum.md)
  Identifies enum schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersenum/locationtriggerevent)*