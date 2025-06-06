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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/copynextsamplebuffer())*