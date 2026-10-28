# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default hover effect based on the surrounding context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
static var automatic: AutomaticHoverEffect { get }
```

Available when `Self` is `AutomaticHoverEffect`.

## Discussion

The automatic effect will resolve to any [`defaultHoverEffect(_:)`](../view/defaulthovereffect%28_%29.md) applied to the current View hierarchy, or a system-defined effect if no default effect has been defined.

## See Also

### Getting built-in hover effects
- [static var empty: EmptyHoverEffect](./empty.md)
  An effect that applies no changes when hovered.
- [static var highlight: HighlightHoverEffect](./highlight.md)
  A hover effect that highlights views using a light source to indicate position.
- [static var lift: LiftHoverEffect](./lift.md)
  A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customhovereffect/automatic)*