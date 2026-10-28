# presentationTimeStamp

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The presentation timestamp (PTS) of a sample.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var presentationTimeStamp: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime presentationTimeStamp;
```

## Discussion

This timestamp may be different from the [`earliestPresentationTimeStamp`](../avassetsegmenttrackreport/earliestpresentationtimestamp.md) if the video’s author encodes it using frame reordering.

## See Also

### Inspecting the information
- [var offset: Int](./offset.md)
  The offset of a sample in the segment.
- [var length: Int](./length.md)
  The length of the sample data.
- [var isSyncSample: Bool](./issyncsample.md)
  A Boolean value that indicates whether the sample is a key frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreportsampleinformation/presentationtimestamp)*