# stopwatch

**Framework**: App Intents  
**Kind**: property

An entity schema for a stopwatch.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stopwatch: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `clock` domain and its content matches the `stopwatch` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .clock.stopwatch)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `stopwatch` schema:

```swift
@AppEntity(schema: .clock.stopwatch)
struct StopwatchEntity {
    // MARK: Static

    static let defaultQuery = StopwatchEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var laps: [Duration]

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct StopwatchEntityQuery: EntityQuery {
        func entities(for identifiers: [StopwatchEntity.ID]) async throws -> [StopwatchEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/clockentity/stopwatch)*