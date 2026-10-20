# AVAssetReaderOutput.Provider

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that reads a collection of samples of a common media type from an asset reader.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class Provider<Payload> where Payload : AVAssetReaderOutput.SupportedPayload
```

## Topics

### Reading media data
- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](./provider/captionsnotpresentinpreviousgroups%28in%29.md)
  Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().
- [func next() async throws -> Payload?](./provider/next%28%29.md)
  Returns the next piece of media data.

## See Also

### Copying sample buffers
- [func copyNextSampleBuffer() -> CMSampleBuffer?](./copynextsamplebuffer%28%29.md)
  Copies the next sample buffer from the output.
- [AVAssetReaderOutput.RandomAccessController](./randomaccesscontroller.md)
  Object used to reset an output provider to read specified time ranges.
- [AVAssetReaderOutput.SupportedPayload](./supportedpayload.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider)*