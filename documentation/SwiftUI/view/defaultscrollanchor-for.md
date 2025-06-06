# defaultScrollAnchor(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Associates an anchor to control the position of a scroll view in a particular circumstance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func defaultScrollAnchor(_ anchor: UnitPoint?, for role: ScrollAnchorRole) -> some View
```

#### Discussion

You can associate a [`UnitPoint`](unitpoint.md) to a [`ScrollView`](scrollview.md) using the [`defaultScrollAnchor(_:)`](view/defaultscrollanchor(_:).md) modifier. By default, the system uses this point for different kinds of behaviors including:

- Where the scroll view should initially be scrolled
- How the scroll view should handle content size or container size changes
- How the scroll view should align content smaller than its container size

You can further customize this behavior by assigning different unit points for these different cases.

For example, you can use the [`defaultScrollAnchor(_:)`](view/defaultscrollanchor(_:).md) modifier to provide a value of [`bottom`](unitpoint/bottom.md) as the anchor for all cases and then opt out of certain cases by providing a different value for them.

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
.defaultScrollAnchor(.topLeading, for: .alignment)
```

## See Also

- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](view/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](view/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func defaultScrollAnchor(UnitPoint?) -> some View](view/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [struct ScrollAnchorRole](scrollanchorrole.md)
  A type defining the role of a scroll anchor.
- [struct ScrollPosition](scrollposition.md)
  A type that defines the semantic position of where a scroll view is scrolled within its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaultscrollanchor(_:for:))*