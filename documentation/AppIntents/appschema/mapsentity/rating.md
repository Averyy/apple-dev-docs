# rating

**Framework**: App Intents  
**Kind**: property

An entity schema for a rating.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var rating: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `rating` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .maps.rating)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `rating` schema:

```swift
@AppEntity(schema: .maps.rating)
struct MapsRating {
    // MARK: Static

    static let defaultQuery = MapsRatingQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var value: Double
    var descriptor: <#MapsRatingDescriptor#>
    var count: Int?
    var provider: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct MapsRatingQuery: EntityQuery {
        func entities(for identifiers: [MapsRating.ID]) async throws -> [MapsRating] {
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
- [var place: some AppSchemaEntity](appschema/mapsentity/place.md)
  An entity schema for a place.
- [AppSchema.MapsEntity](appschema/mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/rating)*