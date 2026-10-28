# explicitAlignment(of:in:proposal:subviews:cache:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the position of the specified horizontal alignment guide along the x axis.

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
func explicitAlignment(of guide: HorizontalAlignment, in bounds: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGFloat?
```

**Other overloads**:

```swift
func explicitAlignment(of guide: VerticalAlignment, in bounds: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGFloat?
```

## Return Value

The guide’s position relative to the `bounds`. Return `nil` to indicate that the guide doesn’t have an explicit value.

## Discussion

Implement this method to return a value for the specified alignment guide of a custom layout container. The value you return affects the placement of the container as a whole, but it doesn’t affect how the container arranges subviews relative to one another.

You can use this method to put an alignment guide in a nonstandard position. For example, you can indent the container’s leading edge alignment guide by 10 points:

```swift
extension BasicVStack {
    func explicitAlignment(
        of guide: HorizontalAlignment,
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) -> CGFloat? {
        if guide == .leading {
            return bounds.minX + 10
        }
        return nil
    }
}
```

The above example returns `nil` for other guides to indicate that they don’t have an explicit value. A guide without an explicit value behaves as it would for any other view. If you don’t implement the method, the protocol’s default implementation merges the subviews’ guides.

## Parameters

- `guide`: The [`HorizontalAlignment`](../horizontalalignment.md) guide that the method calculates the position of.
- `bounds`: The region that the container view’s parent allocates to the container view, specified in the parent’s coordinate space.
- `proposal`: A proposed size for the container.
- `subviews`: A collection of proxy instances that represent the views arranged by the container. You can use the proxies in the collection to get information about the subviews as you determine where to place the guide.
- `cache`: Optional storage for calculated data that you can share among the methods of your custom layout container. See [`makeCache(subviews:)`](./makecache%28subviews%29.md) for details.

## Default Implementations

### Layout Implementations
- [func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGFloat?](./explicitalignment%28of,in,proposal,subviews,cache%29-755bz.md)
  Returns the result of merging the vertical alignment guides of all subviews.
- [func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGFloat?](./explicitalignment%28of,in,proposal,subviews,cache%29-8cl0p.md)
  Returns the result of merging the horizontal alignment guides of all subviews.

## See Also

### Reporting layout container characteristics
- [func spacing(subviews: Self.Subviews, cache: inout Self.Cache) -> ViewSpacing](./spacing%28subviews,cache%29.md)
  Returns the preferred spacing values of the composite view.
- [static var layoutProperties: LayoutProperties](./layoutproperties.md)
  Properties of a layout container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/explicitalignment(of:in:proposal:subviews:cache:))*