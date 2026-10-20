# angle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The angle, in radians, of the force vector for the behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var angle: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat angle;
```

#### Discussion

The default angle is `0` radians, using standard UIKit geometry. To configure the force vector for a push behavior, set the [`magnitude`](./magnitude.md) property as well as the [`angle`](./angle.md) property.

Alternatively, you can express the direction of force by using *x* and *y* components with the [`pushDirection`](./pushdirection.md) property. Whichever approach you use, the alternate, equivalent values update automatically.

## See Also

### Configuring a push behavior
- [func setAngle(CGFloat, magnitude: CGFloat)](./setangle%28_,magnitude%29.md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var magnitude: CGFloat](./magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](./mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](./settargetoffsetfromcenter%28_,for%29.md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](./targetoffsetfromcenter%28for%29.md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](./pushdirection.md)
  The direction of the force vector for the behavior, expressed as *x* and *y* components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/angle)*