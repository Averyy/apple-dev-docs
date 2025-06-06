# placeSubviews(in:proposal:subviews:cache:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Assigns positions to each of the layout’s subviews.

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
func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache)
```

#### Discussion

SwiftUI calls your implementation of this method to tell your custom layout container to place its subviews. From this method, call the [`place(at:anchor:proposal:)`](layoutsubview/place(at:anchor:proposal:).md) method on each element in `subviews` to tell the subviews where to appear in the user interface.

For example, you can create a basic vertical stack that places views in a column, with views horizontally aligned on their leading edge:

```swift
struct BasicVStack: Layout {
    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) {
        var point = bounds.origin
        for subview in subviews {
            subview.place(at: point, anchor: .topLeading, proposal: .unspecified)
            point.y += subview.dimensions(in: .unspecified).height
        }
    }

    // This layout also needs a sizeThatFits() implementation.
}
```

The example creates a placement point that starts at the origin of the specified `bounds` input and uses that to place the first subview. It then moves the point in the y dimension by the subview’s height, which it reads using the [`dimensions(in:)`](layoutsubview/dimensions(in:).md) method. This prepares the point for the next iteration of the loop. All subview operations use an [`unspecified`](proposedviewsize/unspecified.md) size proposal to indicate that subviews should use and report their ideal size.

A more complex layout container might add space between subviews according to their [`spacing`](layoutsubview/spacing.md) preferences, or a fixed space based on input configuration. For example, you can extend the basic vertical stack’s placement method to calculate the preferred distances between adjacent subviews and store the results in an array:

```swift
let spacing: [CGFloat] = subviews.indices.dropLast().map { index in
    subviews[index].spacing.distance(
        to: subviews[index + 1].spacing,
        along: .vertical)
}
```

The spacing’s [`distance(to:along:)`](viewspacing/distance(to:along:).md) method considers the preferences of adjacent views on the edge where they meet. It returns the smallest distance that satisfies both views’ preferences for the given edge. For example, if one view prefers at least `2` points on its bottom edge, and the next view prefers at least `8` points on its top edge, the distance method returns `8`, because that’s the smallest value that satisfies both preferences.

Update the placement calculations to use the spacing values:

```swift
var point = bounds.origin
for (index, subview) in subviews.enumerated() {
    if index > 0 { point.y += spacing[index - 1] } // Add spacing.
    subview.place(at: point, anchor: .topLeading, proposal: .unspecified)
    point.y += subview.dimensions(in: .unspecified).height
}
```

Be sure that you use computations during placement that are consistent with those in your implementation of other protocol methods for a given set of inputs. For example, if you add spacing during placement, make sure your implementation of [`sizeThatFits(proposal:subviews:cache:)`](layout/sizethatfits(proposal:subviews:cache:).md) accounts for the extra space. Similarly, if the sizing method returns different values for different size proposals, make sure the placement method responds to its `proposal` input in the same way.

## Parameters

- `bounds`: The region that the container view’s parent allocates to the   container view, specified in the parent’s coordinate space.   Place all the container’s subviews within the region.   The size of this region matches a size that your container   previously returned from a call to the    method.
- `proposal`: The size proposal from which the container generated the   size that the parent used to create the   parameter.   The parent might propose more than one size before calling the   placement method, but it always uses one of the proposals and the   corresponding returned size when placing the container.
- `subviews`: A collection of proxies that represent the   views that the container arranges. Use the proxies in the collection   to get information about the subviews and to tell the subviews   where to appear.
- `cache`: Optional storage for calculated data that you can share among   the methods of your custom layout container. See    for details.

## See Also

- [func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGSize](layout/sizethatfits(proposal:subviews:cache:).md)
  Returns the size of the composite view, given a proposed size and the view’s subviews.
- [typealias Subviews](layout/subviews.md)
  A collection of proxies for the subviews of a layout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/placesubviews(in:proposal:subviews:cache:))*