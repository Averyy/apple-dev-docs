# alarm

**Framework**: App Intents  
**Kind**: property

An entity schema for an alarm.

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
var alarm: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `clock` domain and its content matches the `alarm` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .clock.alarm)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `alarm` schema:

```swift
@AppEntity(schema: .clock.alarm)
struct AlarmEntity {
    // MARK: Static

    static let defaultQuery = AlarmEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var time: DateComponents
    var isEnabled: Bool
    var label: String?
    var recurrenceDays: Calendar.RecurrenceRule?
    var canSnooze: Bool
    var triggerState: <#AlarmTriggerState#>

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

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

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var timer: some AppSchemaEntity](appschema/clockentity/timer.md)
  An entity schema for a timer.
- [AppSchema.ClockEntity](appschema/clockentity.md)
  Identifies entity schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity/alarm)*