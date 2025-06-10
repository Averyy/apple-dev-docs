# writeImage(toSavedPhotosAlbum:orientation:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Saves a given image to the Saved Photos album.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func writeImage(toSavedPhotosAlbum imageRef: CGImage!, orientation: ALAssetOrientation) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func writeImage(toSavedPhotosAlbum imageRef: CGImage!, orientation: ALAssetOrientation) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If you want to save a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object, you can use the `UIImage` method [`CGImage`](https://developer.apple.com/documentation/uikit/uiimage/1624159-cgimage) to get a `CGImageRef`, and cast the image’s [`imageOrientation`](https://developer.apple.com/documentation/UIKit/UIImage/imageOrientation) to `ALAssetOrientation`.

## Parameters

- `imageRef`: The image to save to the Saved Photos album.
- `orientation`: The orientation at which to save the image.
- `completionBlock`: For a description of the block, see  .

## See Also

- [func writeVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:).md)
  Saves a video identified by a given URL to the Saved Photos album.
- [func videoAtPathIs(compatibleWithSavedPhotosAlbum: URL!) -> Bool](alassetslibrary/videoatpathis(compatiblewithsavedphotosalbum:).md)
  Returns a Boolean value that indicates whether a video identified by a given URL is compatible with the Saved Photos album.
- [func writeImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimagedata(tosavedphotosalbum:metadata:completionblock:).md)
  Writes given image data and metadata to the Photos Album.
- [func writeImage(toSavedPhotosAlbum: CGImage!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alassetslibrary/writeimage(tosavedphotosalbum:metadata:completionblock:).md)
  Writes a given image and metadata to the Photos Album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:))*