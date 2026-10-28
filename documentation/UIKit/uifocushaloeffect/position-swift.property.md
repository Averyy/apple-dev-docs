# position

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The position of the halo effect relative to its shape.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var position: UIFocusHaloEffect.Position { get set }
```

```objc
@property (nonatomic) UIFocusHaloEffectPosition position;
```

## Discussion

The default value of this property is [`UIFocusHaloEffect.Position.automatic`](./position-swift.enum/automatic.md).

## See Also

### Configuring a halo effect
- [var containerView: UIView?](./containerview.md)
  The container view to place the halo effect into.
- [var referenceView: UIView?](./referenceview.md)
  The view to place the halo effect above.
- [UIFocusHaloEffect.Position](./position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocushaloeffect/position-swift.property)*