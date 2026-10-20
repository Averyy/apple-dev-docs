# AVAssetReaderOutput.SupportedPayload

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol SupportedPayload
```

## Relationships

### Conforming Types
- [AVCaptionGroup](../avcaptiongroup.md)
- [AVMutableTimedMetadataGroup](../avmutabletimedmetadatagroup.md)
- [AVTimedMetadataGroup](../avtimedmetadatagroup.md)

## See Also

### Copying sample buffers
- [func copyNextSampleBuffer() -> CMSampleBuffer?](./copynextsamplebuffer%28%29.md)
  Copies the next sample buffer from the output.
- [AVAssetReaderOutput.Provider](./provider.md)
  An object that reads a collection of samples of a common media type from an asset reader.
- [AVAssetReaderOutput.RandomAccessController](./randomaccesscontroller.md)
  Object used to reset an output provider to read specified time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/supportedpayload)*