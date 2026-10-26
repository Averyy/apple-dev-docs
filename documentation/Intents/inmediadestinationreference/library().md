# library()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a new library destination for the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func library() -> Self
```

```objc
+ (instancetype) libraryDestination;
```

#### Return Value

A new [`INMediaDestinationReference`](../inmediadestinationreference.md) object or `nil` if unable to create.

#### Discussion

A library is a generic concept that you must define for your app. For example, in Apple Music, it’s the Apple Music library, while in Podcasts, it’s the user’s subscribed podcasts.

## See Also

### Creating a Media Destination Object
- [class func playlistDestination(withName: String) -> Self](./playlistdestination%28withname%29.md)
  Creates a new playlist destination for the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationreference/library())*