# highlight

**Framework**: SwiftUI  
**Kind**: property

A hover effect that highlights views using a light source to indicate position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static var highlight: HighlightHoverEffect { get }
```

#### Discussion

For pointer input this effect morphs the pointer into a platter behind the view and shows a light source indicating position.

On tvOS it applies a projection effect accompanied with a specular highlight on the view when contained within a focused view. It also incorporates motion effects to produce a parallax effect by adjusting the projection matrix and specular offset.

On visionOS this effect applies a glow effect based on where the user is looking or touching the view.

## See Also

- [static var automatic: AutomaticHoverEffect](customhovereffect/automatic.md)
  The default hover effect based on the surrounding context.
- [static var empty: EmptyHoverEffect](customhovereffect/empty.md)
  An effect that applies no changes when hovered.
- [static var lift: LiftHoverEffect](customhovereffect/lift.md)
  A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/highlight)*