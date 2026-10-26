# artist

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The artist associated with the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var artist: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * artist;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * artist;
```

## See Also

### Describing the Media Item
- [var artwork: INImage?](./artwork.md)
  Artwork for the media item.
- [var identifier: String?](./identifier.md)
  The value your app uses to identify the media item.
- [var title: String?](./title.md)
  The media item title.
- [var type: INMediaItemType](./type.md)
  The media item type.
- [enum INMediaItemType](../inmediaitemtype.md)
  The type of content the media item describes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitem/artist)*