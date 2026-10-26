# mediaItems

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The media items for which to search.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mediaItems: [INMediaItem]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INMediaItem *> * mediaItems;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INMediaItem *> * mediaItems;
```

#### Discussion

A media item such as a song, TV show, or podcast episode. Although the array can contain more than one [`INMediaItem`](../inmediaitem.md) object, the system uses only the first item in the array. You set [`mediaItems`](./mediaitems.md) when creating the [`INSearchForMediaIntent`](../insearchformediaintent.md) object.

## See Also

### Searching for Media
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  The location to search for the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintent/mediaitems)*