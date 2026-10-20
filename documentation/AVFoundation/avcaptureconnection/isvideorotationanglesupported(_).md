# isVideoRotationAngleSupported(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the connection supports a rotation angle.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func isVideoRotationAngleSupported(_ videoRotationAngle: CGFloat) -> Bool
```

```objc
- (BOOL) isVideoRotationAngleSupported:(CGFloat) videoRotationAngle;
```

## Parameters

- `videoRotationAngle`: A rotation angle in degrees.

## See Also

### Rotating a video
- [var videoRotationAngle: CGFloat](./videorotationangle.md)
  A rotation angle the connection applies to the video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideorotationanglesupported(_:))*