# setTargetOffsetFromCenter(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTargetOffsetFromCenter(_ o: UIOffset, for item: any UIDynamicItem)
```

```objc
- (void) setTargetOffsetFromCenter:(UIOffset) o forItem:(id<UIDynamicItem>) item;
```

## Discussion

If you don’t set a target offset for a dynamic item, a push behavior’s force vector is applied at the item center.

## Parameters

- `o`: The offset, from the center of the dynamic item, at which to apply the push behavior’s force vector.
- `item`: The dynamic item for which you’re setting a target offset.

## See Also

### Configuring a push behavior
- [func setAngle(CGFloat, magnitude: CGFloat)](./setangle%28_,magnitude%29.md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](./angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](./magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](./mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](./targetoffsetfromcenter%28for%29.md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](./pushdirection.md)
  The direction of the force vector for the behavior, expressed as *x* and *y* components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/settargetoffsetfromcenter(_:for:))*