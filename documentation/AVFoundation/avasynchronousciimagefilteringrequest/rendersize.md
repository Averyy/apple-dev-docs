# renderSize

**Framework**: AVFoundation  
**Kind**: property

The width and height, in pixels, of the frame being processed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderSize: CGSize { get }
```

#### Discussion

You can use this property if you need to work with Core Image filters that apply transforms to the image.

## See Also

- [var compositionTime: CMTime](avasynchronousciimagefilteringrequest/compositiontime.md)
  The time in the video composition corresponding to the frame being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/rendersize)*