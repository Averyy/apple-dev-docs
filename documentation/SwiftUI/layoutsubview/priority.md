# priority

**Framework**: SwiftUI  
**Kind**: property

The layout priority of the subview.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var priority: Double { get }
```

#### Discussion

If you define a custom layout type using the [`Layout`](layout.md) protocol, you can read this value from subviews and use the value when deciding how to assign space to subviews. For example, you can read all of the subview priorities into an array before placing the subviews in a custom layout type called `BasicVStack`:

```swift
extension BasicVStack {
    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) {
        let priorities = subviews.map { subview in
            subview.priority
        }

        // Place views, based on priorities.
    }
}
```

Set the layout priority for a view that appears in your layout by applying the [`layoutPriority(_:)`](view/layoutpriority(_:).md) view modifier. For example, you can assign two different priorities to views that you arrange with `BasicVStack`:

```swift
BasicVStack {
    Text("High priority")
        .layoutPriority(10)
    Text("Low priority")
        .layoutPriority(1)
}
```

## See Also

- [func dimensions(in: ProposedViewSize) -> ViewDimensions](layoutsubview/dimensions(in:).md)
  Asks the subview for its dimensions and alignment guides.
- [func sizeThatFits(ProposedViewSize) -> CGSize](layoutsubview/sizethatfits(_:).md)
  Asks the subview for its size.
- [var spacing: ViewSpacing](layoutsubview/spacing.md)
  The subviews’s preferred spacing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubview/priority)*