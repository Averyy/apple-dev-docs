# mode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the force mode for the push behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var mode: UIPushBehavior.Mode { get }
```

```objc
@property (nonatomic, readonly) UIPushBehaviorMode mode;
```

## Discussion

The mode is one of the values available in the [`UIPushBehavior.Mode`](./mode-swift.enum.md) enumeration. Set the mode when you call the [`init(items:mode:)`](./init%28items,mode%29.md) method.

## See Also

### Configuring a push behavior
- [func setAngle(CGFloat, magnitude: CGFloat)](./setangle%28_,magnitude%29.md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](./angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](./magnitude.md)
  The magnitude of the force vector for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](./settargetoffsetfromcenter%28_,for%29.md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](./targetoffsetfromcenter%28for%29.md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](./pushdirection.md)
  The direction of the force vector for the behavior, expressed as *x* and *y* components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/mode-swift.property)*