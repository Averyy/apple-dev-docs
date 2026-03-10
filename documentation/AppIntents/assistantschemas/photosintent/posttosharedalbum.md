# postToSharedAlbum

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for posting an asset to a shared album.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var postToSharedAlbum: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.photos.postToSharedAlbum` schema:

```swift
@AppIntent(schema: .photos.postToSharedAlbum)
struct PostToSharedAlbumIntent: AppIntent {
    @Parameter
    var sharedAlbum: PhotoAlbumEntity

    @Parameter
    var assets: [PhotoEntity]?

    @Parameter
    var files: [IntentFile]?

    @Parameter
    var comment: String?

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.photos` app intent domain, see [`Making photo and video actions available to Siri and Apple Intelligence`](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

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
- [var removeAssetsFromAlbum: some AssistantSchemas.Intent](assistantschemas/photosintent/removeassetsfromalbum.md)
  The app intent conforms to the schema for removing an asset from an album.
- [var search: some AssistantSchemas.Intent](assistantschemas/photosintent/search.md)
  The app intent conforms to the schema for searching the content in the media library.
- [var setDepth: some AssistantSchemas.Intent](assistantschemas/photosintent/setdepth.md)
  The app intent conforms to the schema for setting the aperture of an asset.
- [var setExposure: some AssistantSchemas.Intent](assistantschemas/photosintent/setexposure.md)
  The app intent conforms to the schema for setting the exposure of an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosintent/posttosharedalbum)*