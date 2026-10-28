# maximumRelativeValue

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The value that maps to the maximum viewer offset.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var maximumRelativeValue: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id maximumRelativeValue;
```

## Discussion

The value in this property is the value returned when the viewer offset value along the given axis is 1.

## See Also

### Accessing the motion attributes
- [var keyPath: String](./keypath.md)
  The key path you want to modify on the view.
- [var type: UIInterpolatingMotionEffect.EffectType](./type.md)
  The tilt direction to monitor.
- [var minimumRelativeValue: Any?](./minimumrelativevalue.md)
  The value that maps to the minimum viewer offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/maximumrelativevalue)*