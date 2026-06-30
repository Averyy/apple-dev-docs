# copyNextSampleBuffer()

**Framework**: AVFoundation  
**Kind**: method

Copies the next sample buffer from the output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func copyNextSampleBuffer() -> CMSampleBuffer?
```

#### Return Value

The output sample buffer, or `nil` if you’ve read all samples or an error occurs.

#### Discussion

This method returns `nil` when you’ve read all available sample buffers, or if there’s an error. Check the value of the asset reader’s [`status`](avassetreader/status-swift.property.md) property to determine the reason.

The order of returned sample buffers depends on the output’s configuration. For a track output with a `nil` [`outputSettings`](avassetreadertrackoutput/outputsettings.md) dictionary, the output skips decoding and returns sample buffers in decode order. Preserve that order when working with the encoded samples directly, such as when passing them to [`AVAssetWriter`](avassetwriter.md). When the output decodes the samples, it returns them in presentation order. Playback and downstream processing operate in presentation order, so decode order no longer matters after decoding.

## See Also

- [AVAssetReaderOutput.Provider](avassetreaderoutput/provider.md)
  An object that reads a collection of samples of a common media type from an asset reader.
- [AVAssetReaderOutput.RandomAccessController](avassetreaderoutput/randomaccesscontroller.md)
  Object used to reset an output provider to read specified time ranges.
- [AVAssetReaderOutput.SupportedPayload](avassetreaderoutput/supportedpayload.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/copynextsamplebuffer())*