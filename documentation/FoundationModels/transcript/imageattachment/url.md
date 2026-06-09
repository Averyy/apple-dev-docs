# url

**Framework**: Foundation Models  
**Kind**: property

The URL of the original image asset, if the attachment was created from a URL.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

This is `nil` if the attachment was created from a `CGImage`, `CIImage`, or `CVPixelBuffer`.

## See Also

- [var cgImage: CGImage](transcript/imageattachment/cgimage.md)
  The image as a `CGImage`.
- [var ciImage: CIImage](transcript/imageattachment/ciimage.md)
  The image as a `CIImage`.
- [var orientation: CGImagePropertyOrientation](transcript/imageattachment/orientation.md)
  The display orientation of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/imageattachment/url)*