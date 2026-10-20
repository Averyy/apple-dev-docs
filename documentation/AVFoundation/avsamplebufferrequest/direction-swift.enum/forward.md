# AVSampleBufferRequest.Direction.forward

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The number of following samples may be zero or greater.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case forward
```

```c
AVSampleBufferRequestDirectionForward
```

#### Discussion

The number of following samples allowed is subject to the [`limitCursor`](../limitcursor.md), [`preferredMinSampleCount`](../preferredminsamplecount.md), and [`maxSampleCount`](../maxsamplecount.md) property values.

## See Also

### Buffer direction
- [AVSampleBufferRequest.Direction.none](./none.md)
  A single sample will be loaded.
- [AVSampleBufferRequest.Direction.reverse](./reverse.md)
  The number of previous samples may be zero or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/forward)*