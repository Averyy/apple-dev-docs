# startNavigation

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that starts navigation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var startNavigation: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `maps` domain and one of your app’s actions matches the `startNavigation` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .maps.startNavigation)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

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

Define a `@UnionValue` enumeration for the `origin` parameter, as in the following example, by typing the first few characters of `maps_location` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum MapsLocation {
    case place(<#MapsPlaceEntity#>)
    case currentLocation(<#MapsCurrentLocationEntity#>)
}
```

Define a `@UnionValue` enumeration for the `destinations` parameter, as in the following example, by typing the first few characters of `maps_location` in Xcode and selecting it from the code-completion suggestions.

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

## See Also

### Actions
- [var reportIncident: some AppSchemaIntent](./reportincident.md)
  An intent schema that reports a traffic incident on the route.
- [var shareETA: some AppSchemaIntent](./shareeta.md)
  An intent schema that shares ETA to a contact while navigating.
- [var stopNavigation: some AppSchemaIntent](./stopnavigation.md)
  An intent schema that ends navigation.
- [var stopShareETA: some AppSchemaIntent](./stopshareeta.md)
  An intent schema that stops sharing ETA.
- [var updateNavigationWaypoints: some AppSchemaIntent](./updatenavigationwaypoints.md)
  An intent schema that updates the list of waypoints for a navigation session.
- [AppSchema.MapsIntent](../mapsintent.md)
  Identifies intent schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsintent/startnavigation)*