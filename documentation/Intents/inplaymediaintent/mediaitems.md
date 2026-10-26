# mediaItems

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The media content.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

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

This property is a media item such as a song, audiobook, or podcast episode. Although the array can contain more than one [`INMediaItem`](../inmediaitem.md) object, the system uses only the first item in the array. You set [`mediaItems`](./mediaitems.md) when creating the [`INPlayMediaIntent`](../inplaymediaintent.md) object.

## See Also

### Accessing Media Items
- [var mediaContainer: INMediaItem?](./mediacontainer.md)
  The media item container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent/mediaitems)*