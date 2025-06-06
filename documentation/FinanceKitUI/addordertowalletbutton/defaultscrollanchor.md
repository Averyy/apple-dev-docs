# defaultScrollAnchor(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Associates an anchor to control which part of the scroll view’s content should be rendered by default.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func defaultScrollAnchor(_ anchor: UnitPoint?) -> some View
```

#### Discussion

Use this modifier to specify an anchor to control both which part of the scroll view’s content should be visible initially and how the scroll view handles content size changes.

Provide a value of `UnitPoint/center`` to have the scroll view start in the center of its content when a scroll view is scrollable in both axes.

```None
ScrollView([.horizontal, .vertical]) {
    // initially centered content
}
.defaultScrollAnchor(.center)
```

Provide a value of `UnitPoint/bottom` to have the scroll view start at the bottom of its content when scrollable in the vertical axis.

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/defaultscrollanchor(_:))*