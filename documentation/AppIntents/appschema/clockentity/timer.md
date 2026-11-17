# timer

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a timer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var timer: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `clock` domain and its content matches the `timer` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .clock.timer)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `timer` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `clock_timer` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .clock.timer)
struct TimerEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more timer entities, unless you provide another.
    static let defaultQuery = TimerEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the timer entity.
    let id: <#Identifiable.ID#>

    var duration: Duration

    var durationRemaining: Duration

    var state: <#TimerState#>

    var label: String?

    var isSleepTimer: Bool

    /// The details the system shows to identify the timer entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more timer entities by their identifiers.
    struct TimerEntityQuery: EntityQuery {
        func entities(for identifiers: [TimerEntity.ID]) async throws -> [TimerEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the timer entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `duration` | `Duration` | Swift | Duration |
| `durationRemaining` | `Duration` | Swift | Duration Remaining |
| `state` | `@AppEnum(schema: .clock.timerState)` | Your app | State `TimerState` is a placeholder name for a type that conforms to the [`timerState`](../clockenum/timerstate.md) enum schema, which your app defines and implements. |
| `label` | `String?` | Swift | Label |
| `isSleepTimer` | `Bool` | Swift | Is Sleep Timer |

## See Also

### Content and parameter types
- [var alarm: some AppSchemaEntity](./alarm.md)
  An entity schema for an alarm.
- [AppSchema.ClockEntity](../clockentity.md)
  Identifies entity schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity/timer)*