# assetType

**Framework**: App Intents  
**Kind**: property

An enum schema for an asset type parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var assetType: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `photos` domain and a parameter type matches the `assetType` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .photos.assetType)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `assetType` schema:

```swift
@AppEnum(schema: .photos.assetType)
enum PhotoAssetType: String {
    case <#PhotoAssetType Case#>

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
- [var filterType: some AppSchemaEnum](appschema/photosenum/filtertype.md)
  An enum schema for a filter type parameter.
- [var rotationDirection: some AppSchemaEnum](appschema/photosenum/rotationdirection.md)
  An enum schema for a rotation direction parameter.
- [AppSchema.PhotosEnum](appschema/photosenum.md)
  Identifies enum schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosenum/assettype)*