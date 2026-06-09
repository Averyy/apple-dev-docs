# attendee

**Framework**: App Intents  
**Kind**: property

An entity schema for an attendee.

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
var attendee: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `calendar` domain and its content matches the `attendee` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .calendar.attendee)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `attendee` schema:

```swift
@AppEntity(schema: .calendar.attendee)
struct AttendeeEntity {
    // MARK: Static

    static let defaultQuery = AttendeeEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var person: IntentPerson
    var status: <#ParticipantStatus#>?
    var isAttendanceOptional: Bool
    var type: <#AttendeeType#>?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct AttendeeEntityQuery: EntityQuery {
        func entities(for identifiers: [AttendeeEntity.ID]) async throws -> [AttendeeEntity] {
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

- [var calendar: some AppSchemaEntity](appschema/calendarentity/calendar.md)
  An entity schema for a calendar.
- [var event: some AppSchemaEntity](appschema/calendarentity/event.md)
  An entity schema for an event.
- [AppSchema.CalendarEntity](appschema/calendarentity.md)
  Identifies entity schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarentity/attendee)*