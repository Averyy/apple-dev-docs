# shazamID

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

The Shazam ID for the song.

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
var shazamID: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * shazamID;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * shazamID;
```

## See Also

### Working with Shazam music catalog media items
- [var webURL: URL?](./weburl.md)
  A link to the Shazam Music catalog page that contains the full information for the song.
- [class func fetch(shazamID: String, completionHandler: (SHMediaItem?, (any Error)?) -> Void)](./fetch%28shazamid,completionhandler%29.md)
  Requests the media item for the song with the specified Shazam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/shazamid)*