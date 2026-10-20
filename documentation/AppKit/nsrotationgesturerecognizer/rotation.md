# rotation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rotation of the gesture in radians.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var rotation: CGFloat { get set }
```

```objc
@property CGFloat rotation;
```

#### Discussion

This property contains the current rotation in effect for the gesture. Changing the value in this property also updates the value in the [`rotationInDegrees`](./rotationindegrees.md) property.

## See Also

### Interpreting the gesture
- [var rotationInDegrees: CGFloat](./rotationindegrees.md)
  The rotation of the gesture in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer/rotation)*