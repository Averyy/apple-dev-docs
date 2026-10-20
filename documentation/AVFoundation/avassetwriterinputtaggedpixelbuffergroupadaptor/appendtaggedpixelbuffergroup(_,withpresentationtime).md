# appendTaggedPixelBufferGroup(_:withPresentationTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a tagged buffer group to the adaptor.

**Availability**:
- iOS 17.0+ - Deprecated in 27.0
- iPadOS 17.0+ - Deprecated in 27.0
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

## Declaration

```swift
func appendTaggedPixelBufferGroup(_ taggedPixelBufferGroup: __CMTaggedBufferGroup, withPresentationTime presentationTime: CMTime) -> Bool
```

```objc
- (BOOL) appendTaggedPixelBufferGroup:(CMTaggedBufferGroupRef) taggedPixelBufferGroup withPresentationTime:(CMTime) presentationTime;
```

## See Also

### Appending pixel buffers
- [func appendTaggedBuffers([CMTaggedBuffer], withPresentationTime: CMTime) -> Bool](./appendtaggedbuffers%28_,withpresentationtime%29.md)
  Appends a tagged buffer group to the adaptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedpixelbuffergroup(_:withpresentationtime:))*