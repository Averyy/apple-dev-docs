# copyEdits

**Framework**: App Intents  
**Kind**: property

An intent schema that copies edits from the provided photo.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var copyEdits: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `photos` domain and one of your app’s actions matches the `copyEdits` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .photos.copyEdits)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `copyEdits` schema:

```swift
@AppIntent(schema: .photos.copyEdits)
struct CopyMediaEditsIntent {
    var target: <#PhotoEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var addAssetsToAlbum: some AppSchemaIntent](appschema/photosintent/addassetstoalbum.md)
  An intent schema that adds the provided photos to the provided album.
- [var cleanupPhoto: some AppSchemaIntent](appschema/photosintent/cleanupphoto.md)
  An intent schema that removes distracting objects in a photo.
- [var createAlbum: some AppSchemaIntent](appschema/photosintent/createalbum.md)
  An intent schema that creates an album.
- [var createAssets: some AppSchemaIntent](appschema/photosintent/createassets.md)
  An intent schema that creates photos from the provided files.
- [var crop: some AppSchemaIntent](appschema/photosintent/crop.md)
  An intent schema that crops a photo.
- [var deleteAlbum: some AppSchemaIntent](appschema/photosintent/deletealbum.md)
  An intent schema that deletes the provided albums.
- [var deleteAssets: some AppSchemaIntent](appschema/photosintent/deleteassets.md)
  An intent schema that deletes the provided photos.
- [var duplicateAssets: some AppSchemaIntent](appschema/photosintent/duplicateassets.md)
  An intent schema that duplicates the selected photos.
- [var editAsset: some AppSchemaIntent](appschema/photosintent/editasset.md)
  An intent schema that opens a photo for editing.
- [var openAlbum: some AppSchemaIntent](appschema/photosintent/openalbum.md)
  An intent schema that opens the provided album.
- [var openAsset: some AppSchemaIntent](appschema/photosintent/openasset.md)
  An intent schema that opens the app to a photo.
- [var pasteEdits: some AppSchemaIntent](appschema/photosintent/pasteedits.md)
  An intent schema that pastes edits to the provided photo.
- [var postToSharedAlbum: some AppSchemaIntent](appschema/photosintent/posttosharedalbum.md)
  An intent schema that posts the provided photos or files and optional comment to the provided shared album.
- [var removeAssetsFromAlbum: some AppSchemaIntent](appschema/photosintent/removeassetsfromalbum.md)
  An intent schema that removes the provided photos from the provided album.
- [var setDepth: some AppSchemaIntent](appschema/photosintent/setdepth.md)
  An intent schema that sets the depth value of a photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosintent/copyedits)*