# scrollPosition(id:anchor:)

**Framework**: Assignables  
**Kind**: method

Associates a binding to be updated when a scroll view within this view scrolls.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint? = nil) -> some View
```

#### Discussion

Use this modifier along with the `View/scrollTargetLayout()` modifier to know the identity of the view that is actively scrolled. As the scroll view scrolls, the binding will be updated with the identity of the leading-most / top-most view.

Use the `View/scrollTargetLayout()` modifier to configure which the layout that contains your scroll targets. In the following example, the top-most ItemView will update with the scrolledID binding as the scroll view scrolls.

```None
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

```None
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

For example, providing a value of `UnitPoint/bottom` will prefer to have the bottom-most view chosen and prefer to scroll to views aligned to the bottom.

If no anchor has been provided, SwiftUI will scroll the minimal amount when using the scroll position to programmatically scroll to a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/scrollposition(id:anchor:))*