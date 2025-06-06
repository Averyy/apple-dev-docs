# automatic

**Framework**: SwiftUI  
**Kind**: property

The default hover effect based on the surrounding context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static var automatic: AutomaticHoverEffect { get }
```

#### Discussion

The automatic effect will resolve to any [`defaultHoverEffect(_:)`](view/defaulthovereffect(_:).md) applied to the current View hierarchy, or a system-defined effect if no default effect has been defined.

## See Also

- [static var empty: EmptyHoverEffect](customhovereffect/empty.md)
  An effect that applies no changes when hovered.
- [static var highlight: HighlightHoverEffect](customhovereffect/highlight.md)
  A hover effect that highlights views using a light source to indicate position.
- [static var lift: LiftHoverEffect](customhovereffect/lift.md)
  A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/automatic)*