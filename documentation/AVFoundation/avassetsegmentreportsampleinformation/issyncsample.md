# isSyncSample

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the sample is a key frame.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isSyncSample: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isSyncSample;
```

## See Also

### Inspecting the information
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The presentation timestamp (PTS) of a sample.
- [var offset: Int](./offset.md)
  The offset of a sample in the segment.
- [var length: Int](./length.md)
  The length of the sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreportsampleinformation/issyncsample)*