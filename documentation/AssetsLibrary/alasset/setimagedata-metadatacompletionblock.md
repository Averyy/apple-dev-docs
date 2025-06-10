# setImageData(_:metadata:completionBlock:)

**Framework**: Assets Library  
**Kind**: method

Replaces the image data in the receiver with given image data

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setImageData(_ imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setImageData(_ imageData: Data!, metadata: [AnyHashable : Any]!) async throws -> URL?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Before invoking this method, you should check the [`isEditable`](alasset/iseditable.md) property of the asset to determine whether it is possible to replace the image data.

## Parameters

- `imageData`: Image data for the asset.
- `metadata`: Metadata for the image.
- `completionBlock`: If the application is not able to edit the asset, the completion blocks return a   asset URL and an  .

## See Also

- [func setVideoAtPath(URL!, completionBlock: ((URL?, (any Error)?) -> Void)!)](alasset/setvideoatpath(_:completionblock:).md)
  Replaces the video data in receiver with the video at a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/setimagedata(_:metadata:completionblock:))*