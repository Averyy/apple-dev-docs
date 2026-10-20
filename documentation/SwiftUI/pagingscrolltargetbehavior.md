# PagingScrollTargetBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The scroll behavior that aligns scroll targets to container-based geometry.

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
struct PagingScrollTargetBehavior
```

#### Overview

In the following example, every view in the lazy stack is flexible in both directions and the scroll view settles to container-aligned boundaries.

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

## Topics

### Creating the target behavior
- [init()](./pagingscrolltargetbehavior/init%28%29.md)
  Creates a paging scroll behavior.

## Relationships

### Conforms To
- [ChartScrollTargetBehavior](../Charts/chartscrolltargetbehavior.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [ScrollTargetBehavior](./scrolltargetbehavior.md)

## See Also

### Defining scroll targets
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](./view/scrolltargetbehavior%28_%29.md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](./view/scrolltargetlayout%28isenabled%29.md)
  Configures the outermost layout as a scroll target layout.
- [struct ScrollTarget](./scrolltarget.md)
  A type defining the target in which a scroll view should try and scroll to.
- [protocol ScrollTargetBehavior](./scrolltargetbehavior.md)
  A type that defines the scroll behavior of a scrollable view.
- [struct ScrollTargetBehaviorContext](./scrolltargetbehaviorcontext.md)
  The context in which a scroll target behavior updates its scroll target.
- [struct ViewAlignedScrollTargetBehavior](./viewalignedscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [struct AnyScrollTargetBehavior](./anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.
- [struct ScrollTargetBehaviorProperties](./scrolltargetbehaviorproperties.md)
  Properties influencing the scroll view a scroll target behavior applies to.
- [struct ScrollTargetBehaviorPropertiesContext](./scrolltargetbehaviorpropertiescontext.md)
  The context in which a scroll target behavior can decide its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pagingscrolltargetbehavior)*