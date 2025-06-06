# AssistantSchemas.PhotosIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that offer photo and video functionality.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol PhotosIntent : AssistantSchemas.Model
```

## Mentions

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)

## Topics

### Instance Properties
- [var addAssetsToAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/addassetstoalbum.md)
  The app intent conforms to the schema for adding an asset to an album.
- [var cleanupPhoto: some AssistantSchemas.Intent](assistantschemas/photosintent/cleanupphoto.md)
  The app intent conforms to the schema for undoing edits to an asset.
- [var copyEdits: some AssistantSchemas.Intent](assistantschemas/photosintent/copyedits.md)
  The app intent conforms to the schema for copying edits to an asset.
- [var createAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/createalbum.md)
  The app intent conforms to the schema for creating an album.
- [var createAssets: some AssistantSchemas.Intent](assistantschemas/photosintent/createassets.md)
  The app intent conforms to the schema for creating an asset.
- [var crop: some AssistantSchemas.Intent](assistantschemas/photosintent/crop.md)
  The app intent conforms to the schema for cropping an asset.
- [var deleteAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/deletealbum.md)
  The app intent conforms to the schema for deleting an album.
- [var deleteAssets: some AssistantSchemas.Intent](assistantschemas/photosintent/deleteassets.md)
  The app intent conforms to the schema for deleting an asset.
- [var duplicateAssets: some AssistantSchemas.Intent](assistantschemas/photosintent/duplicateassets.md)
  The app intent conforms to the schema for duplicating an asset.
- [var openAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/openalbum.md)
  The app intent conforms to the schema for opening an album.
- [var openAsset: some AssistantSchemas.Intent](assistantschemas/photosintent/openasset.md)
  The app intent conforms to the schema for opening an asset.
- [var pasteEdits: some AssistantSchemas.Intent](assistantschemas/photosintent/pasteedits.md)
  The app intent conforms to the schema for pasting edits to an asset.
- [var postToSharedAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/posttosharedalbum.md)
  The app intent conforms to the schema for posting an asset to a shared album.
- [var removeAssetsFromAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/removeassetsfromalbum.md)
  The app intent conforms to the schema for removing an asset from an album.
- [var search: some AssistantSchemas.Intent](assistantschemas/photosintent/search.md)
  The app intent conforms to the schema for searching the content in the media library.
- [var setDepth: some AssistantSchemas.Intent](assistantschemas/photosintent/setdepth.md)
  The app intent conforms to the schema for setting the aperture of an asset.
- [var setExposure: some AssistantSchemas.Intent](assistantschemas/photosintent/setexposure.md)
  The app intent conforms to the schema for setting the exposure of an asset.
- [var setFilter: some AssistantSchemas.Intent](assistantschemas/photosintent/setfilter.md)
  The app intent conforms to the schema for applying a filter to an asset.
- [var setRotation: some AssistantSchemas.Intent](assistantschemas/photosintent/setrotation.md)
  The app intent conforms to the schema for rotating an asset.
- [var setSaturation: some AssistantSchemas.Intent](assistantschemas/photosintent/setsaturation.md)
  The app intent conforms to the schema for setting the saturation of an asset.
- [var setWarmth: some AssistantSchemas.Intent](assistantschemas/photosintent/setwarmth.md)
  The app intent conforms to the schema for setting the warmth of an asset.
- [var straighten: some AssistantSchemas.Intent](assistantschemas/photosintent/straighten.md)
  The app intent conforms to the schema for straightening an asset.
- [var toggleDepth: some AssistantSchemas.Intent](assistantschemas/photosintent/toggledepth.md)
  The app intent conforms to the schema for toggling the depth of an asset.
- [var toggleSuggestedEdits: some AssistantSchemas.Intent](assistantschemas/photosintent/togglesuggestededits.md)
  The app intent conforms to the schema for enhancing an asset.
- [var updateAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/updatealbum.md)
  The app intent conforms to the schema for updating an album.
- [var updateAsset: some AssistantSchemas.Intent](assistantschemas/photosintent/updateasset.md)
  The app intent conforms to the schema for updating an asset.
- [var updateRecognizedPerson: some AssistantSchemas.Intent](assistantschemas/photosintent/updaterecognizedperson.md)
  The app intent conforms to the schema for updating a recognized person in an asset.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s photo and video functionality with Siri and Apple Intelligence.
- [AssistantSchemas.PhotosEntity](assistantschemas/photosentity.md)
  Assistant schema conformance for app entities that describe media assets.
- [AssistantSchemas.PhotosEnum](assistantschemas/photosenum.md)
  Assistant schema conformance for types you use to describe photos and videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosintent)*