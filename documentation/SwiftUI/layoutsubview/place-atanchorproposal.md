# place(at:anchor:proposal:)

**Framework**: SwiftUI  
**Kind**: method

Assigns a position and proposed size to the subview.

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
func place(at position: CGPoint, anchor: UnitPoint = .topLeading, proposal: ProposedViewSize)
```

#### Discussion

Call this method from your implementation of the [`Layout`](layout.md) protocol’s [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) method for each subview arranged by the layout. Provide a position within the container’s bounds where the subview should appear, and an anchor that indicates which part of the subview appears at that point.

Include a proposed size that the subview can take into account when sizing itself. To learn the subview’s size for a given proposal before calling this method, you can call the [`dimensions(in:)`](layoutsubview/dimensions(in:).md) or [`sizeThatFits(_:)`](layoutsubview/sizethatfits(_:).md) method on the subview with the same proposal. That enables you to know subview sizes before committing to subview positions.

> ❗ **Important**: Call this method only from within your [`Layout`](layout.md) type’s implementation of the [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) method.

Call this method only from within your [`Layout`](layout.md) type’s implementation of the [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) method.

If you call this method more than once for a subview, the last call takes precedence. If you don’t call this method for a subview, the subview appears at the center of its layout container and uses the layout container’s size proposal.

## Parameters

- `position`: The place where the anchor of the subview should   appear in its container view, relative to container’s bounds.
- `anchor`: The unit point on the subview that appears at  .   You can use a built-in point, like  , or   you can create a custom  .
- `proposal`: A proposed size for the subview. In SwiftUI,   views choose their own size, but can take a size proposal from   their parent view into account when doing so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubview/place(at:anchor:proposal:))*