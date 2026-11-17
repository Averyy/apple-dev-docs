# amenity

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for an amenity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var amenity: some AppSchemaEnum { get }
```

## Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `maps` domain and a parameter type matches the `amenity` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum(schema: .maps.amenity)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `amenity` schema. You can create a type that conforms to the schema by adding the `@AppEnum` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `maps_amenity` and select it from the code-completion suggestions:

```swift
@AppEnum(schema: .maps.amenity)
enum MapsAmenityTypeEnum: String {
    case <#MapsAmenityTypeEnum Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Types for static parameters
- [var incident: some AppSchemaEnum](./incident.md)
  An enum schema for an incident.
- [var navigationPreferences: some AppSchemaEnum](./navigationpreferences.md)
  An enum schema for a navigation preferences.
- [var operatingStatus: some AppSchemaEnum](./operatingstatus.md)
  An enum schema for an operating status.
- [var priceRange: some AppSchemaEnum](./pricerange.md)
  An enum schema for a price range.
- [var ratingDescriptor: some AppSchemaEnum](./ratingdescriptor.md)
  An enum schema for a rating descriptor.
- [var transportType: some AppSchemaEnum](./transporttype.md)
  An enum schema for a transport type.
- [AppSchema.MapsEnum](../mapsenum.md)
  Identifies enum schemas in the maps domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/mapsenum/amenity)*