# init(keyPath:type:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns an interpolating motion effect object configured for the specific tilt direction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(keyPath: String, type: UIInterpolatingMotionEffect.EffectType)
```

#### Return Value

An initialized interpolating motion effect object.

## Parameters

- `keyPath`: The key path of the view that you want to modify. This path must correspond to an animatable property of the view on which this motion effect is applied. For example, to update the   property of the view, specify the string “center”.
- `type`: The type of motion to track. You can track horizontal or vertical tilt. For a list of possible values, see  .

## See Also

- [init?(coder: NSCoder)](uiinterpolatingmotioneffect/init(coder:).md)
  Creates a motion effect from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/init(keypath:type:))*