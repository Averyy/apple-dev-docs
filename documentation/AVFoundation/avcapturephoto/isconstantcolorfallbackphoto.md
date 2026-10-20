# isConstantColorFallbackPhoto

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isConstantColorFallbackPhoto: Bool { get }
```

```objc
@property (readonly, getter=isConstantColorFallbackPhoto) BOOL constantColorFallbackPhoto;
```

## See Also

### Enabling constant color
- [var constantColorCenterWeightedMeanConfidenceLevel: Float](./constantcolorcenterweightedmeanconfidencelevel.md)
  A score that summarizes the overall confidence level of a constant color photo.
- [var constantColorConfidenceMap: CVPixelBuffer?](./constantcolorconfidencemap.md)
  A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/isconstantcolorfallbackphoto)*