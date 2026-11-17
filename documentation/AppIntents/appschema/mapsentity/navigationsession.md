# navigationSession

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a navigation session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var navigationSession: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `navigationSession` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .maps.navigationSession)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `navigationSession` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_navigationSession` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .maps.navigationSession)
struct MapsNavigationSessionEntity: UniqueEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more current route entities, unless you provide another.
    static let defaultQuery = MapsNavigationSessionEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the current route entity.
    let id: <#Identifiable.ID#>

    var estimatedArrivalDate: Date

    var waypoints: [<#MapsLocation#>]

    var transportationType: <#MapsTransportTypeEnum#>

    var preferences: [<#MapsNavigationPreferencesEnum#>]

    /// The details the system shows to identify the current route entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more current route entities by their identifiers.
    struct MapsNavigationSessionEntityQuery: EntityQuery {
        func entities(for identifiers: [MapsNavigationSessionEntity.ID]) async throws -> [MapsNavigationSessionEntity] {
            <#code#>
        }
    }
}
```

Define a `@UnionValue` enumeration for the `waypoints` property, as in the following example, by typing the first few characters of `maps_location` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum MapsLocation {
    case place(<#MapsPlaceEntity#>)
    case currentLocation(<#MapsCurrentLocationEntity#>)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the navigation-session entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `estimatedArrivalDate` | `Date` | Foundation | Estimated Arrival Date |
| `waypoints` | `[@UnionValue]` | Your app | Waypoints `MapsLocation` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `transportationType` | `@AppEnum(schema: .maps.transportType)` | Your app | Transportation Type `MapsTransportTypeEnum` is a placeholder name for a type that conforms to the [`transportType`](../mapsenum/transporttype.md) enum schema, which your app defines and implements. |
| `preferences` | `[@AppEnum(schema: .maps.navigationPreferences)]` | Your app | Preferences `MapsNavigationPreferencesEnum` is a placeholder name for a type that conforms to the [`navigationPreferences`](../mapsenum/navigationpreferences.md) enum schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var currentLocation: some AppSchemaEntity](./currentlocation.md)
  An entity schema for a current location.
- [var operatingHours: some AppSchemaEntity](./operatinghours.md)
  An entity schema for an operating hours.
- [var operatingTimeRange: some AppSchemaEntity](./operatingtimerange.md)
  An entity schema for an operating time range.
- [var place: some AppSchemaEntity](./place.md)
  An entity schema for a place.
- [var rating: some AppSchemaEntity](./rating.md)
  An entity schema for a rating.
- [AppSchema.MapsEntity](../mapsentity.md)
  Identifies entity schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/navigationsession)*