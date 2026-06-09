# Photos

**Framework**: App Intents

Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.

#### Overview

The `.photos` domain defines app schemas that provide a structured representation for common photo and video actions and content. Apply schemas in the `.photos` domain to make your app’s photo and video functionality available to Apple Intelligence and Siri. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across photo and video apps. For example, a person can edit a photo on different apps that support the [`editAsset`](appschema/photosintent/editasset.md) schema with the same phrases.

Most schemas in this domain operate on assets that are already in your app’s library. The exception is [`createAssets`](appschema/photosintent/createassets.md), which adds new assets from an external source.

The following table maps example phrases that apply to each schema:

| Photos intent schemas | Example phrases |
| --- | --- |
| [`addAssetsToAlbum`](appschema/photosintent/addassetstoalbum.md) | “Add DSC_001.JPEG to the 2024 album.” |
| [`cleanupPhoto`](appschema/photosintent/cleanupphoto.md) | “Clean up.” or “Remove the clutter.” |
| [`createAlbum`](appschema/photosintent/createalbum.md) | “Create a new album named pics.” |
| [`createAssets`](appschema/photosintent/createassets.md) | “Save these to my photos.” |
| [`crop`](appschema/photosintent/crop.md) | “Crop this photo.” or “Trim a bit off the borders.” |
| [`deleteAlbum`](appschema/photosintent/deletealbum.md) | “Trash this album.” or “Get rid of vacation 2024.” |
| [`deleteAssets`](appschema/photosintent/deleteassets.md) | “Delete this photo.” or “Get rid of the three most recent photos.” |
| [`duplicateAssets`](appschema/photosintent/duplicateassets.md) | “Duplicate DSC_001.JPEG.” or “Make a copy of DSC_0123.JPEG.” |
| [`editAsset`](appschema/photosintent/editasset.md) | “Edit this photo.” |
| [`openAlbum`](appschema/photosintent/openalbum.md) | “Open the 2024 album.” or “Show me 2024.” |
| [`openAsset`](appschema/photosintent/openasset.md) | “Open DSC_0123.JPEG.” or “Play IMG_4567.MOV.” |
| [`postToSharedAlbum`](appschema/photosintent/posttosharedalbum.md) | “Share DSC_001.JPEG to the baby shared album.” |
| [`removeAssetsFromAlbum`](appschema/photosintent/removeassetsfromalbum.md) | “Remove this photo from my shared album.” |
| [`setFilter`](appschema/photosintent/setfilter.md) | “Apply the dramatic effect.” or “Remove the filter.” |
| [`setRotation`](appschema/photosintent/setrotation.md) | “Rotate this photo clockwise.” or “Rotate this photo left.” |
| [`setWarmth`](appschema/photosintent/setwarmth.md) | “Apply a warmth value of negative fifty.” |
| [`straighten`](appschema/photosintent/straighten.md) | “Straighten this photo.” or “Make this photo straight.” |
| [`toggleSuggestedEdits`](appschema/photosintent/togglesuggestededits.md) | “Enhance this photo.” or “Make this photo better.” |
| [`updateAlbum`](appschema/photosintent/updatealbum.md) | “Rename vacation 2024 to trip.” |
| [`updateAsset`](appschema/photosintent/updateasset.md) | “Favorite this photo.” or “Hide this photo.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `photos_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Essentials
- [Integrating your photo app with Apple Intelligence](integrating-your-photo-app-with-apple-intelligence.md)
  Adopt photo schemas so people can edit and manage photos with Siri.
### Actions
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
- [AppSchema.PhotosIntent](appschema/photosintent.md)
  Identifies intent schemas in the photos domain.
### Content and parameter types
- [var album: some AppSchemaEntity](appschema/photosentity/album.md)
  An entity schema for an album.
- [var asset: some AppSchemaEntity](appschema/photosentity/asset.md)
  An entity schema for an asset.
- [var recognizedPerson: some AppSchemaEntity](appschema/photosentity/recognizedperson.md)
  An entity schema for a recognized person.
- [AppSchema.PhotosEntity](appschema/photosentity.md)
  Identifies entity schemas in the photos domain.
### Types for static parameters
- [var albumType: some AppSchemaEnum](appschema/photosenum/albumtype.md)
  An enum schema for an album type parameter.
- [var assetType: some AppSchemaEnum](appschema/photosenum/assettype.md)
  An enum schema for an asset type parameter.
- [var filterType: some AppSchemaEnum](appschema/photosenum/filtertype.md)
  An enum schema for a filter type parameter.
- [var rotationDirection: some AppSchemaEnum](appschema/photosenum/rotationdirection.md)
  An enum schema for a rotation direction parameter.
- [AppSchema.PhotosEnum](appschema/photosenum.md)
  Identifies enum schemas in the photos domain.
### Deprecated schemas
- [var search: some AppSchemaIntent](appschema/photosintent/search.md)
  An intent schema that navigates to search results.

## See Also

- [Audio](app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Files](app-schema-domain-files.md)
  Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-photos)*