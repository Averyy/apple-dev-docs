# keyspace

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The namespace of the identifying key.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var keyspace: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * keyspace;
```

## See Also

### Extracting timed metadata from a stream
- [var allMetadata: [AnyHashable : Any]!](./allmetadata.md)
  A dictionary containing all the metadata in the object.
- [var key: String!](./key.md)
  A key that identifies a piece of timed metadata.
- [var timestamp: TimeInterval](./timestamp.md)
  The timestamp of the metadata, in the timebase of the media stream.
- [var value: Any!](./value.md)
  The timed metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/keyspace)*