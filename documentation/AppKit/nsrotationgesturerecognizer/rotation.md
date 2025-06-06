# rotation

**Framework**: AppKit  
**Kind**: property

The rotation of the gesture in radians.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var rotation: CGFloat { get set }
```

#### Discussion

This property contains the current rotation in effect for the gesture. Changing the value in this property also updates the value in the [`rotationInDegrees`](nsrotationgesturerecognizer/rotationindegrees.md) property.

## See Also

- [var rotationInDegrees: CGFloat](nsrotationgesturerecognizer/rotationindegrees.md)
  The rotation of the gesture in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer/rotation)*