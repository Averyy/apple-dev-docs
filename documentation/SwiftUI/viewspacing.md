# ViewSpacing

**Framework**: SwiftUI  
**Kind**: struct

A collection of the geometric spacing preferences of a view.

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
struct ViewSpacing
```

#### Overview

This type represents how much space a view prefers to have between it and the next view in a layout. The type stores independent values for each of the top, bottom, leading, and trailing edges, and can also record different values for different kinds of adjacent views. For example, it might contain one value for the spacing to the next text view along the top and bottom edges, other values for the spacing to text views on other edges, and yet other values for other kinds of views. Spacing preferences can also vary by platform.

Your [`Layout`](layout.md) type doesn’t have to take preferred spacing into account, but if it does, you can use the [`spacing`](layoutsubview/spacing.md) preferences of the subviews in your layout container to:

- Add space between subviews when you implement the [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) method.
- Create a spacing preferences instance for the container view by implementing the [`spacing(subviews:cache:)`](layout/spacing(subviews:cache:).md) method.

## Topics

### Creating spacing instances
- [init()](viewspacing/init.md)
  Initializes an instance with default spacing values.
- [static let zero: ViewSpacing](viewspacing/zero.md)
  A view spacing instance that contains zero on all edges.
### Measuring spacing distance
- [func distance(to: ViewSpacing, along: Axis) -> CGFloat](viewspacing/distance(to:along:).md)
  Gets the preferred spacing distance along the specified axis to the view that returns a specified spacing preference.
### Merging spacing instances
- [func formUnion(ViewSpacing, edges: Edge.Set)](viewspacing/formunion(_:edges:).md)
  Merges the spacing preferences of another spacing instance with this instance for a specified set of edges.
- [func union(ViewSpacing, edges: Edge.Set) -> ViewSpacing](viewspacing/union(_:edges:).md)
  Gets a new value that merges the spacing preferences of another spacing instance with this instance for a specified set of edges.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct LayoutProperties](layoutproperties.md)
  Layout-specific properties of a layout container.
- [struct ProposedViewSize](proposedviewsize.md)
  A proposal for the size of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewspacing)*