# currentLocation

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a current location.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var currentLocation: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `maps` domain and its content matches the `currentLocation` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .maps.currentLocation)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `currentLocation` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_currentLocation` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .maps.currentLocation)
struct MapsCurrentLocationEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more current location entities, unless you provide another.
    static let defaultQuery = MapsCurrentLocationEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the current location entity.
    let id: <#Identifiable.ID#>

    /// The details the system shows to identify the current location entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more current location entities by their identifiers.
    struct MapsCurrentLocationEntityQuery: EntityQuery {
        func entities(for identifiers: [MapsCurrentLocationEntity.ID]) async throws -> [MapsCurrentLocationEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Content and parameter types
- [var navigationSession: some AppSchemaEntity](./navigationsession.md)
  An entity schema for a navigation session.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsentity/currentlocation)*