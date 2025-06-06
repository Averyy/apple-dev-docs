# add(_:completionHandler:)

**Framework**: Shazamkit  
**Kind**: method

Adds an array of songs to the user’s Shazam library.

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
func add(_ mediaItems: [SHMediaItem]) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func add(_ mediaItems: [SHMediaItem]) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Saving a song to the user’s Shazam library also saves the following media item properties and their associated values:

- [`shazamID`](shmediaitemproperty/shazamid.md)
- [`title`](shmediaitemproperty/title.md)
- [`subtitle`](shmediaitemproperty/subtitle.md), or [`artist`](shmediaitemproperty/artist.md) if the subtitle is unavailable

> **Note**:  Saving to the user’s Shazam library works only for songs with a valid [`shazamID`](shmediaitemproperty/shazamid.md).

## Parameters

- `mediaItems`: An array of media items that represents the songs to add to the library.
- `completionHandler`: This block takes the following parameters:

## See Also

- [class var `default`: SHMediaLibrary](shmedialibrary/default.md)
  An instance of the user’s default Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmedialibrary/add(_:completionhandler:))*