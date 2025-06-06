# writeImageData(toSavedPhotosAlbum:metadata:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Writes given image data and metadata to the Photos Album.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeImageData(toSavedPhotosAlbum imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func writeImageData(toSavedPhotosAlbum imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func writeImageData(toSavedPhotosAlbum imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If there is a conflict between the metadata in the image data and the metadata dictionary, the image data metadata values will be overwritten.

## Parameters

- `imageData`: Data for the image to add to the album.
- `metadata`: The metadata to associate with the image.
- `completionBlock`: For a description of the block, see  .

## See Also

- [func writeVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)](alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:).md)
  Saves a video identified by a given URL to the Saved Photos album.
- [func videoAtPathIs(compatibleWithSavedPhotosAlbum: URL!) -> Bool](alassetslibrary/videoatpathis(compatiblewithsavedphotosalbum:).md)
  Returns a Boolean value that indicates whether a video identified by a given URL is compatible with the Saved Photos album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, orientation: ALAssetOrientation, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md)
  Saves a given image to the Saved Photos album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, metadata: [AnyHashable : Any]!, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](alassetslibrary/writeimage(tosavedphotosalbum:metadata:completionblock:).md)
  Writes a given image and metadata to the Photos Album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/writeimagedata(tosavedphotosalbum:metadata:completionblock:))*