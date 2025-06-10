# AVSampleBufferRequest.Mode.opportunistic

**Framework**: AVFoundation  
**Kind**: case

A mode that indicates that opportunistic sample buffer creation requests load data as soon as possible.

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
case opportunistic
```

#### Discussion

In situations with multiple competing requests, a sample buffer generator may defer an opportunistic request in favor of another immediate request, or a scheduled requests with a presentation time close to the timebase time.

> ❗ **Important**:  The system may postpone an opportunistic request indefinitely. Don’t use this mode for time-sensitive processing.

## See Also

- [AVSampleBufferRequest.Mode.immediate](avsamplebufferrequest/mode-swift.enum/immediate.md)
  A mode that indicates that sample buffer creation requests load data as soon as possible.
- [AVSampleBufferRequest.Mode.scheduled](avsamplebufferrequest/mode-swift.enum/scheduled.md)
  A mode that indicates that sample buffer creation requests load data according to a scheduled deadline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum/opportunistic)*