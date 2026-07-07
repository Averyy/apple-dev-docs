# AppSchema.MapsIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the maps domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MapsIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addNavigationWaypoints: some AppSchemaIntent](appschema/mapsintent/addnavigationwaypoints.md)
  An intent schema that adds waypoints to a navigation session.
- [var reportIncident: some AppSchemaIntent](appschema/mapsintent/reportincident.md)
  An intent schema that reports a traffic incident on the route.
- [var shareETA: some AppSchemaIntent](appschema/mapsintent/shareeta.md)
  An intent schema that shares ETA to a contact while navigating.
- [var startNavigation: some AppSchemaIntent](appschema/mapsintent/startnavigation.md)
  An intent schema that starts navigation.
- [var stopNavigation: some AppSchemaIntent](appschema/mapsintent/stopnavigation.md)
  An intent schema that ends navigation.
- [var stopShareETA: some AppSchemaIntent](appschema/mapsintent/stopshareeta.md)
  An intent schema that stops sharing ETA.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var addNavigationWaypoints: some AppSchemaIntent](appschema/mapsintent/addnavigationwaypoints.md)
  An intent schema that adds waypoints to a navigation session.
- [var reportIncident: some AppSchemaIntent](appschema/mapsintent/reportincident.md)
  An intent schema that reports a traffic incident on the route.
- [var shareETA: some AppSchemaIntent](appschema/mapsintent/shareeta.md)
  An intent schema that shares ETA to a contact while navigating.
- [var startNavigation: some AppSchemaIntent](appschema/mapsintent/startnavigation.md)
  An intent schema that starts navigation.
- [var stopNavigation: some AppSchemaIntent](appschema/mapsintent/stopnavigation.md)
  An intent schema that ends navigation.
- [var stopShareETA: some AppSchemaIntent](appschema/mapsintent/stopshareeta.md)
  An intent schema that stops sharing ETA.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsintent)*