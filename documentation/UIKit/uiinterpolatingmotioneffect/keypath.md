# keyPath

**Framework**: UIKit  
**Kind**: property

The key path you want to modify on the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var keyPath: String { get }
```

#### Discussion

This property must correspond to an animatable property of the view to which the motion effect is attached.

## See Also

- [var type: UIInterpolatingMotionEffect.EffectType](uiinterpolatingmotioneffect/type.md)
  The tilt direction to monitor.
- [var minimumRelativeValue: Any?](uiinterpolatingmotioneffect/minimumrelativevalue.md)
  The value that maps to the minimum viewer offset.
- [var maximumRelativeValue: Any?](uiinterpolatingmotioneffect/maximumrelativevalue.md)
  The value that maps to the maximum viewer offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/keypath)*