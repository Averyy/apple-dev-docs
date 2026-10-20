# rotationRate

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The rotation rate of the controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rotationRate: GCRotationRate { get }
```

```objc
@property (nonatomic, readonly) GCRotationRate rotationRate;
```

#### Discussion

The *rotation rate* is a gyroscopic measurement of the controller’s rotation around the x, y, and z axes.

## See Also

### Accessing Attitude and Rotation Data
- [var attitude: GCQuaternion](./attitude.md)
  The attitude of the controller.
- [struct GCQuaternion](../gcquaternion.md)
  A quaternion that represents a controller’s measurement of attitude.
- [struct GCRotationRate](../gcrotationrate.md)
  A structure that represents rotation rates around the x, y, and z axes.
- [struct GCEulerAngles](../gceulerangles.md)
  A structure that specifies the controller’s attitude as a series of rotations around the x, y, and z axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/rotationrate)*