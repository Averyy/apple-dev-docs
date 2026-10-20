# appleMusicURL

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

A link to the Apple Music page that contains the full information for the song.

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
var appleMusicURL: URL? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) NSURL * appleMusicURL;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) NSURL * appleMusicURL;
```

## See Also

### Reading Apple Music properties
- [var songs: [Song]](./songs.md)
  An array of MusicKit song objects that represent the song.
- [var appleMusicID: String?](./applemusicid.md)
  The Apple Music ID for the song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/applemusicurl)*