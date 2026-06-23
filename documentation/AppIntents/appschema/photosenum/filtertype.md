# filterType

**Framework**: App Intents  
**Kind**: property

An enum schema for a filter type parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var filterType: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `photos` domain and a parameter type matches the `filterType` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .photos.filterType)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `filterType` schema:

```swift
@AppEnum(schema: .photos.filterType)
enum PhotoFilterEffectType: String {
    case <#PhotoFilterEffectType Case#>

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

- [var albumType: some AppSchemaEnum](appschema/photosenum/albumtype.md)
  An enum schema for an album type parameter.
- [var assetType: some AppSchemaEnum](appschema/photosenum/assettype.md)
  An enum schema for an asset type parameter.
- [var rotationDirection: some AppSchemaEnum](appschema/photosenum/rotationdirection.md)
  An enum schema for a rotation direction parameter.
- [AppSchema.PhotosEnum](appschema/photosenum.md)
  Identifies enum schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosenum/filtertype)*