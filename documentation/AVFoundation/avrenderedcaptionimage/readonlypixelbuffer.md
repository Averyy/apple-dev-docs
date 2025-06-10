# readOnlyPixelBuffer

**Framework**: AVFoundation  
**Kind**: property

A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
var readOnlyPixelBuffer: CVReadOnlyPixelBuffer { get }
```

#### Discussion

The pixel format is fixed to `kCVPixelFormatType_32BGRA` defined in <CoreVideo/CVPixelBuffer.h>


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage/readonlypixelbuffer)*