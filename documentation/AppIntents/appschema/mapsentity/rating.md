# rating

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a rating.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var rating: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `rating` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .maps.rating)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `rating` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_rating` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .maps.rating)
struct MapsRating {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more rating entities, unless you provide another.
    static let defaultQuery = MapsRatingQuery()

    // MARK: Entity properties

    /// The unique identifier for the rating entity.
    let id: <#Identifiable.ID#>

    var value: Double

    var descriptor: <#MapsRatingDescriptor#>

    var count: Int?

    var provider: String

    /// The details the system shows to identify the rating entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more rating entities by their identifiers.
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

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the rating entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `value` | `Double` | Swift | Rating |
| `descriptor` | `@AppEnum(schema: .maps.ratingDescriptor)` | Your app | Rating Descriptor `MapsRatingDescriptor` is a placeholder name for a type that conforms to the [`ratingDescriptor`](../mapsenum/ratingdescriptor.md) enum schema, which your app defines and implements. |
| `count` | `Int?` | Swift | Count |
| `provider` | `String` | Swift | Source |

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
- [var place: some AppSchemaEntity](./place.md)
  An entity schema for a place.
- [AppSchema.MapsEntity](../mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/rating)*