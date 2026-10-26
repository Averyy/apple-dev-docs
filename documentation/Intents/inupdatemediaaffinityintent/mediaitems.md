# mediaItems

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The media items to update.

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

A media item such as a song, audiobook, or podcast episode. Although the array can contain more than one [`INMediaItem`](../inmediaitem.md) object, the system uses only the first item in the array. You set [`mediaItems`](./mediaitems.md) when creating the [`INSearchForMediaIntent`](../insearchformediaintent.md) object.

## See Also

### Getting the Media Information
- [var affinityType: INMediaAffinityType](./affinitytype.md)
  The user’s affinity for the media item.
- [enum INMediaAffinityType](../inmediaaffinitytype.md)
  Constants that describe a user’s affinity for a media item.
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  The type of item to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintent/mediaitems)*