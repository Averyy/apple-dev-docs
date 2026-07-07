# AppSchema.PhotosIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the photos domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol PhotosIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addAssetsToAlbum: some AppSchemaIntent](appschema/photosintent/addassetstoalbum.md)
  An intent schema that adds the provided photos to the provided album.
- [var cleanupPhoto: some AppSchemaIntent](appschema/photosintent/cleanupphoto.md)
  An intent schema that removes distracting objects in a photo.
- [var copyEdits: some AppSchemaIntent](appschema/photosintent/copyedits.md)
  An intent schema that copies edits from the provided photo.
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
- [var search: some AppSchemaIntent](appschema/photosintent/search.md)
  An intent schema that navigates to search results.
- [var setDepth: some AppSchemaIntent](appschema/photosintent/setdepth.md)
  An intent schema that sets the depth value of a photo.
- [var setExposure: some AppSchemaIntent](appschema/photosintent/setexposure.md)
  An intent schema that configures the exposure for a photo.
- [var setFilter: some AppSchemaIntent](appschema/photosintent/setfilter.md)
  An intent schema that applies a filter to a photo.
- [var setRotation: some AppSchemaIntent](appschema/photosintent/setrotation.md)
  An intent schema that rotates a photo.
- [var setSaturation: some AppSchemaIntent](appschema/photosintent/setsaturation.md)
  An intent schema that configures the saturation for a photo.
- [var setWarmth: some AppSchemaIntent](appschema/photosintent/setwarmth.md)
  An intent schema that configures the warmth for a photo.
- [var straighten: some AppSchemaIntent](appschema/photosintent/straighten.md)
  An intent schema that straightens a photo.
- [var toggleDepth: some AppSchemaIntent](appschema/photosintent/toggledepth.md)
  An intent schema that toggles depth effect for a photo.
- [var toggleSuggestedEdits: some AppSchemaIntent](appschema/photosintent/togglesuggestededits.md)
  An intent schema that enhances a photo.
- [var updateAlbum: some AppSchemaIntent](appschema/photosintent/updatealbum.md)
  An intent schema that renames the provided album.
- [var updateAsset: some AppSchemaIntent](appschema/photosintent/updateasset.md)
  An intent schema that updates an existing photo’s properties.
- [var updateRecognizedPerson: some AppSchemaIntent](appschema/photosintent/updaterecognizedperson.md)
  An intent schema that updates the provided person with new properties.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var addAssetsToAlbum: some AppSchemaIntent](appschema/photosintent/addassetstoalbum.md)
  An intent schema that adds the provided photos to the provided album.
- [var cleanupPhoto: some AppSchemaIntent](appschema/photosintent/cleanupphoto.md)
  An intent schema that removes distracting objects in a photo.
- [var copyEdits: some AppSchemaIntent](appschema/photosintent/copyedits.md)
  An intent schema that copies edits from the provided photo.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosintent)*