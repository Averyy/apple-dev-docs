# mediaDestinationType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The destination of the media your app adds.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var mediaDestinationType: INMediaDestinationType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INMediaDestinationType mediaDestinationType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INMediaDestinationType mediaDestinationType;
```

#### Discussion

This property indicates whether to add the media item to the library or a playlist.

## See Also

### Describing the Media Destination
- [var playlistName: String?](./playlistname.md)
  The name of the playlist to which you add the media.
- [enum INMediaDestinationType](../inmediadestinationtype.md)
  Constants that describe the different media destination types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationreference/mediadestinationtype)*