# setTargetOffsetFromCenter(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setTargetOffsetFromCenter(_ o: UIOffset, for item: any UIDynamicItem)
```

#### Discussion

If you don’t set a target offset for a dynamic item, a push behavior’s force vector is applied at the item center.

## Parameters

- `o`: The offset, from the center of the dynamic item, at which to apply the push behavior’s force vector.
- `item`: The dynamic item for which you’re setting a target offset.

## See Also

- [func setAngle(CGFloat, magnitude: CGFloat)](uipushbehavior/setangle(_:magnitude:).md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](uipushbehavior/angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](uipushbehavior/magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](uipushbehavior/mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](uipushbehavior/targetoffsetfromcenter(for:).md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](uipushbehavior/pushdirection.md)
  The direction of the force vector for the behavior, expressed as  and  components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/settargetoffsetfromcenter(_:for:))*