# hasLeftEyePosition

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the detector found the face’s left eye.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var hasLeftEyePosition: Bool { get }
```

```objc
@property (assign, readonly) BOOL hasLeftEyePosition;
```

## See Also

### Identifying Facial Features
- [var hasRightEyePosition: Bool](./hasrighteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](./hasmouthposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var leftEyePosition: CGPoint](./lefteyeposition-swift.property.md)
  The image coordinate of the center of the left eye.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/haslefteyeposition-swift.property)*