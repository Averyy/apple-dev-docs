# AVSampleBufferRequest.Direction.none

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

A single sample will be loaded.

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
case none
```

```c
AVSampleBufferRequestDirectionNone
```

#### Discussion

When this constant is set, the [`limitCursor`](../limitcursor.md), [`preferredMinSampleCount`](../preferredminsamplecount.md), and [`maxSampleCount`](../maxsamplecount.md) properties are ignored.

## See Also

### Buffer direction
- [AVSampleBufferRequest.Direction.forward](./forward.md)
  The number of following samples may be zero or greater.
- [AVSampleBufferRequest.Direction.reverse](./reverse.md)
  The number of previous samples may be zero or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/none)*