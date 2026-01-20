# leftEyeClosed

**Framework**: Core Image  
**Kind**: property

A Boolean value that indicates whether a closed left eye is detected in the face.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var leftEyeClosed: Bool { get }
```

#### Discussion

To detect closed eyes, `/CIDetector/featuresInImage:options:` needs to be called with the [`CIDetectorEyeBlink`](cidetectoreyeblink.md) option set to true.

## See Also

- [var hasLeftEyePosition: Bool](cifacefeature/haslefteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s left eye.
- [var hasRightEyePosition: Bool](cifacefeature/hasrighteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](cifacefeature/hasmouthposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var leftEyePosition: CGPoint](cifacefeature/lefteyeposition-swift.property.md)
  The image coordinate of the center of the left eye.
- [var rightEyePosition: CGPoint](cifacefeature/righteyeposition-swift.property.md)
  The image coordinate of the center of the right eye.
- [var mouthPosition: CGPoint](cifacefeature/mouthposition-swift.property.md)
  The image coordinate of the center of the mouth.
- [var hasSmile: Bool](cifacefeature/hassmile-swift.property.md)
  A Boolean value that indicates whether a smile is detected in the face.
- [var rightEyeClosed: Bool](cifacefeature/righteyeclosed-swift.property.md)
  A Boolean value that indicates whether a closed right eye is detected in the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/lefteyeclosed-swift.property)*