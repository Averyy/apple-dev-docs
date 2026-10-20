# key

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A key that identifies a piece of timed metadata.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var key: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * key;
```

## See Also

### Extracting timed metadata from a stream
- [var allMetadata: [AnyHashable : Any]!](./allmetadata.md)
  A dictionary containing all the metadata in the object.
- [var keyspace: String!](./keyspace.md)
  The namespace of the identifying key.
- [var timestamp: TimeInterval](./timestamp.md)
  The timestamp of the metadata, in the timebase of the media stream.
- [var value: Any!](./value.md)
  The timed metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/key)*