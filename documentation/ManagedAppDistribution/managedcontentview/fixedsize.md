# fixedSize()

**Framework**: ManagedAppDistribution  
**Kind**: method

Fixes this view at its ideal size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func fixedSize() -> some View
```

#### Return Value

A view that fixes this view at its ideal size.

#### Discussion

During the layout of the view hierarchy, each view proposes a size to each child view it contains. If the child view doesn’t need a fixed size it can accept and conform to the size offered by the parent.

For example, a `Text` view placed in an explicitly sized frame wraps and truncates its string to remain within its parent’s bounds:

```None
Text("A single line of text, too long to fit in a box.")
    .frame(width: 200, height: 200)
    .border(Color.gray)
```

The `fixedSize()` modifier can be used to create a view that maintains the  of its children both dimensions:

```None
Text("A single line of text, too long to fit in a box.")
    .fixedSize()
    .frame(width: 200, height: 200)
    .border(Color.gray)
```

This can result in the view exceeding the parent’s bounds, which may or may not be the effect you want.

You can think of `fixedSize()` as the creation of a  to the view size proposed to a view by its parent. The ideal size of a view, and the specific effects of `fixedSize()` depends on the particular view and how you have configured it.

To create a view that fixes the view’s size in either the horizontal or vertical dimensions, see `View/fixedSize(horizontal:vertical:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/fixedsize())*