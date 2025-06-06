# dimensions(in:)

**Framework**: SwiftUI  
**Kind**: method

Asks the subview for its dimensions and alignment guides.

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
func dimensions(in proposal: ProposedViewSize) -> ViewDimensions
```

#### Return Value

A [`ViewDimensions`](viewdimensions.md) instance that includes a height and width, as well as a set of alignment guides.

#### Discussion

Call this method to ask a subview of a custom [`Layout`](layout.md) type about its size and alignment properties. You can call it from your implementation of any of that protocol’s methods, like [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) or [`sizeThatFits(proposal:subviews:cache:)`](layout/sizethatfits(proposal:subviews:cache:).md), to get information for your layout calculations.

When you call this method, you propose a size using the `proposal` parameter. The subview can choose its own size, but might take the proposal into account. You can call this method more than once with different proposals to find out if the view is flexible. For example, you can propose:

- [`zero`](proposedviewsize/zero.md) to get the subview’s minimum size.
- [`infinity`](proposedviewsize/infinity.md) to get the subview’s maximum size.
- [`unspecified`](proposedviewsize/unspecified.md) to get the subview’s ideal size.

If you need only the view’s height and width, you can use the [`sizeThatFits(_:)`](layoutsubview/sizethatfits(_:).md) method instead.

## Parameters

- `proposal`: A proposed size for the subview. In SwiftUI,   views choose their own size, but can take a size proposal from   their parent view into account when doing so.

## See Also

- [func sizeThatFits(ProposedViewSize) -> CGSize](layoutsubview/sizethatfits(_:).md)
  Asks the subview for its size.
- [var spacing: ViewSpacing](layoutsubview/spacing.md)
  The subviews’s preferred spacing values.
- [var priority: Double](layoutsubview/priority.md)
  The layout priority of the subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubview/dimensions(in:))*