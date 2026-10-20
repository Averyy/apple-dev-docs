# quaternion

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

Returns a quaternion representing the device’s attitude.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var quaternion: CMQuaternion { get }
```

```objc
@property (nonatomic, readonly) CMQuaternion quaternion;
```

#### Discussion

See the discussion of the [`CMQuaternion`](../cmquaternion.md) type in “Constants” for further information.

## See Also

### Related Documentation
- [var rotationMatrix: CMRotationMatrix](./rotationmatrix.md)
  Returns a rotation matrix representing the device’s attitude.
### Getting a Mathematical Representation of Attitude as a Quaternion
- [struct CMQuaternion](../cmquaternion.md)
  The type for a quaternion representing a measurement of attitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitude/quaternion)*