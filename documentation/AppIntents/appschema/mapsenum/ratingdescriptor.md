# ratingDescriptor

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for a rating descriptor parameter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var ratingDescriptor: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `maps` domain and a parameter type matches the `ratingDescriptor` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .maps.ratingDescriptor)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `ratingDescriptor` schema:

```swift
@AppEnum(schema: .maps.ratingDescriptor)
enum MapsRatingDescriptor: String {
    case percentage

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .percentage: "Percentage"
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Types for static parameters
- [var amenity: some AppSchemaEnum](./amenity.md)
  An enum schema for an amenity parameter.
- [var incident: some AppSchemaEnum](./incident.md)
  An enum schema for an incident parameter.
- [var navigationPreferences: some AppSchemaEnum](./navigationpreferences.md)
  An enum schema for a navigation preferences parameter.
- [var operatingStatus: some AppSchemaEnum](./operatingstatus.md)
  An enum schema for an operating status parameter.
- [var priceRange: some AppSchemaEnum](./pricerange.md)
  An enum schema for a price range parameter.
- [var transportType: some AppSchemaEnum](./transporttype.md)
  An enum schema for a transport type parameter.
- [AppSchema.MapsEnum](../mapsenum.md)
  Identifies enum schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsenum/ratingdescriptor)*