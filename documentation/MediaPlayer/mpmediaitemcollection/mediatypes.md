# mediaTypes

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The types of the media items in a collection.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var mediaTypes: MPMediaType { get }
```

```objc
@property (nonatomic, readonly) MPMediaType mediaTypes;
```

#### Discussion

The [`MPMediaType`](../mpmediatype.md) enumeration in [`MPMediaItem`](../mpmediaitem.md) lists the media types.

## See Also

### Using a media item collection
- [var items: [MPMediaItem]](./items.md)
  The media items in a media item collection.
- [var representativeItem: MPMediaItem?](./representativeitem.md)
  A media item whose properties are representative of the other media items in a collection.
- [var count: Int](./count.md)
  The number of media items in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/mediatypes)*