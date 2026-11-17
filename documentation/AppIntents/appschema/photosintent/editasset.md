# editAsset

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that opens a photo for editing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var editAsset: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `photos` domain and one of your app’s actions matches the `editAsset` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .photos.editAsset)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `editAsset` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `photos_editAsset` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .photos.editAsset)
struct EditAsset {
    /// Photo to edit.
    var asset: <#PhotoEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the edit-asset intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `asset` | `@AppEntity(schema: .photos.asset)` | Your app | Photo to edit. `PhotoEntity` is a placeholder name for a type that conforms to the [`asset`](../photosentity/asset.md) entity schema, which your app defines and implements. |

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
- [var setDepth: some AppSchemaIntent](./setdepth.md)
  An intent schema that sets the depth value of a photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosintent/editasset)*