# appleMusicID

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

The Apple Music ID for the song.

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
var appleMusicID: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * appleMusicID;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * appleMusicID;
```

## See Also

### Reading Apple Music properties
- [var songs: [Song]](./songs.md)
  An array of MusicKit song objects that represent the song.
- [var appleMusicURL: URL?](./applemusicurl.md)
  A link to the Apple Music page that contains the full information for the song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/applemusicid)*