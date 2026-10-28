# toggleDepth

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that toggles depth effect for a photo.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var toggleDepth: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `photos` domain and one of your app’s actions matches the `toggleDepth` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .photos.toggleDepth)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `toggleDepth` schema:

```swift
@AppIntent(schema: .photos.toggleDepth)
struct SetMediaDepthIntent {
    var isEnabled: Bool
    var target: <#PhotoEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Actions
- [var addAssetsToAlbum: some AppSchemaIntent](./addassetstoalbum.md)
  An intent schema that adds the provided photos to the provided album.
- [var cleanupPhoto: some AppSchemaIntent](./cleanupphoto.md)
  An intent schema that removes distracting objects in a photo.
- [var copyEdits: some AppSchemaIntent](./copyedits.md)
  An intent schema that copies edits from the provided photo.
- [var createAlbum: some AppSchemaIntent](./createalbum.md)
  An intent schema that creates an album.
- [var createAssets: some AppSchemaIntent](./createassets.md)
  An intent schema that creates photos from the provided files.
- [var crop: some AppSchemaIntent](./crop.md)
  An intent schema that crops a photo.
- [var deleteAlbum: some AppSchemaIntent](./deletealbum.md)
  An intent schema that deletes the provided albums.
- [var deleteAssets: some AppSchemaIntent](./deleteassets.md)
  An intent schema that deletes the provided photos.
- [var duplicateAssets: some AppSchemaIntent](./duplicateassets.md)
  An intent schema that duplicates the selected photos.
- [var editAsset: some AppSchemaIntent](./editasset.md)
  An intent schema that opens a photo for editing.
- [var openAlbum: some AppSchemaIntent](./openalbum.md)
  An intent schema that opens the provided album.
- [var openAsset: some AppSchemaIntent](./openasset.md)
  An intent schema that opens the app to a photo.
- [var pasteEdits: some AppSchemaIntent](./pasteedits.md)
  An intent schema that pastes edits to the provided photo.
- [var postToSharedAlbum: some AppSchemaIntent](./posttosharedalbum.md)
  An intent schema that posts the provided photos or files and optional comment to the provided shared album.
- [var removeAssetsFromAlbum: some AppSchemaIntent](./removeassetsfromalbum.md)
  An intent schema that removes the provided photos from the provided album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosintent/toggledepth)*