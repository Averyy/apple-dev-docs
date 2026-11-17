# operatingTimeRange

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an operating time range.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var operatingTimeRange: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `operatingTimeRange` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .maps.operatingTimeRange)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `operatingTimeRange` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_operatingTimeRange` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .maps.operatingTimeRange)
struct MapsOperatingTimeRangeEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more business operating time range entities, unless you provide another.
    static let defaultQuery = MapsOperatingTimeRangeEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the business operating time range entity.
    let id: <#Identifiable.ID#>

    var startTime: DateComponents

    var endTime: DateComponents

    /// The details the system shows to identify the business operating time range entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more business operating time range entities by their identifiers.
    struct MapsOperatingTimeRangeEntityQuery: EntityQuery {
        func entities(for identifiers: [MapsOperatingTimeRangeEntity.ID]) async throws -> [MapsOperatingTimeRangeEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the operating-time-range entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `startTime` | `DateComponents` | Foundation | Start Time |
| `endTime` | `DateComponents` | Foundation | End Time |

## See Also

### Content and parameter types
- [var currentLocation: some AppSchemaEntity](./currentlocation.md)
  An entity schema for a current location.
- [var navigationSession: some AppSchemaEntity](./navigationsession.md)
  An entity schema for a navigation session.
- [var operatingHours: some AppSchemaEntity](./operatinghours.md)
  An entity schema for an operating hours.
- [var place: some AppSchemaEntity](./place.md)
  An entity schema for a place.
- [var rating: some AppSchemaEntity](./rating.md)
  An entity schema for a rating.
- [AppSchema.MapsEntity](../mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/operatingtimerange)*