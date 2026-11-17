# alarm

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an alarm.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var alarm: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `clock` domain and its content matches the `alarm` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .clock.alarm)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `alarm` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `clock_alarm` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .clock.alarm)
struct AlarmEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more alarm entities, unless you provide another.
    static let defaultQuery = AlarmEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the alarm entity.
    let id: <#Identifiable.ID#>

    var time: DateComponents

    var isEnabled: Bool

    var label: String?

    var recurrenceDays: Calendar.RecurrenceRule?

    var canSnooze: Bool

    var triggerState: <#AlarmTriggerState#>

    /// The details the system shows to identify the alarm entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more alarm entities by their identifiers.
    struct AlarmEntityQuery: EntityQuery {
        func entities(for identifiers: [AlarmEntity.ID]) async throws -> [AlarmEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the alarm entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `time` | `DateComponents` | Foundation | Time |
| `isEnabled` | `Bool` | Swift | Is Enabled |
| `label` | `String?` | Swift | Label |
| `recurrenceDays` | `Calendar.RecurrenceRule?` | Foundation | Recurrence Days |
| `canSnooze` | `Bool` | Swift | Can Snooze |
| `triggerState` | `@AppEnum(schema: .clock.alarmTriggerState)` | Your app | Trigger State `AlarmTriggerState` is a placeholder name for a type that conforms to the [`alarmTriggerState`](../clockenum/alarmtriggerstate.md) enum schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var timer: some AppSchemaEntity](./timer.md)
  An entity schema for a timer.
- [AppSchema.ClockEntity](../clockentity.md)
  Identifies entity schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity/alarm)*