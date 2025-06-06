# transform

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The rotation of the dynamic item.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var transform: CGAffineTransform { get set }
```

#### Discussion

UIKit Dynamics makes use only of the rotation value in this property.

The dynamic animator (that the item is associated with) calls this method when it has computed a new rotation value for the item.

## See Also

- [var bounds: CGRect](uidynamicitem/bounds.md)
  Called when a dynamic animator needs the bounds of the dynamic item.
- [var center: CGPoint](uidynamicitem/center.md)
  The center point of the dynamic item.
- [var collisionBoundsType: UIDynamicItemCollisionBoundsType](uidynamicitem/collisionboundstype.md)
  The type of collision bounds associated with the item.
- [var collisionBoundingPath: UIBezierPath](uidynamicitem/collisionboundingpath.md)
  The path-based shape to use for the collision bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicitem/transform)*