# timer

**Framework**: App Intents  
**Kind**: property

An entity schema for a timer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var timer: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `clock` domain and its content matches the `timer` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .clock.timer)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `timer` schema:

```swift
@AppEntity(schema: .clock.timer)
struct TimerEntity {
    // MARK: Static

    static let defaultQuery = TimerEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var duration: Duration
    var durationRemaining: Duration
    var state: <#TimerState#>
    var label: String?
    var isSleepTimer: Bool

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

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

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var alarm: some AppSchemaEntity](appschema/clockentity/alarm.md)
  An entity schema for an alarm.
- [AppSchema.ClockEntity](appschema/clockentity.md)
  Identifies entity schemas in the clock domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity/timer)*