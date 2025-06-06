# rotationInDegrees

**Framework**: AppKit  
**Kind**: property

The rotation of the gesture in degrees.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var rotationInDegrees: CGFloat { get set }
```

#### Discussion

This property contains the current rotation in effect for the gesture. Changing the value in this property also updates the value in the [`rotation`](nsrotationgesturerecognizer/rotation.md) property.

## See Also

- [var rotation: CGFloat](nsrotationgesturerecognizer/rotation.md)
  The rotation of the gesture in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer/rotationindegrees)*