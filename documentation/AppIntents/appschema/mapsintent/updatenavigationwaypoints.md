# updateNavigationWaypoints

**Framework**: App Intents  
**Kind**: property

An intent schema that updates the list of waypoints for a navigation session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var updateNavigationWaypoints: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `maps` domain and one of your app’s actions matches the `updateNavigationWaypoints` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .maps.updateNavigationWaypoints)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateNavigationWaypoints` schema:

```swift
@AppIntent(schema: .maps.updateNavigationWaypoints)
struct MapsUpdateNavigationWaypointsIntent {
    var navigation: <#MapsNavigationSessionEntity#>
    var waypoints: [<#MapsLocation#>]

    func perform() async throws -> some ReturnsValue<<#MapsNavigationSessionEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsintent/updatenavigationwaypoints)*