# count

**Framework**: Media Player  
**Kind**: property

The number of media items in a collection.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var count: Int { get }
```

#### Discussion

In some cases, using this property is more efficient than fetching the [`items`](mpmediaitemcollection/items.md) array and asking for the count.

## See Also

- [var items: [MPMediaItem]](mpmediaitemcollection/items.md)
  The media items in a media item collection.
- [var representativeItem: MPMediaItem?](mpmediaitemcollection/representativeitem.md)
  A media item whose properties are representative of the other media items in a collection.
- [var mediaTypes: MPMediaType](mpmediaitemcollection/mediatypes.md)
  The types of the media items in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/count)*