# stopShareETA

**Framework**: App Intents  
**Kind**: property

An intent schema that stops sharing ETA.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stopShareETA: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `maps` domain and one of your app’s actions matches the `stopShareETA` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .maps.stopShareETA)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `stopShareETA` schema:

```swift
@AppIntent(schema: .maps.stopShareETA)
struct MapsStopShareETAIntent {
    var person: IntentPerson?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var reportIncident: some AppSchemaIntent](appschema/mapsintent/reportincident.md)
  An intent schema that reports a traffic incident on the route.
- [var shareETA: some AppSchemaIntent](appschema/mapsintent/shareeta.md)
  An intent schema that shares ETA to a contact while navigating.
- [var startNavigation: some AppSchemaIntent](appschema/mapsintent/startnavigation.md)
  An intent schema that starts navigation.
- [var stopNavigation: some AppSchemaIntent](appschema/mapsintent/stopnavigation.md)
  An intent schema that ends navigation.
- [AppSchema.MapsIntent](appschema/mapsintent.md)
  Identifies intent schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsintent/stopshareeta)*