# Photos

**Framework**: App Intents

App intent schemas you use for photo and video functionality and content.

## Topics

### Essentials
- [Making photo and video actions available to Siri and Apple Intelligence](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s photo and video functionality with Siri and Apple Intelligence.
### Actions
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
- [AssistantSchemas.PhotosIntent](assistantschemas/photosintent.md)
  Assistant schema conformance for app intents that offer photo and video functionality.
### Content and parameter types
- [var album: some AssistantSchemas.Entity](assistantschemas/photosentity/album.md)
  The app entity describes an album.
- [var asset: some AssistantSchemas.Entity](assistantschemas/photosentity/asset.md)
- [var recognizedPerson: some AssistantSchemas.Entity](assistantschemas/photosentity/recognizedperson.md)
  The app entity describes a person who appears in an asset.
- [AssistantSchemas.PhotosEntity](assistantschemas/photosentity.md)
  Assistant schema conformance for app entities that describe media assets.
### Types for static parameters
- [var albumType: some AssistantSchemas.Enum](assistantschemas/photosenum/albumtype.md)
  The type of photo album.
- [var assetType: some AssistantSchemas.Enum](assistantschemas/photosenum/assettype.md)
  The type of asset.
- [var filterType: some AssistantSchemas.Enum](assistantschemas/photosenum/filtertype.md)
  The filter effect for a photo or video.
- [var rotationDirection: some AssistantSchemas.Enum](assistantschemas/photosenum/rotationdirection.md)
  The direction for rotating a photo or video.
- [AssistantSchemas.PhotosEnum](assistantschemas/photosenum.md)
  Assistant schema conformance for types you use to describe photos and videos.

## See Also

- [Assistant](app-intent-domain-assistant.md)
  An app intent schema that lets people in Japan configure the side button of iPhone to launch your voice-based conversational app.
- [Books](app-intent-domain-books.md)
  App intent schemas you use for ebook reader functionality and content.
- [Browser](app-intent-domain-browser.md)
  App intent schemas you use for web browsing functionality and content.
- [Camera](app-intent-domain-camera.md)
  App intent schemas you use for camera functionality and content.
- [File management](app-intent-domain-file-management.md)
  App intent schemas you use for file management functionality and content.
- [Journaling](app-intent-domain-journaling.md)
  App intent schemas you use for journaling functionality and content.
- [Mail](app-intent-domain-mail.md)
  App intent schemas you use for email clients.
- [Presentations](app-intent-domain-presentation.md)
  App intent schemas you use for presentation functionality and content.
- [Reader](app-intent-domain-reader.md)
  App intent schemas you use for document reading functionality and content.
- [Spreadsheet](app-intent-domain-spreadsheet.md)
  App intent schemas you use for spreadsheet functionality and content.
- [System and in-app search](app-intent-domain-system-and-search.md)
  App intent schemas you use for in-app search functionality and content.
- [Visual intelligence](app-intent-domain-visual-intelligence.md)
  An app intent schema that lets you integrate your app with visual intelligence.
- [Whiteboard](app-intent-domain-whiteboard.md)
  App intent schemas you use for whiteboard functionality and content.
- [Word proccessor](app-intent-domain-wordprocessor.md)
  App intent schemas you use for text editing functionality and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-intent-domain-photos)*