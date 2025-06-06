# fetch(shazamID:completionHandler:)

**Framework**: ShazamKit  
**Kind**: method

Requests the media item for the song with the specified Shazam ID.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class func fetch(shazamID: String) async throws -> SHMediaItem
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func fetch(shazamID: String) async throws -> SHMediaItem
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func fetch(shazamID: String) async throws -> SHMediaItem
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `shazamID`: The Shazam ID of the song.
- `completionHandler`: This block takes the following parameters:

## See Also

- [var webURL: URL?](shmediaitem/weburl.md)
  A link to the Shazam Music catalog page that contains the full information for the song.
- [var shazamID: String?](shmediaitem/shazamid.md)
  The Shazam ID for the song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/fetch(shazamid:completionhandler:))*