# writeModifiedVideoAtPath(toSavedPhotosAlbum:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Saves the video at a specified path to the Saved Photos album.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func writeModifiedVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func writeModifiedVideoAtPath(toSavedPhotosAlbum videoPathURL: URL!) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method saves the video at `videoPathURL` to the Saved Photos album as a new asset that is considered a modified version of the receiver.

## Parameters

- `videoPathURL`: An URL that specifies the location of video data.
- `completionBlock`: The block invoked after the save operation completes.

## See Also

- [func writeModifiedImageData(toSavedPhotosAlbum: Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/writemodifiedimagedata(tosavedphotosalbum:metadata:completionblock:).md)
  Saves image data to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/writemodifiedvideoatpath(tosavedphotosalbum:completionblock:))*