# next()

**Framework**: AVFoundation  
**Kind**: method

Retruns the next piece of media data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func next() async throws -> Payload?
```

#### Return Value

Returns the next piece of media data with the specified Payload type. If no more media data is available, this method returns nil.

#### Discussion

> **Note**: If the underlying reader encountered an error.

## See Also

- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:).md)
  Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/next())*