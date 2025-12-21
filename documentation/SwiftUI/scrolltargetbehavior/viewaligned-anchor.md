# viewAligned(anchor:)

**Framework**: SwiftUI  
**Kind**: method

The scroll behavior that aligns scroll targets to view-based geometry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func viewAligned(anchor: UnitPoint?) -> Self
```

#### Discussion

You use this behavior when a scroll view should always align its scroll targets to a rectangle that’s aligned to the geometry of a view. In the following example, the scroll view always picks an item view to settle on.

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned(anchor: .center))
.padding(.horizontal, 20.0)
```

You configure which views should be used for settling using the `View/scrollTargetLayout()` modifier. Apply this modifier to a layout container like [`LazyVStack`](lazyvstack.md) or [`HStack`](hstack.md) and each individual view in that layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views that can be scrolled at a time by using the `ViewAlignedScrollTargetBehavior.LimitBehavior` type. Provide a value of `ViewAlignedScrollTargetBehavior.LimitBehavior/always` to always have the behavior only allow a few views to be scrolled at a time.

You can further customize how the view aligned behavior aligns the view within the visible region of the scroll view by providing a custom anchor. By default, the behavior will align the view to the top or leading edge of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehavior/viewaligned(anchor:))*