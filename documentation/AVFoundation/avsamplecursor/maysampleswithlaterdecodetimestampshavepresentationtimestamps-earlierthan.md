# maySamplesWithLaterDecodeTimeStampsHavePresentationTimeStamps(earlierThan:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether a sample later in decode order can have a presentation timestamp earlier than that of the specified sample cursor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func maySamplesWithLaterDecodeTimeStampsHavePresentationTimeStamps(earlierThan cursor: AVSampleCursor) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if it’s possible for any sample later in decode order than the sample at the position of the receiver can have a presentation timestamp earlier than that of the specified sample cursor; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Undefined results occur if this cursor and the passed in cursor reference different sequences of samples, such as when they’re created by different instances of [`AVAssetTrack`](avassettrack.md).

## Parameters

- `cursor`: An instance of   with which to test the sample reordering boundary.

## See Also

- [func maySamplesWithEarlierDecodeTimeStampsHavePresentationTimeStamps(laterThan: AVSampleCursor) -> Bool](avsamplecursor/maysampleswithearlierdecodetimestampshavepresentationtimestamps(laterthan:).md)
  Determines whether a sample earlier in decode order can have a presentation timestamp later than that of the specified sample cursor.
- [var samplesRequiredForDecoderRefresh: Int](avsamplecursor/samplesrequiredfordecoderrefresh.md)
  The number of samples prior to the current sample, in decode order, the decoder requires to achieve a coherent output at the current decode time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursor/maysampleswithlaterdecodetimestampshavepresentationtimestamps(earlierthan:))*