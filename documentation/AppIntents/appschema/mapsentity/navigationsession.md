# navigationSession

**Framework**: App Intents  
**Kind**: property

An entity schema for a navigation session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var navigationSession: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `navigationSession` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .maps.navigationSession)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `navigationSession` schema:

```swift
@AppEntity(schema: .maps.navigationSession)
struct MapsNavigationSessionEntity: UniqueEntity {
    // MARK: Static

    static let defaultQuery = MapsNavigationSessionEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var estimatedArrivalDate: Date
    var waypoints: [<#MapsLocation#>]
    var transportationType: <#MapsTransportTypeEnum#>
    var preferences: [<#MapsNavigationPreferencesEnum#>]

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct MapsNavigationSessionEntityQuery: EntityQuery {
        func entities(for identifiers: [MapsNavigationSessionEntity.ID]) async throws -> [MapsNavigationSessionEntity] {
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

- [var currentLocation: some AppSchemaEntity](appschema/mapsentity/currentlocation.md)
  An entity schema for a current location.
- [var operatingHours: some AppSchemaEntity](appschema/mapsentity/operatinghours.md)
  An entity schema for an operating hours.
- [var operatingTimeRange: some AppSchemaEntity](appschema/mapsentity/operatingtimerange.md)
  An entity schema for an operating time range.
- [var place: some AppSchemaEntity](appschema/mapsentity/place.md)
  An entity schema for a place.
- [var rating: some AppSchemaEntity](appschema/mapsentity/rating.md)
  An entity schema for a rating.
- [AppSchema.MapsEntity](appschema/mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/navigationsession)*