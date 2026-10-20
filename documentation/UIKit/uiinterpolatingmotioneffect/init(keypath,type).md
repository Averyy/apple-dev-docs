# init(keyPath:type:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an interpolating motion effect object configured for the specific tilt direction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(keyPath: String, type: UIInterpolatingMotionEffect.EffectType)
```

```objc
- (instancetype) initWithKeyPath:(NSString *) keyPath type:(UIInterpolatingMotionEffectType) type;
```

#### Return Value

An initialized interpolating motion effect object.

## Parameters

- `keyPath`: The key path of the view that you want to modify. This path must correspond to an animatable property of the view on which this motion effect is applied. For example, to update the [`center`](../uiview/center.md) property of the view, specify the string “center”.
- `type`: The type of motion to track. You can track horizontal or vertical tilt. For a list of possible values, see [`UIInterpolatingMotionEffect.EffectType`](./effecttype.md).

## See Also

### Initializing a motion effect
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a motion effect from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/init(keypath:type:))*