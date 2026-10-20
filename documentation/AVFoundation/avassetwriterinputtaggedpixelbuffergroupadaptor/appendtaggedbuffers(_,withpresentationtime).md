# appendTaggedBuffers(_:withPresentationTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a tagged buffer group to the adaptor.

**Availability**:
- iOS 17.0+ - Deprecated in 26.0
- iPadOS 17.0+ - Deprecated in 26.0
- Mac Catalyst 17.0+ - Deprecated in 26.0
- macOS 14.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use AVAssetWriterInput.TaggedPixelBufferGroupReceiver.append(_:with:isolation:) instead

## Declaration

```swift
func appendTaggedBuffers(_ taggedBuffers: [CMTaggedBuffer], withPresentationTime: CMTime) -> Bool
```

## See Also

### Appending pixel buffers
- [func appendTaggedPixelBufferGroup(__CMTaggedBufferGroup, withPresentationTime: CMTime) -> Bool](./appendtaggedpixelbuffergroup%28_,withpresentationtime%29.md)
  Appends a tagged buffer group to the adaptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers(_:withpresentationtime:))*