# bounds

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A rectangle indicating the position and extent of the face feature in image coordinates.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get }
```

```objc
@property (assign, readonly) CGRect bounds;
```

## See Also

### Locating Faces
- [var hasFaceAngle: Bool](./hasfaceangle-swift.property.md)
  A Boolean value that indicates whether information about face rotation is available.
- [var faceAngle: Float](./faceangle-swift.property.md)
  The rotation of the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/bounds-swift.property)*