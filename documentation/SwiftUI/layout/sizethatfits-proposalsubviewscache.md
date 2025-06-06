# sizeThatFits(proposal:subviews:cache:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Returns the size of the composite view, given a proposed size and the view’s subviews.

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
func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGSize
```

#### Return Value

A size that indicates how much space the container needs to arrange its subviews.

#### Discussion

Implement this method to tell your custom layout container’s parent view how much space the container needs for a set of subviews, given a size proposal. The parent might call this method more than once during a layout pass with different proposed sizes to test the flexibility of the container, using proposals like:

- The [`zero`](proposedviewsize/zero.md) proposal; respond with the layout’s minimum size.
- The [`infinity`](proposedviewsize/infinity.md) proposal; respond with the layout’s maximum size.
- The [`unspecified`](proposedviewsize/unspecified.md) proposal; respond with the layout’s ideal size.

The parent might also choose to test flexibility in one dimension at a time. For example, a horizontal stack might propose a fixed height and an infinite width, and then the same height with a zero width.

The following example calculates the size for a basic vertical stack that places views in a column, with no spacing between the views:

```swift
private struct BasicVStack: Layout {
    func sizeThatFits(
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) -> CGSize {
        subviews.reduce(CGSize.zero) { result, subview in
            let size = subview.sizeThatFits(.unspecified)
            return CGSize(
                width: max(result.width, size.width),
                height: result.height + size.height)
        }
    }

    // This layout also needs a placeSubviews() implementation.
}
```

The implementation asks each subview for its ideal size by calling the [`sizeThatFits(_:)`](layoutsubview/sizethatfits(_:).md) method with an [`unspecified`](proposedviewsize/unspecified.md) proposed size. It then reduces these values into a single size that represents the maximum subview width and the sum of subview heights. Because this example isn’t flexible, it ignores its size proposal input and always returns the same value for a given set of subviews.

SwiftUI views choose their own size, so the layout engine always uses a value that you return from this method as the actual size of the composite view. That size factors into the construction of the `bounds` input to the [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) method.

## Parameters

- `proposal`: A size proposal for the container. The container’s parent   view that calls this method might call the method more than once   with different proposals to learn more about the container’s   flexibility before deciding which proposal to use for placement.
- `subviews`: A collection of proxies that represent the   views that the container arranges. You can use the proxies in the   collection to get information about the subviews as you determine   how much space the container needs to display them.
- `cache`: Optional storage for calculated data that you can share among   the methods of your custom layout container. See    for details.

## See Also

- [func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache)](layout/placesubviews(in:proposal:subviews:cache:).md)
  Assigns positions to each of the layout’s subviews.
- [typealias Subviews](layout/subviews.md)
  A collection of proxies for the subviews of a layout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/sizethatfits(proposal:subviews:cache:))*