# webURL

**Framework**: ShazamKit  
**Kind**: property

A link to the Shazam Music catalog page that contains the full information for the song.

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
var webURL: URL? { get }
```

#### Discussion

This link opens the Shazam app or App Clip if it’s available on the device.

## See Also

- [var shazamID: String?](shmediaitem/shazamid.md)
  The Shazam ID for the song.
- [class func fetch(shazamID: String, completionHandler: (SHMediaItem?, (any Error)?) -> Void)](shmediaitem/fetch(shazamid:completionhandler:).md)
  Requests the media item for the song with the specified Shazam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/weburl)*