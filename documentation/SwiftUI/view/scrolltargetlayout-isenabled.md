# scrollTargetLayout(isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Configures the outermost layout as a scroll target layout.

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
func scrollTargetLayout(isEnabled: Bool = true) -> some View
```

#### Discussion

This modifier works together with the [`ViewAlignedScrollTargetBehavior`](viewalignedscrolltargetbehavior.md) to ensure that scroll views align to view based content.

Apply this modifier to layout containers like [`LazyHStack`](lazyhstack.md) or [`VStack`](vstack.md) within a [`ScrollView`](scrollview.md) that contain the main repeating content of your [`ScrollView`](scrollview.md).

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
```

Scroll target layouts act as a convenience for applying a `View/scrollTarget(isEnabled:)` modifier to each views in the layout.

A scroll target layout will ensure that any target layout nested within the primary one will not also become a scroll target layout.

```swift
LazyHStack { // a scroll target layout
    VStack { ... } // not a scroll target layout
    LazyHStack { ... } // also not a scroll target layout
}
.scrollTargetLayout()
```

## See Also

- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](view/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolltargetlayout(isenabled:))*