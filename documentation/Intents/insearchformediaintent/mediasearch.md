# mediaSearch

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location to search for the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var mediaSearch: INMediaSearch? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INMediaSearch * mediaSearch;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INMediaSearch * mediaSearch;
```

## Discussion

Depending on the user’s request, you may need to search for a particular media item. For example, adding a specific song would set `mediaSearch` to [`mediaName`](../inmediasearch/medianame.md) to “name” and [`mediaType`](../inmediasearch/mediatype.md) to [`INMediaItemType.song`](../inmediaitemtype/song.md).

## See Also

### Searching for Media
- [var mediaItems: [INMediaItem]?](./mediaitems.md)
  The media items for which to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintent/mediasearch)*