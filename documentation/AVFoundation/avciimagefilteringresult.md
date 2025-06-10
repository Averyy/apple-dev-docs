# AVCIImageFilteringResult

**Framework**: AVFoundation  
**Kind**: struct

An output video frame processed with Core Image filtering.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AVCIImageFilteringResult
```

## Topics

### Initializers
- [init(resultImage: CIImage, ciContext: CIContext?)](avciimagefilteringresult/init(resultimage:cicontext:).md)
### Instance Properties
- [let ciContext: CIContext?](avciimagefilteringresult/cicontext.md)
  The core image context used to render the image
- [let resultImage: CIImage](avciimagefilteringresult/resultimage.md)
  Provides the filtered video frame image to AVFoundation for further processing or display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avciimagefilteringresult)*