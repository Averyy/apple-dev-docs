# writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Saves a video identified by a given URL to the Saved Photos album.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func writeVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func writeVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `videoPathURL`: An URL that points to a video file.
- `completionBlock`: For a description of the block, see  .

## See Also

- [func videoAtPathIs(compatibleWithSavedPhotosAlbum: URL!) -> Bool](alassetslibrary/videoatpathis(compatiblewithsavedphotosalbum:).md)
  Returns a Boolean value that indicates whether a video identified by a given URL is compatible with the Saved Photos album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, orientation: ALAssetOrientation, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md)
  Saves a given image to the Saved Photos album.
- [func writeImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimagedata(tosavedphotosalbum:metadata:completionblock:).md)
  Writes given image data and metadata to the Photos Album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:metadata:completionblock:).md)
  Writes a given image and metadata to the Photos Album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:))*