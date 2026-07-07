# locationTrigger

**Framework**: App Intents  
**Kind**: property

An entity schema for a location trigger.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var locationTrigger: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reminders` domain and its content matches the `locationTrigger` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .reminders.locationTrigger)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `locationTrigger` schema:

```swift
@AppEntity(schema: .reminders.locationTrigger)
struct LocationTriggerEntity {
    // MARK: Static

    static let defaultQuery = LocationTriggerEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var place: GeoToolbox.PlaceDescriptor
    var event: <#LocationTriggerEvent#>

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct LocationTriggerEntityQuery: EntityQuery {
        func entities(for identifiers: [LocationTriggerEntity.ID]) async throws -> [LocationTriggerEntity] {
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

- [var group: some AppSchemaEntity](appschema/remindersentity/group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](appschema/remindersentity/list.md)
  An entity schema for a list.
- [var reminder: some AppSchemaEntity](appschema/remindersentity/reminder.md)
  An entity schema for a reminder.
- [var section: some AppSchemaEntity](appschema/remindersentity/section.md)
  An entity schema for a section.
- [AppSchema.RemindersEntity](appschema/remindersentity.md)
  Identifies entity schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity/locationtrigger)*