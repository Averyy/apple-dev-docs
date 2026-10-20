# webURL

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSURL * webURL;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSURL * webURL;
```

#### Discussion

This link opens the Shazam app or App Clip if it’s available on the device.

## See Also

### Working with Shazam music catalog media items
- [var shazamID: String?](./shazamid.md)
  The Shazam ID for the song.
- [class func fetch(shazamID: String, completionHandler: (SHMediaItem?, (any Error)?) -> Void)](./fetch%28shazamid,completionhandler%29.md)
  Requests the media item for the song with the specified Shazam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/weburl)*