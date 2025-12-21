# AVAssetReaderOutput.RandomAccessController

**Framework**: AVFoundation  
**Kind**: class

Object used to reset an output provider to read specified time ranges.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class RandomAccessController
```

## Topics

### Configuring a controller
- [func markConfigurationAsFinal()](avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal.md)
  Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.
- [func resetForReading(timeRanges: [CMTimeRange])](avassetreaderoutput/randomaccesscontroller/resetforreading(timeranges:).md)
  Starts reading over with a new set of time ranges.

## See Also

- [func copyNextSampleBuffer() -> CMSampleBuffer?](avassetreaderoutput/copynextsamplebuffer.md)
  Copies the next sample buffer from the output.
- [AVAssetReaderOutput.Provider](avassetreaderoutput/provider.md)
  An object that reads a collection of samples of a common media type from an asset reader.
- [AVAssetReaderOutput.SupportedPayload](avassetreaderoutput/supportedpayload.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller)*