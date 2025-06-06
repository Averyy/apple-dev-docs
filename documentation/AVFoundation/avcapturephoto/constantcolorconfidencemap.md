# constantColorConfidenceMap

**Framework**: AVFoundation  
**Kind**: property

A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var constantColorConfidenceMap: CVPixelBuffer? { get }
```

#### Discussion

A value of `255` means full confidence and `0` means zero confidence.

This property provides a valid value only for constant color photos. The value is `nil` in all other cases.

## See Also

- [var constantColorCenterWeightedMeanConfidenceLevel: Float](avcapturephoto/constantcolorcenterweightedmeanconfidencelevel.md)
  A score that summarizes the overall confidence level of a constant color photo.
- [var isConstantColorFallbackPhoto: Bool](avcapturephoto/isconstantcolorfallbackphoto.md)
  A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/constantcolorconfidencemap)*