# setAngle(_:magnitude:)

**Framework**: UIKit  
**Kind**: method

Sets the angle and magnitude of the force vector for the behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setAngle(_ angle: CGFloat, magnitude: CGFloat)
```

#### Discussion

Whether you express a push behavior’s force direction in terms of radian angle or with ,  components, the alternate, equivalent values update automatically.

## Parameters

- `angle`: The default angle is   radians, using standard UIKit geometry.
- `magnitude`: Setting the   parameter to a negative value reverses the direction of the force.

## See Also

- [var angle: CGFloat](uipushbehavior/angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](uipushbehavior/magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](uipushbehavior/mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](uipushbehavior/settargetoffsetfromcenter(_:for:).md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](uipushbehavior/targetoffsetfromcenter(for:).md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](uipushbehavior/pushdirection.md)
  The direction of the force vector for the behavior, expressed as  and  components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/setangle(_:magnitude:))*