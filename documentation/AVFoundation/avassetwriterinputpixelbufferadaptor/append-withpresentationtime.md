# append(_:withPresentationTime:)

**Framework**: AVFoundation  
**Kind**: method

Appends a pixel buffer to the adaptor.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func append(_ pixelBuffer: CVPixelBuffer, withPresentationTime presentationTime: CMTime) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the adaptor appends the pixel buffer; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `pixelBuffer`: The pixel buffer to append.
- `presentationTime`: The pixel buffer’s presentation time. The time you specify is relative to the time you called   with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:))*