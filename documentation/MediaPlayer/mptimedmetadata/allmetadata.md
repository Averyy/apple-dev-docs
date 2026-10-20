# allMetadata

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A dictionary containing all the metadata in the object.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var allMetadata: [AnyHashable : Any]! { get }
```

```objc
@property (nonatomic, readonly) NSDictionary * allMetadata;
```

#### Discussion

To retrieve metadata from the dictionary, use the keys described in [Timed metadata dictionary keys](../timed-metadata-dictionary-keys.md).

## See Also

### Extracting timed metadata from a stream
- [var key: String!](./key.md)
  A key that identifies a piece of timed metadata.
- [var keyspace: String!](./keyspace.md)
  The namespace of the identifying key.
- [var timestamp: TimeInterval](./timestamp.md)
  The timestamp of the metadata, in the timebase of the media stream.
- [var value: Any!](./value.md)
  The timed metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/allmetadata)*