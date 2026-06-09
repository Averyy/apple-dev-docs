# operatingHours

**Framework**: App Intents  
**Kind**: property

An entity schema for an operating hours.

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
var operatingHours: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `operatingHours` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .maps.operatingHours)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `operatingHours` schema:

```swift
@AppEntity(schema: .maps.operatingHours)
struct MapsOperatingHoursEntity {
    // MARK: Static

    static let defaultQuery = MapsOperatingHoursEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var monday: [<#MapsOperatingTimeRangeEntity#>]
    var tuesday: [<#MapsOperatingTimeRangeEntity#>]
    var wednesday: [<#MapsOperatingTimeRangeEntity#>]
    var thursday: [<#MapsOperatingTimeRangeEntity#>]
    var friday: [<#MapsOperatingTimeRangeEntity#>]
    var saturday: [<#MapsOperatingTimeRangeEntity#>]
    var sunday: [<#MapsOperatingTimeRangeEntity#>]

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct MapsOperatingHoursEntityQuery: EntityQuery {
        func entities(for identifiers: [MapsOperatingHoursEntity.ID]) async throws -> [MapsOperatingHoursEntity] {
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
- [var operatingTimeRange: some AppSchemaEntity](appschema/mapsentity/operatingtimerange.md)
  An entity schema for an operating time range.
- [var place: some AppSchemaEntity](appschema/mapsentity/place.md)
  An entity schema for a place.
- [var rating: some AppSchemaEntity](appschema/mapsentity/rating.md)
  An entity schema for a rating.
- [AppSchema.MapsEntity](appschema/mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/operatinghours)*