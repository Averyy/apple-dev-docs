# affinityType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s affinity for the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var affinityType: INMediaAffinityType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INMediaAffinityType affinityType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INMediaAffinityType affinityType;
```

## See Also

### Getting the Media Information
- [enum INMediaAffinityType](../inmediaaffinitytype.md)
  Constants that describe a user’s affinity for a media item.
- [var mediaItems: [INMediaItem]?](./mediaitems.md)
  The media items to update.
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  The type of item to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintent/affinitytype)*