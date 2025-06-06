# viewAligned

**Framework**: SwiftUI  
**Kind**: property

The scroll behavior that aligns scroll targets to view-based geometry.

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
static var viewAligned: ViewAlignedScrollTargetBehavior { get }
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
.scrollTargetBehavior(.viewAligned)
.padding(.horizontal, 20.0)
```

You configure which views should be used for settling using the `View/scrollTargetLayout()` modifier. Apply this modifier to a layout container like [`LazyVStack`](lazyvstack.md) or [`HStack`](hstack.md) and each individual view in that layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views that can be scrolled at a time by using the `ViewAlignedScrollTargetBehavior.LimitBehavior` type. Provide a value of `ViewAlignedScrollTargetBehavior.LimitBehavior/always` to always have the behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior limits the number of views it scrolls when in a compact horizontal size class when scrollable in the horizontal axis, when in a compact vertical size class when scrollable in the vertical axis, and otherwise doesn’t impose any limit on the number of views that can be scrolled.

## See Also

- [static var paging: PagingScrollTargetBehavior](scrolltargetbehavior/paging.md)
  The scroll behavior that aligns scroll targets to container-based geometry.
- [static func viewAligned(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self](scrolltargetbehavior/viewaligned(limitbehavior:).md)
  The scroll behavior that aligns scroll targets to view-based geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehavior/viewaligned)*