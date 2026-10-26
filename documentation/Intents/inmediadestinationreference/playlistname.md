# playlistName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the playlist to which you add the media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var playlistName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * playlistName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * playlistName;
```

## See Also

### Describing the Media Destination
- [var mediaDestinationType: INMediaDestinationType](./mediadestinationtype.md)
  The destination of the media your app adds.
- [enum INMediaDestinationType](../inmediadestinationtype.md)
  Constants that describe the different media destination types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationreference/playlistname)*