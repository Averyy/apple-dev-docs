# finish()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finish()
```

## See Also

### Appending samples
- [func append(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws](./append%28_%29.md)
  Suspends until the input is ready for more media data, then appends the sample buffer.
- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](./appendimmediately%28_%29.md)
  Appends the sample buffer synchronously if the input is ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/finish())*