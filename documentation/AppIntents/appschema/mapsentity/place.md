# place

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a place.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var place: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `place` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .maps.place)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `place` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_place` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .maps.place)
struct MapsPlaceEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more place entities, unless you provide another.
    static let defaultQuery = MapsPlaceEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the place entity.
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

    /// The details the system shows to identify the place entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more place entities by their identifiers.
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

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the place entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `place` | `GeoToolbox.PlaceDescriptor` | GeoToolbox | Place |
| `name` | `String?` | Swift | Name |
| `categories` | `[String]` | Swift | Categories |
| `operatingStatus` | `@AppEnum(schema: .maps.operatingStatus)?` | Your app | Operating Status `MapsOperatingStatusEnum` is a placeholder name for a type that conforms to the [`operatingStatus`](../mapsenum/operatingstatus.md) enum schema, which your app defines and implements. |
| `operatingHours` | `@AppEntity(schema: .maps.operatingHours)?` | Your app | Operating Hours `MapsOperatingHoursEntity` is a placeholder name for a type that conforms to the [`operatingHours`](./operatinghours.md) entity schema, which your app defines and implements. |
| `phoneNumber` | `String?` | Swift | Phone Number |
| `priceRange` | `@AppEnum(schema: .maps.priceRange)?` | Your app | Price Range `MapsPriceRangeEnum` is a placeholder name for a type that conforms to the [`priceRange`](../mapsenum/pricerange.md) enum schema, which your app defines and implements. |
| `ratings` | `[@AppEntity(schema: .maps.rating)]` | Your app | Ratings `MapsRating` is a placeholder name for a type that conforms to the [`rating`](./rating.md) entity schema, which your app defines and implements. |
| `amenities` | `[String]` | Swift | Amenities |

## See Also

### Content and parameter types
- [var currentLocation: some AppSchemaEntity](./currentlocation.md)
  An entity schema for a current location.
- [var navigationSession: some AppSchemaEntity](./navigationsession.md)
  An entity schema for a navigation session.
- [var operatingHours: some AppSchemaEntity](./operatinghours.md)
  An entity schema for an operating hours.
- [var operatingTimeRange: some AppSchemaEntity](./operatingtimerange.md)
  An entity schema for an operating time range.
- [var rating: some AppSchemaEntity](./rating.md)
  An entity schema for a rating.
- [AppSchema.MapsEntity](../mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/place)*