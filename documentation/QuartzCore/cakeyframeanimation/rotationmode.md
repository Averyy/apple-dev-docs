# rotationMode

**Framework**: Core Animation  
**Kind**: property

Determines whether objects animating along the path rotate to match the path tangent.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rotationMode: CAAnimationRotationMode? { get set }
```

#### Discussion

The possible values for this property are described in [`Rotation Mode Values`](rotation-mode-values.md). The default value of this property is `nil`, which indicates that objects should not rotate to follow the path.

The effect of setting this property to a non-`nil` value when no path object is supplied is undefined.

## See Also

- [var path: CGPath?](cakeyframeanimation/path.md)
  The path for a point-based property to follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/rotationmode)*