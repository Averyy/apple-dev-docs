# setVideoAtPath(_:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Replaces the video data in receiver with the video at a given URL.

## Declaration

```swift
func setVideoAtPath(_ videoPathURL: URL!) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setVideoAtPath(_ videoPathURL: URL!) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Before invoking this method, you should check the [`isEditable`](alasset/iseditable.md) property of the asset to determine whether it is possible to replace the video data.

## Parameters

- `videoPathURL`: An URL that specifies the location of video data.
- `completionBlock`: If the application is not able to edit the asset, the completion blocks return a   asset URL and an  .

## See Also

- [func setImageData(Data!, metadata: [AnyHashable : Any]!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/setimagedata(_:metadata:completionblock:).md)
  Replaces the image data in the receiver with given image data


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/setvideoatpath(_:completionblock:))*