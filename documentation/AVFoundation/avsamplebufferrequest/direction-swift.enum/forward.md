# AVSampleBufferRequest.Direction.forward

**Framework**: AVFoundation  
**Kind**: case

The number of following samples may be zero or greater.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case forward
```

#### Discussion

The number of following samples allowed is subject to the [`limitCursor`](avsamplebufferrequest/limitcursor.md), [`preferredMinSampleCount`](avsamplebufferrequest/preferredminsamplecount.md), and [`maxSampleCount`](avsamplebufferrequest/maxsamplecount.md) property values.

## See Also

- [AVSampleBufferRequest.Direction.none](avsamplebufferrequest/direction-swift.enum/none.md)
  A single sample will be loaded.
- [AVSampleBufferRequest.Direction.reverse](avsamplebufferrequest/direction-swift.enum/reverse.md)
  The number of previous samples may be zero or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/forward)*