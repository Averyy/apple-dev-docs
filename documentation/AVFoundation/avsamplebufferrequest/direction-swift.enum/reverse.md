# AVSampleBufferRequest.Direction.reverse

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The number of previous samples may be zero or greater.

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
case reverse
```

```c
AVSampleBufferRequestDirectionReverse
```

#### Discussion

The number of previous samples allowed is subject to the [`limitCursor`](../limitcursor.md), [`preferredMinSampleCount`](../preferredminsamplecount.md), and [`maxSampleCount`](../maxsamplecount.md) property values.

## See Also

### Buffer direction
- [AVSampleBufferRequest.Direction.forward](./forward.md)
  The number of following samples may be zero or greater.
- [AVSampleBufferRequest.Direction.none](./none.md)
  A single sample will be loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/reverse)*