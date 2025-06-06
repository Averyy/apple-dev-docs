# compositionTime

**Framework**: AVFoundation  
**Kind**: property

The time in the video composition corresponding to the frame being processed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var compositionTime: CMTime { get }
```

#### Discussion

You can use this property to vary the parameters of a filter over time.

## See Also

- [var renderSize: CGSize](avasynchronousciimagefilteringrequest/rendersize.md)
  The width and height, in pixels, of the frame being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/compositiontime)*