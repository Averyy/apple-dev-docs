# artwork

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Artwork for the media item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var artwork: INImage? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INImage * artwork;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INImage * artwork;
```

## See Also

### Describing the Media Item
- [var identifier: String?](./identifier.md)
  The value your app uses to identify the media item.
- [var title: String?](./title.md)
  The media item title.
- [var artist: String?](./artist.md)
  The artist associated with the media item.
- [var type: INMediaItemType](./type.md)
  The media item type.
- [enum INMediaItemType](../inmediaitemtype.md)
  The type of content the media item describes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitem/artwork)*