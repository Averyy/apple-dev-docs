# items

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The media items in a media item collection.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var items: [MPMediaItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<MPMediaItem *> * items;
```

## See Also

### Using a media item collection
- [var representativeItem: MPMediaItem?](./representativeitem.md)
  A media item whose properties are representative of the other media items in a collection.
- [var count: Int](./count.md)
  The number of media items in a collection.
- [var mediaTypes: MPMediaType](./mediatypes.md)
  The types of the media items in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/items)*