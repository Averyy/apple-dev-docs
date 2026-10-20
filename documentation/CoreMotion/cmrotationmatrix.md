# CMRotationMatrix

**Framework**: Core Motion  
**Kind**: struct  
**Role**: Structure

The type of a structure representing a rotation matrix.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMRotationMatrix
```

```c
typedef struct { ... } CMRotationMatrix;
```

## Topics

### Fields
- [var m11: Double](./cmrotationmatrix/m11.md)
- [var m12: Double](./cmrotationmatrix/m12.md)
- [var m13: Double](./cmrotationmatrix/m13.md)
- [var m21: Double](./cmrotationmatrix/m21.md)
- [var m22: Double](./cmrotationmatrix/m22.md)
- [var m23: Double](./cmrotationmatrix/m23.md)
- [var m31: Double](./cmrotationmatrix/m31.md)
- [var m32: Double](./cmrotationmatrix/m32.md)
- [var m33: Double](./cmrotationmatrix/m33.md)
### Initializers
- [init()](./cmrotationmatrix/init%28%29.md)
- [init(m11: Double, m12: Double, m13: Double, m21: Double, m22: Double, m23: Double, m31: Double, m32: Double, m33: Double)](./cmrotationmatrix/init%28m11,m12,m13,m21,m22,m23,m31,m32,m33%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Getting a Mathematical Representation of Attitude as a Rotation Matrix
- [var rotationMatrix: CMRotationMatrix](./cmattitude/rotationmatrix.md)
  Returns a rotation matrix representing the device’s attitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrotationmatrix)*