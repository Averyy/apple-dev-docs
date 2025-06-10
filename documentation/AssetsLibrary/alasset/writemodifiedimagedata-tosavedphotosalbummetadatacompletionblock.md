# writeModifiedImageData(toSavedPhotosAlbum:metadata:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Saves image data to the Saved Photos album.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func writeModifiedImageData(toSavedPhotosAlbum imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func writeModifiedImageData(toSavedPhotosAlbum imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method saves `imageData` to the saved photos album as a new asset that is considered a modified version of the receiver.

## Parameters

- `imageData`: Image data for the asset.
- `metadata`: Metadata for the image.
- `completionBlock`: The block invoked after the save operation completes.

## See Also

- [func writeModifiedVideoAtPath(toSavedPhotosAlbum: URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/writemodifiedvideoatpath(tosavedphotosalbum:completionblock:).md)
  Saves the video at a specified path to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/writemodifiedimagedata(tosavedphotosalbum:metadata:completionblock:))*