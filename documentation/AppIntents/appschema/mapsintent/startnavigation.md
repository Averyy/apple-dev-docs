# startNavigation

**Framework**: App Intents  
**Kind**: property

An intent schema that starts navigation.

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
var startNavigation: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `maps` domain and one of your app’s actions matches the `startNavigation` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .maps.startNavigation)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `startNavigation` schema:

```swift
@AppIntent(schema: .maps.startNavigation)
struct MapsStartNavigationIntent {
    var transportationType: <#MapsTransportTypeEnum#>
    var origin: <#MapsLocation#>
    var destinations: [<#MapsLocation#>]
    var preferences: Set<<#MapsNavigationPreferencesEnum#>>

    func perform() async throws -> some ReturnsValue<<#MapsNavigationSessionEntity#>?> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var addNavigationWaypoints: some AppSchemaIntent](appschema/mapsintent/addnavigationwaypoints.md)
  An intent schema that adds waypoints to a navigation session.
- [var reportIncident: some AppSchemaIntent](appschema/mapsintent/reportincident.md)
  An intent schema that reports a traffic incident on the route.
- [var shareETA: some AppSchemaIntent](appschema/mapsintent/shareeta.md)
  An intent schema that shares ETA to a contact while navigating.
- [var stopNavigation: some AppSchemaIntent](appschema/mapsintent/stopnavigation.md)
  An intent schema that ends navigation.
- [var stopShareETA: some AppSchemaIntent](appschema/mapsintent/stopshareeta.md)
  An intent schema that stops sharing ETA.
- [AppSchema.MapsIntent](appschema/mapsintent.md)
  Identifies intent schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsintent/startnavigation)*