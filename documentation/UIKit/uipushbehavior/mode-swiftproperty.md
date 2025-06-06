# mode

**Framework**: UIKit  
**Kind**: property

Returns the force mode for the push behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var mode: UIPushBehavior.Mode { get }
```

#### Discussion

The mode is one of the values available in the [`UIPushBehavior.Mode`](uipushbehavior/mode-swift.enum.md) enumeration. Set the mode when you call the [`init(items:mode:)`](uipushbehavior/init(items:mode:).md) method.

## See Also

- [func setAngle(CGFloat, magnitude: CGFloat)](uipushbehavior/setangle(_:magnitude:).md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](uipushbehavior/angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](uipushbehavior/magnitude.md)
  The magnitude of the force vector for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](uipushbehavior/settargetoffsetfromcenter(_:for:).md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](uipushbehavior/targetoffsetfromcenter(for:).md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](uipushbehavior/pushdirection.md)
  The direction of the force vector for the behavior, expressed as  and  components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/mode-swift.property)*