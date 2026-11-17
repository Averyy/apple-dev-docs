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

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `maps` domain and one of your app’s actions matches the `startNavigation` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .maps.startNavigation)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `startNavigation` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_startNavigation` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .maps.startNavigation)
struct MapsStartNavigationIntent {
    /// The transportation type.
    var transportationType: <#MapsTransportTypeEnum#>

    /// Origin location to start navigation.
    var origin: <#MapsLocation#>

    /// Destination locations to start navigation.
    var destinations: [<#MapsLocation#>]

    /// Navigation preferences.
    var preferences: Set<<#MapsNavigationPreferencesEnum#>>

    func perform() async throws -> some ReturnsValue<<#MapsNavigationSessionEntity#>?> {
        <#code#>
    }
}
```

Define a `@UnionValue` enumeration for the `origin` and `destinations` parameters, as in the following example, by typing the first few characters of `maps_location` in Xcode and selecting it from the code-completion suggestions.

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

## Parameters for the start-navigation intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `transportationType` | `@AppEnum(schema: .maps.transportType)` | Your app | The transportation type. `MapsTransportTypeEnum` is a placeholder name for a type that conforms to the [`transportType`](../mapsenum/transporttype.md) enum schema, which your app defines and implements. |
| `origin` | `@UnionValue` | Your app | Origin location to start navigation. `MapsLocation` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `destinations` | `[@UnionValue]` | Your app | Destination locations to start navigation. `MapsLocation` is a placeholder name for the `@UnionValue` type your app defines, as shown in the example above the table. |
| `preferences` | `Set<@AppEnum(schema: .maps.navigationPreferences)>` | Your app | Navigation preferences. `MapsNavigationPreferencesEnum` is a placeholder name for a type that conforms to the [`navigationPreferences`](../mapsenum/navigationpreferences.md) enum schema, which your app defines and implements. |

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