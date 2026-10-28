# init(identifier:title:type:artwork:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a media item with an identifier, title, type, and artwork.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
convenience init(identifier: String?, title: String?, type: INMediaItemType, artwork: INImage?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier title:(NSString *) title type:(INMediaItemType) type artwork:(INImage *) artwork;
```

## Return Value

A newly initialized media item object.

## Parameters

- `identifier`: The value your app uses to identify the media item.
- `title`: The media title.
- `type`: The media type.
- `artwork`: An image that represents a media item such as an album cover.

## See Also

### Creating a Media Item
- [init(identifier: String?, title: String?, type: INMediaItemType, artwork: INImage?, artist: String?)](./init%28identifier,title,type,artwork,artist%29.md)
  Creates a media item with an identifier, title, type, artwork, and artist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitem/init(identifier:title:type:artwork:))*