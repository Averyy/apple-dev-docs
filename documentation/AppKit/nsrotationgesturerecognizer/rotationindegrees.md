# rotationInDegrees

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rotation of the gesture in degrees.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var rotationInDegrees: CGFloat { get set }
```

```objc
@property CGFloat rotationInDegrees;
```

#### Discussion

This property contains the current rotation in effect for the gesture. Changing the value in this property also updates the value in the [`rotation`](./rotation.md) property.

## See Also

### Interpreting the gesture
- [var rotation: CGFloat](./rotation.md)
  The rotation of the gesture in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrotationgesturerecognizer/rotationindegrees)*