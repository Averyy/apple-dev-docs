# scrollTargetBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the scroll behavior of views scrollable in the provided axes.

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
func scrollTargetBehavior(_ behavior: some ScrollTargetBehavior) -> some View
```

#### Discussion

A scrollable view calculates where scroll gestures should end using its deceleration rate and the state of its scroll gesture by default. A scroll behavior allows for customizing this logic. You can provide your own [`ScrollTargetBehavior`](scrolltargetbehavior.md) or use one of the built in behaviors provided by SwiftUI.

##### Paging Behavior

SwiftUI offers a [`PagingScrollTargetBehavior`](pagingscrolltargetbehavior.md) behavior which uses the geometry of the scroll view to decide where to allow scrolls to end.

In the following example, every view in the lazy stack is flexible in both directions and the scroll view will settle to container aligned boundaries.

```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

##### View Aligned Behavior

SwiftUI offers a [`ViewAlignedScrollTargetBehavior`](viewalignedscrolltargetbehavior.md) scroll behavior that will always settle on the geometry of individual views.

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
.safeAreaPadding(.horizontal, 20.0)
```

You configure which views should be used for settling using the [`scrollTargetLayout(isEnabled:)`](view/scrolltargetlayout(isenabled:).md) modifier. Apply this modifier to a layout container like [`LazyVStack`](lazyvstack.md) or [`HStack`](hstack.md) and each individual view in that layout will be considered for alignment.

## See Also

- [func scrollTargetLayout(isEnabled: Bool) -> some View](view/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [struct ScrollTarget](scrolltarget.md)
  A type defining the target in which a scroll view should try and scroll to.
- [protocol ScrollTargetBehavior](scrolltargetbehavior.md)
  A type that defines the scroll behavior of a scrollable view.
- [struct ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md)
  The context in which a scroll target behavior updates its scroll target.
- [struct PagingScrollTargetBehavior](pagingscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to container-based geometry.
- [struct ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [struct AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolltargetbehavior(_:))*