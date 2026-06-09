# removeClipBufferingOutput(_:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func removeClipBufferingOutput(_ clipBufferingOutput: SCClipBufferingOutput) throws
```

#### Discussion

Remove SCClipBufferingOutput from the SCStream to stop clip buffering and flush the buffer

Returns a BOOL denoting if the remove was successful. This method stops the accumulation of samples and releases all buffered content. Once removed, no new exports can be requested until clip buffering is added again. If the stream is stopped while clip buffering is active, clip buffering will be automatically stopped as well.

## Parameters

- `clipBufferingOutput`: A SCClipBufferingOutput object


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/removeclipbufferingoutput(_:))*