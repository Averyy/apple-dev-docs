# allMetadata

**Framework**: Media Player  
**Kind**: property

A dictionary containing all the metadata in the object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var allMetadata: [AnyHashable : Any]! { get }
```

#### Discussion

To retrieve metadata from the dictionary, use the keys described in [`Timed metadata dictionary keys`](timed-metadata-dictionary-keys.md).

## See Also

- [var key: String!](mptimedmetadata/key.md)
  A key that identifies a piece of timed metadata.
- [var keyspace: String!](mptimedmetadata/keyspace.md)
  The namespace of the identifying key.
- [var timestamp: TimeInterval](mptimedmetadata/timestamp.md)
  The timestamp of the metadata, in the timebase of the media stream.
- [var value: Any!](mptimedmetadata/value.md)
  The timed metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/allmetadata)*