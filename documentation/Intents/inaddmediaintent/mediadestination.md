# mediaDestination

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location for the media to add.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mediaDestination: INMediaDestination? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INMediaDestination * mediaDestination;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INMediaDestination * mediaDestination;
```

## See Also

### Accessing the Media
- [var mediaItems: [INMediaItem]?](./mediaitems.md)
  The media content to add.
- [var mediaSearch: INMediaSearch?](./mediasearch.md)
  The location to search for the media item to add.
- [enum INMediaDestination](../inmediadestination-swift.enum.md)
  An object that describes the destination for a media item.
- [class INMediaDestinationReference](../inmediadestinationreference.md)
  An object that describes the destination for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintent/mediadestination)*