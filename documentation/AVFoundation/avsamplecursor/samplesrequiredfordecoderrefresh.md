# samplesRequiredForDecoderRefresh

**Framework**: AVFoundation  
**Kind**: property

The number of samples prior to the current sample, in decode order, the decoder requires to achieve a coherent output at the current decode time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.11+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var samplesRequiredForDecoderRefresh: Int { get }
```

#### Discussion

This property value is 0 when the decoder doesn’t require samples for refresh or when the track doesn’t contain this information.

Some sample sequences don’t indicate sample dependencies and instead indicate to decode a specific sample with all available accuracy. The system must decode samples in decode order before decoding the specific sample.

## See Also

- [func maySamplesWithEarlierDecodeTimeStampsHavePresentationTimeStamps(laterThan: AVSampleCursor) -> Bool](avsamplecursor/maysampleswithearlierdecodetimestampshavepresentationtimestamps(laterthan:).md)
  Determines whether a sample earlier in decode order can have a presentation timestamp later than that of the specified sample cursor.
- [func maySamplesWithLaterDecodeTimeStampsHavePresentationTimeStamps(earlierThan: AVSampleCursor) -> Bool](avsamplecursor/maysampleswithlaterdecodetimestampshavepresentationtimestamps(earlierthan:).md)
  Determines whether a sample later in decode order can have a presentation timestamp earlier than that of the specified sample cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursor/samplesrequiredfordecoderrefresh)*