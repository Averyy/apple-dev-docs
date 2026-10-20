# representativeItem

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A media item whose properties are representative of the other media items in a collection.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var representativeItem: MPMediaItem? { get }
```

```objc
@property (nonatomic, readonly, nullable) MPMediaItem * representativeItem;
```

#### Discussion

The media items in a collection typically share common property values, owing to how you built the collection. For example, if you build a collection based on a predicate that uses the [`MPMediaItemPropertyArtist`](../mpmediaitempropertyartist.md) property, all items in the collection share the same artist name. You can use the `representativeItem` property to efficiently obtain values for such common properties—often more efficiently than fetching an item from the [`items`](./items.md) array.

## See Also

### Using a media item collection
- [var items: [MPMediaItem]](./items.md)
  The media items in a media item collection.
- [var count: Int](./count.md)
  The number of media items in a collection.
- [var mediaTypes: MPMediaType](./mediatypes.md)
  The types of the media items in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/representativeitem)*