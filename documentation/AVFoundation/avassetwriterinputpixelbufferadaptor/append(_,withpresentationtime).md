# append(_:withPresentationTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a pixel buffer to the adaptor.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

## Declaration

```swift
func append(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool
```

```objc
- (BOOL) appendPixelBuffer:(CVPixelBufferRef) pixelBuffer withPresentationTime:(CMTime) presentationTime;
```

#### Return Value

[`true`](../../Swift/true.md) if the adaptor appends the pixel buffer; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `pixelBuffer`: The pixel buffer to append.
- `presentationTime`: The pixel buffer’s presentation time. The time you specify is relative to the time you called [`startSession(atSourceTime:)`](../avassetwriter/startsession%28atsourcetime%29.md) with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:))*