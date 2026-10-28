# rotationMatrix

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

Returns a rotation matrix representing the device’s attitude.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rotationMatrix: CMRotationMatrix { get }
```

```objc
@property (nonatomic, readonly) CMRotationMatrix rotationMatrix;
```

## Discussion

A rotation matrix in linear algebra describes the rotation of a body in three-dimensional Euclidean space.

## See Also

### Related Documentation
- [var quaternion: CMQuaternion](./quaternion.md)
  Returns a quaternion representing the device’s attitude.
### Getting a Mathematical Representation of Attitude as a Rotation Matrix
- [struct CMRotationMatrix](../cmrotationmatrix.md)
  The type of a structure representing a rotation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitude/rotationmatrix)*