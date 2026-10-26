# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The value your app uses to identify the media item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var identifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * identifier;
```

## See Also

### Describing the Media Item
- [var artwork: INImage?](./artwork.md)
  Artwork for the media item.
- [var title: String?](./title.md)
  The media item title.
- [var artist: String?](./artist.md)
  The artist associated with the media item.
- [var type: INMediaItemType](./type.md)
  The media item type.
- [enum INMediaItemType](../inmediaitemtype.md)
  The type of content the media item describes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitem/identifier)*