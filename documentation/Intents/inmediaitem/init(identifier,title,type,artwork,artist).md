# init(identifier:title:type:artwork:artist:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a media item with an identifier, title, type, artwork, and artist.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(identifier: String?, title: String?, type: INMediaItemType, artwork: INImage?, artist: String?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier title:(NSString *) title type:(INMediaItemType) type artwork:(INImage *) artwork artist:(NSString *) artist;
```

#### Return Value

A newly initialized media item object.

## Parameters

- `identifier`: The value your app uses to identify the media item.
- `title`: The media title.
- `type`: The media type.
- `artwork`: An image that represents a media item such as an album cover.
- `artist`: A string identifying the artist for the media item.

## See Also

### Creating a Media Item
- [convenience init(identifier: String?, title: String?, type: INMediaItemType, artwork: INImage?)](./init%28identifier,title,type,artwork%29.md)
  Creates a media item with an identifier, title, type, and artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitem/init(identifier:title:type:artwork:artist:))*