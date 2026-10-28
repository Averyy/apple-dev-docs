# leftEyePosition

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The image coordinate of the center of the left eye.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var leftEyePosition: CGPoint { get }
```

```objc
@property (assign, readonly) CGPoint leftEyePosition;
```

## Discussion

> **Note**: The left eye is on the left side of the face from the observer’s perspective. It is not the left eye from the subject’s perspective.

## See Also

### Identifying Facial Features
- [var hasLeftEyePosition: Bool](./haslefteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s left eye.
- [var hasRightEyePosition: Bool](./hasrighteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](./hasmouthposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var rightEyePosition: CGPoint](./righteyeposition-swift.property.md)
  The image coordinate of the center of the right eye.
- [var mouthPosition: CGPoint](./mouthposition-swift.property.md)
  The image coordinate of the center of the mouth.
- [var hasSmile: Bool](./hassmile-swift.property.md)
  A Boolean value that indicates whether a smile is detected in the face.
- [var leftEyeClosed: Bool](./lefteyeclosed-swift.property.md)
  A Boolean value that indicates whether a closed left eye is detected in the face.
- [var rightEyeClosed: Bool](./righteyeclosed-swift.property.md)
  A Boolean value that indicates whether a closed right eye is detected in the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/lefteyeposition-swift.property)*