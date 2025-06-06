# defaultScrollAnchor(_:)

**Framework**: SwiftUI  
**Kind**: method

Associates an anchor to control which part of the scroll view’s content should be rendered by default.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func defaultScrollAnchor(_ anchor: UnitPoint?) -> some View
```

#### Discussion

Use this modifier to specify an anchor to control both which part of the scroll view’s content should be visible initially and how the scroll view handles content size changes.

Provide a value of `UnitPoint/center`` to have the scroll view start in the center of its content when a scroll view is scrollable in both axes.

```swift
ScrollView([.horizontal, .vertical]) {
    // initially centered content
}
.defaultScrollAnchor(.center)
```

Provide a value of `UnitPoint/bottom` to have the scroll view start at the bottom of its content when scrollable in the vertical axis.

```swift
@Binding var items: [Item]
@Binding var scrolledID: Item.ID?

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemView(item)
        }
    }
}
.defaultScrollAnchor(.bottom)
```

The user may scroll away from the initial defined scroll position. When the content size of the scroll view changes, it may consult the anchor to know how to reposition the content.

## See Also

- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](view/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](view/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](view/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [struct ScrollAnchorRole](scrollanchorrole.md)
  A type defining the role of a scroll anchor.
- [struct ScrollPosition](scrollposition.md)
  A type that defines the semantic position of where a scroll view is scrolled within its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaultscrollanchor(_:))*