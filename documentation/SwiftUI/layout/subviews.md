# Layout.Subviews

**Framework**: SwiftUI  
**Kind**: typealias

A collection of proxies for the subviews of a layout view.

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
typealias Subviews = LayoutSubviews
```

#### Discussion

This collection doesn’t store views. Instead it stores instances of [`LayoutSubview`](layoutsubview.md), each of which acts as a proxy for one of the views arranged by the layout. Use the proxies to get information about the views, and to tell the views where to appear.

For more information about the behavior of the underlying collection type, see [`LayoutSubviews`](layoutsubviews.md).

## See Also

- [func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGSize](layout/sizethatfits(proposal:subviews:cache:).md)
  Returns the size of the composite view, given a proposed size and the view’s subviews.
- [func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache)](layout/placesubviews(in:proposal:subviews:cache:).md)
  Assigns positions to each of the layout’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/subviews)*