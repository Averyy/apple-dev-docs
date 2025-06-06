# scrollPosition(id:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Associates a binding to be updated when a scroll view within this view scrolls.

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
func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint? = nil) -> some View
```

#### Discussion

Use this modifier along with the `View/scrollTargetLayout()` modifier to know the identity of the view that is actively scrolled. As the scroll view scrolls, the binding will be updated with the identity of the leading-most / top-most view.

Use the `View/scrollTargetLayout()` modifier to configure which the layout that contains your scroll targets. In the following example, the top-most ItemView will update with the scrolledID binding as the scroll view scrolls.

```swift
@Binding var items: [Item]
@Binding var scrolledID: Item.ID?

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollPosition(id: $scrolledID)
```

You can write to the binding to scroll to the view with the provided identity.

```swift
@Binding var items: [Item]
@Binding var scrolledID: Item.ID?

ScrollView {
    // ...
}
.scrollPosition(id: $scrolledID)
.toolbar {
    Button("Scroll to Top") {
        scrolledID = items.first
    }
}
```

SwiftUI will attempt to keep the view with the identity specified in the provided binding visible when events occur that might cause it to be scrolled out of view by the system. Some examples of these include:

- The data backing the content of a scroll view is re-ordered.
- The size of the scroll view changes, like when a window is resized on macOS or during a rotation on iOS.
- The scroll view initially lays out it content defaulting to the top most view, but the binding has a different view’s identity.

You can provide an anchor to this modifier to both:

- Influence which view the system chooses as the view whose identity value will update the providing binding as the scroll view scrolls.
- Control the alignment of the view when scrolling to a view when writing a new binding value.

For example, providing a value of [`bottom`](unitpoint/bottom.md) will prefer to have the bottom-most view chosen and prefer to scroll to views aligned to the bottom.

If no anchor has been provided, SwiftUI will scroll the minimal amount when using the scroll position to programmatically scroll to a view.

## See Also

- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](view/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func defaultScrollAnchor(UnitPoint?) -> some View](view/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](view/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [struct ScrollAnchorRole](scrollanchorrole.md)
  A type defining the role of a scroll anchor.
- [struct ScrollPosition](scrollposition.md)
  A type that defines the semantic position of where a scroll view is scrolled within its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrollposition(id:anchor:))*