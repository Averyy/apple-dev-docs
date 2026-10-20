# offset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The offset of a sample in the segment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger offset;
```

## See Also

### Inspecting the information
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The presentation timestamp (PTS) of a sample.
- [var length: Int](./length.md)
  The length of the sample data.
- [var isSyncSample: Bool](./issyncsample.md)
  A Boolean value that indicates whether the sample is a key frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreportsampleinformation/offset)*