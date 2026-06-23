# attendeeStatus

**Framework**: App Intents  
**Kind**: property

An enum schema for an attendee status parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var attendeeStatus: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `calendar` domain and a parameter type matches the `attendeeStatus` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .calendar.attendeeStatus)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `attendeeStatus` schema:

```swift
@AppEnum(schema: .calendar.attendeeStatus)
enum ParticipantStatus: String {
    case accepted
    case declined
    case tentative

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .accepted: "Accepted",
        .declined: "Declined",
        .tentative: "Tentative"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var attendeeType: some AppSchemaEnum](appschema/calendarenum/attendeetype.md)
  An enum schema for an attendee type parameter.
- [var eventSpan: some AppSchemaEnum](appschema/calendarenum/eventspan.md)
  An enum schema for an event span parameter.
- [var eventStatus: some AppSchemaEnum](appschema/calendarenum/eventstatus.md)
  An enum schema for an event status parameter.
- [AppSchema.CalendarEnum](appschema/calendarenum.md)
  Identifies enum schemas in the calendar domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/calendarenum/attendeestatus)*