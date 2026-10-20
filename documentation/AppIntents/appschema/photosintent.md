# AppSchema.PhotosIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

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
- [var addAssetsToAlbum: some AppSchemaIntent](./photosintent/addassetstoalbum.md)
  An intent schema that adds the provided photos to the provided album.
- [var cleanupPhoto: some AppSchemaIntent](./photosintent/cleanupphoto.md)
  An intent schema that removes distracting objects in a photo.
- [var copyEdits: some AppSchemaIntent](./photosintent/copyedits.md)
  An intent schema that copies edits from the provided photo.
- [var createAlbum: some AppSchemaIntent](./photosintent/createalbum.md)
  An intent schema that creates an album.
- [var createAssets: some AppSchemaIntent](./photosintent/createassets.md)
  An intent schema that creates photos from the provided files.
- [var crop: some AppSchemaIntent](./photosintent/crop.md)
  An intent schema that crops a photo.
- [var deleteAlbum: some AppSchemaIntent](./photosintent/deletealbum.md)
  An intent schema that deletes the provided albums.
- [var deleteAssets: some AppSchemaIntent](./photosintent/deleteassets.md)
  An intent schema that deletes the provided photos.
- [var duplicateAssets: some AppSchemaIntent](./photosintent/duplicateassets.md)
  An intent schema that duplicates the selected photos.
- [var editAsset: some AppSchemaIntent](./photosintent/editasset.md)
  An intent schema that opens a photo for editing.
- [var openAlbum: some AppSchemaIntent](./photosintent/openalbum.md)
  An intent schema that opens the provided album.
- [var openAsset: some AppSchemaIntent](./photosintent/openasset.md)
  An intent schema that opens the app to a photo.
- [var pasteEdits: some AppSchemaIntent](./photosintent/pasteedits.md)
  An intent schema that pastes edits to the provided photo.
- [var postToSharedAlbum: some AppSchemaIntent](./photosintent/posttosharedalbum.md)
  An intent schema that posts the provided photos or files and optional comment to the provided shared album.
- [var removeAssetsFromAlbum: some AppSchemaIntent](./photosintent/removeassetsfromalbum.md)
  An intent schema that removes the provided photos from the provided album.
- [var search: some AppSchemaIntent](./photosintent/search.md)
  An intent schema that navigates to search results.
- [var setDepth: some AppSchemaIntent](./photosintent/setdepth.md)
  An intent schema that sets the depth value of a photo.
- [var setExposure: some AppSchemaIntent](./photosintent/setexposure.md)
  An intent schema that configures the exposure for a photo.
- [var setFilter: some AppSchemaIntent](./photosintent/setfilter.md)
  An intent schema that applies a filter to a photo.
- [var setRotation: some AppSchemaIntent](./photosintent/setrotation.md)
  An intent schema that rotates a photo.
- [var setSaturation: some AppSchemaIntent](./photosintent/setsaturation.md)
  An intent schema that configures the saturation for a photo.
- [var setWarmth: some AppSchemaIntent](./photosintent/setwarmth.md)
  An intent schema that configures the warmth for a photo.
- [var straighten: some AppSchemaIntent](./photosintent/straighten.md)
  An intent schema that straightens a photo.
- [var toggleDepth: some AppSchemaIntent](./photosintent/toggledepth.md)
  An intent schema that toggles depth effect for a photo.
- [var toggleSuggestedEdits: some AppSchemaIntent](./photosintent/togglesuggestededits.md)
  An intent schema that enhances a photo.
- [var updateAlbum: some AppSchemaIntent](./photosintent/updatealbum.md)
  An intent schema that renames the provided album.
- [var updateAsset: some AppSchemaIntent](./photosintent/updateasset.md)
  An intent schema that updates an existing photo’s properties.
- [var updateRecognizedPerson: some AppSchemaIntent](./photosintent/updaterecognizedperson.md)
  An intent schema that updates the provided person with new properties.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var addAssetsToAlbum: some AppSchemaIntent](./photosintent/addassetstoalbum.md)
  An intent schema that adds the provided photos to the provided album.
- [var cleanupPhoto: some AppSchemaIntent](./photosintent/cleanupphoto.md)
  An intent schema that removes distracting objects in a photo.
- [var copyEdits: some AppSchemaIntent](./photosintent/copyedits.md)
  An intent schema that copies edits from the provided photo.
- [var createAlbum: some AppSchemaIntent](./photosintent/createalbum.md)
  An intent schema that creates an album.
- [var createAssets: some AppSchemaIntent](./photosintent/createassets.md)
  An intent schema that creates photos from the provided files.
- [var crop: some AppSchemaIntent](./photosintent/crop.md)
  An intent schema that crops a photo.
- [var deleteAlbum: some AppSchemaIntent](./photosintent/deletealbum.md)
  An intent schema that deletes the provided albums.
- [var deleteAssets: some AppSchemaIntent](./photosintent/deleteassets.md)
  An intent schema that deletes the provided photos.
- [var duplicateAssets: some AppSchemaIntent](./photosintent/duplicateassets.md)
  An intent schema that duplicates the selected photos.
- [var editAsset: some AppSchemaIntent](./photosintent/editasset.md)
  An intent schema that opens a photo for editing.
- [var openAlbum: some AppSchemaIntent](./photosintent/openalbum.md)
  An intent schema that opens the provided album.
- [var openAsset: some AppSchemaIntent](./photosintent/openasset.md)
  An intent schema that opens the app to a photo.
- [var pasteEdits: some AppSchemaIntent](./photosintent/pasteedits.md)
  An intent schema that pastes edits to the provided photo.
- [var postToSharedAlbum: some AppSchemaIntent](./photosintent/posttosharedalbum.md)
  An intent schema that posts the provided photos or files and optional comment to the provided shared album.
- [var removeAssetsFromAlbum: some AppSchemaIntent](./photosintent/removeassetsfromalbum.md)
  An intent schema that removes the provided photos from the provided album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosintent)*