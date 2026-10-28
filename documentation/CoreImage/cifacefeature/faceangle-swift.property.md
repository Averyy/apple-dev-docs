# faceAngle

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The rotation of the face.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var faceAngle: Float { get }
```

```objc
@property (assign, readonly) float faceAngle;
```

## Discussion

Rotation is measured counterclockwise in degrees, with zero indicating that a line drawn between the eyes is horizontal relative to the image orientation.

## See Also

### Locating Faces
- [var bounds: CGRect](./bounds-swift.property.md)
  A rectangle indicating the position and extent of the face feature in image coordinates.
- [var hasFaceAngle: Bool](./hasfaceangle-swift.property.md)
  A Boolean value that indicates whether information about face rotation is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/faceangle-swift.property)*