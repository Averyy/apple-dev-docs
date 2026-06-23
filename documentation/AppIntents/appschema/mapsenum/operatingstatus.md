# operatingStatus

**Framework**: App Intents  
**Kind**: property

An enum schema for an operating status parameter.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var operatingStatus: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `maps` domain and a parameter type matches the `operatingStatus` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .maps.operatingStatus)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `operatingStatus` schema:

```swift
@AppEnum(schema: .maps.operatingStatus)
enum MapsOperatingStatusEnum: String {
    case <#MapsOperatingStatusEnum Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var amenity: some AppSchemaEnum](appschema/mapsenum/amenity.md)
  An enum schema for an amenity parameter.
- [var incident: some AppSchemaEnum](appschema/mapsenum/incident.md)
  An enum schema for an incident parameter.
- [var navigationPreferences: some AppSchemaEnum](appschema/mapsenum/navigationpreferences.md)
  An enum schema for a navigation preferences parameter.
- [var priceRange: some AppSchemaEnum](appschema/mapsenum/pricerange.md)
  An enum schema for a price range parameter.
- [var ratingDescriptor: some AppSchemaEnum](appschema/mapsenum/ratingdescriptor.md)
  An enum schema for a rating descriptor parameter.
- [var transportType: some AppSchemaEnum](appschema/mapsenum/transporttype.md)
  An enum schema for a transport type parameter.
- [AppSchema.MapsEnum](appschema/mapsenum.md)
  Identifies enum schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsenum/operatingstatus)*