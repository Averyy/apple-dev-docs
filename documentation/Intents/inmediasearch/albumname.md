# albumName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the album to search for.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var albumName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * albumName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * albumName;
```

#### Discussion

Only use this property for combination queries in conjunction with the [`mediaName`](./medianame.md) property. For example, “Play the song requestedSongName on the album requestedAlbumName by requestedArtistName”.

```swift
{
  mediaName: requestedSongName
  mediaType: song
  albumName: requestedAlbumName
  artistName: requestedArtistName
}
```

Do not use this property when the user requests to play an album. For example, “Play the album requestedAlbumName”.

```swift
{
  mediaName: requestedAlbumName
  mediaType: album
}
```

## See Also

### Modifying the Media Name
- [var artistName: String?](./artistname.md)
  The name of the artist to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediasearch/albumname)*