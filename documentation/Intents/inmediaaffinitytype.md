# INMediaAffinityType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe a user’s affinity for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INMediaAffinityType
```

```c
enum INMediaAffinityType : NSInteger;
```

## Topics

### Constants
- [INMediaAffinityType.unknown](./inmediaaffinitytype/unknown.md)
  A type that indicates the user’s affinity for the media item is unknown.
- [INMediaAffinityType.like](./inmediaaffinitytype/like.md)
  A type that indicates the user likes the media item.
- [INMediaAffinityType.dislike](./inmediaaffinitytype/dislike.md)
  A type that indicates the user dislikes the media item.
### Initializers
- [init?(rawValue: Int)](./inmediaaffinitytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Media Information
- [var affinityType: INMediaAffinityType](./inupdatemediaaffinityintent/affinitytype.md)
  The user’s affinity for the media item.
- [var mediaItems: [INMediaItem]?](./inupdatemediaaffinityintent/mediaitems.md)
  The media items to update.
- [var mediaSearch: INMediaSearch?](./inupdatemediaaffinityintent/mediasearch.md)
  The type of item to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaaffinitytype)*