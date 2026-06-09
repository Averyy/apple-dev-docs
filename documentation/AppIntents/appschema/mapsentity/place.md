# place

**Framework**: App Intents  
**Kind**: property

An entity schema for a place.

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
var place: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `place` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .maps.place)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `place` schema:

```swift
@AppEntity(schema: .maps.place)
struct MapsPlaceEntity {
    // MARK: Static

    static let defaultQuery = MapsPlaceEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var place: GeoToolbox.PlaceDescriptor
    var name: String?
    var categories: [String]
    var operatingStatus: <#MapsOperatingStatusEnum#>?
    var operatingHours: <#MapsOperatingHoursEntity#>?
    var phoneNumber: String?
    var priceRange: <#MapsPriceRangeEnum#>?
    var ratings: [<#MapsRating#>]
    var amenities: [String]

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct MapsPlaceEntityQuery: EntityQuery {
        func entities(for identifiers: [MapsPlaceEntity.ID]) async throws -> [MapsPlaceEntity] {
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
- [var navigationSession: some AppSchemaEntity](appschema/mapsentity/navigationsession.md)
  An entity schema for a navigation session.
- [var operatingHours: some AppSchemaEntity](appschema/mapsentity/operatinghours.md)
  An entity schema for an operating hours.
- [var operatingTimeRange: some AppSchemaEntity](appschema/mapsentity/operatingtimerange.md)
  An entity schema for an operating time range.
- [var rating: some AppSchemaEntity](appschema/mapsentity/rating.md)
  An entity schema for a rating.
- [AppSchema.MapsEntity](appschema/mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/place)*