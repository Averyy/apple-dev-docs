# reportIncident

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that reports a traffic incident on the route.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var reportIncident: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `maps` domain and one of your app’s actions matches the `reportIncident` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .maps.reportIncident)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `reportIncident` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_reportIncident` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .maps.reportIncident)
struct ReportIncidentIntent {
    /// Traffic incident type to report.
    var incident: <#MapsIncidentEnum#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the report-incident intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `incident` | `@AppEnum(schema: .maps.incident)` | Your app | Traffic incident type to report. `MapsIncidentEnum` is a placeholder name for a type that conforms to the [`incident`](../mapsenum/incident.md) enum schema, which your app defines and implements. |

## See Also

### Actions
- [var shareETA: some AppSchemaIntent](./shareeta.md)
  An intent schema that shares ETA to a contact while navigating.
- [var startNavigation: some AppSchemaIntent](./startnavigation.md)
  An intent schema that starts navigation.
- [var stopNavigation: some AppSchemaIntent](./stopnavigation.md)
  An intent schema that ends navigation.
- [var stopShareETA: some AppSchemaIntent](./stopshareeta.md)
  An intent schema that stops sharing ETA.
- [var updateNavigationWaypoints: some AppSchemaIntent](./updatenavigationwaypoints.md)
  An intent schema that updates the list of waypoints for a navigation session.
- [AppSchema.MapsIntent](../mapsintent.md)
  Identifies intent schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsintent/reportincident)*