# mediaItems

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The media content to add.

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

## Discussion

A media item such as a song, audiobook, or podcast episode. Although the array can contain more than one [`INMediaItem`](../inmediaitem.md) object, the system uses only the first item in the array. You set [`mediaItems`](../inplaymediaintent/mediaitems.md) when creating the [`INAddMediaIntent`](../inaddmediaintent.md) object.

## See Also

### Accessing the Media
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  The location to search for the media item to add.
- [var mediaDestination: INMediaDestination?](./mediadestination.md)
  The location for the media to add.
- [enum INMediaDestination](../inmediadestination-swift.enum.md)
  An object that describes the destination for a media item.
- [class INMediaDestinationReference](../inmediadestinationreference.md)
  An object that describes the destination for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintent/mediaitems)*