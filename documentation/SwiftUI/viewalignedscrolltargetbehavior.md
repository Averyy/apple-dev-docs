# ViewAlignedScrollTargetBehavior

**Framework**: SwiftUI  
**Kind**: struct

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
struct ViewAlignedScrollTargetBehavior
```

#### Overview

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

You configure which views should be used for settling using the [`scrollTargetLayout(isEnabled:)`](view/scrolltargetlayout(isenabled:).md) modifier. Apply this modifier to a layout container like [`LazyVStack`](lazyvstack.md) or [`HStack`](hstack.md) and each individual view in that layout will be considered for alignment.

You can customize whether the view aligned behavior limits the number of views that can be scrolled at a time by using the [`ViewAlignedScrollTargetBehavior.LimitBehavior`](viewalignedscrolltargetbehavior/limitbehavior.md) type. Provide a value of [`always`](viewalignedscrolltargetbehavior/limitbehavior/always.md) to always have the behavior only allow a few views to be scrolled at a time.

By default, the view aligned behavior will limit the number of views it scrolls when in a compact horizontal size class when scrollable in the horizontal axis, when in a compact vertical size class when scrollable in the vertical axis, and otherwise does not impose any limit on the number of views that can be scrolled.

## Topics

### Creating the target behavior
- [init(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior)](viewalignedscrolltargetbehavior/init(limitbehavior:).md)
  Creates a view aligned scroll behavior.
- [ViewAlignedScrollTargetBehavior.LimitBehavior](viewalignedscrolltargetbehavior/limitbehavior.md)
  A type that defines the amount of views that can be scrolled at a time.
### Initializers
- [init(anchor: UnitPoint?)](viewalignedscrolltargetbehavior/init(anchor:).md)
  Creates a view aligned scroll behavior with the provided anchor.
- [init(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior, anchor: UnitPoint?)](viewalignedscrolltargetbehavior/init(limitbehavior:anchor:).md)
  Creates a view aligned scroll behavior with the provided limit behavior and anchor.

## Relationships

### Conforms To
- [ScrollTargetBehavior](scrolltargetbehavior.md)

## See Also

- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](view/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
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
- [struct AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.
- [struct ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md)
  Properties influencing the scroll view a scroll target behavior applies to.
- [struct ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md)
  The context in which a scroll target behavior can decide its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewalignedscrolltargetbehavior)*