# albumType

**Framework**: App Intents  
**Kind**: property

An enum schema for an album type parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var albumType: some AppSchemaEnum { get }
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `photos` domain and a parameter type matches the `albumType` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .photos.albumType)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `albumType` schema:

```swift
@AppEnum(schema: .photos.albumType)
enum PhotoAlbumType: String {
    case <#PhotoAlbumType Case#>

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

- [var assetType: some AppSchemaEnum](appschema/photosenum/assettype.md)
  An enum schema for an asset type parameter.
- [var filterType: some AppSchemaEnum](appschema/photosenum/filtertype.md)
  An enum schema for a filter type parameter.
- [var rotationDirection: some AppSchemaEnum](appschema/photosenum/rotationdirection.md)
  An enum schema for a rotation direction parameter.
- [AppSchema.PhotosEnum](appschema/photosenum.md)
  Identifies enum schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosenum/albumtype)*