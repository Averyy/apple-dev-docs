# AVAssetReaderOutput.Provider

**Framework**: AVFoundation  
**Kind**: class

An object that reads a collection of samples of a common media type from an asset reader.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class Provider<Payload> where Payload : AVAssetReaderOutput.SupportedPayload
```

## Topics

### Reading media data
- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:).md)
  Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().
- [func next() async throws -> Payload?](avassetreaderoutput/provider/next.md)
  Retruns the next piece of media data.

## See Also

- [func copyNextSampleBuffer() -> CMSampleBuffer?](avassetreaderoutput/copynextsamplebuffer.md)
  Copies the next sample buffer from the output.
- [AVAssetReaderOutput.RandomAccessController](avassetreaderoutput/randomaccesscontroller.md)
  Object used to reset an output provider to read specified time ranges.
- [AVAssetReaderOutput.SupportedPayload](avassetreaderoutput/supportedpayload.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider)*