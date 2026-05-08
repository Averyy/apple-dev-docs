# AnyScrollTargetBehavior

**Framework**: SwiftUI  
**Kind**: struct

A type-erased scroll target behavior.

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
@frozen
struct AnyScrollTargetBehavior
```

#### Overview

Provide this to the [`scrollTargetBehavior(_:)`](view/scrolltargetbehavior(_:).md) modifier. When the underlying behavior changes, the scroll view to which this behavior applies will be updated.

Use this to dynamically control the scroll target behavior at runtime. For example, you could provide a paging behavior in compact size classes and a view aligned behavior otherwise.

```swift
@Environment(\.horizontalSizeClass) var sizeClass

var body: some View {
    ScrollView { ... }
        .scrollTargetBehavior(scrollTargetBehavior)
}

 var scrollTargetBehavior: some ScrollTargetBehavior {
    sizeClass == .compact
        ? AnyScrollTargetBehavior(.paging)
        : AnyScrollTargetBehavior(.viewAligned)
}
```

## Topics

### Initializers
- [init(some ScrollTargetBehavior)](anyscrolltargetbehavior/init(_:).md)
  Creates a new type-erase scroll target behavior.
### Instance Properties
- [var base: any ScrollTargetBehavior](anyscrolltargetbehavior/base.md)
  The type-erased scroll target behavior.

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
- [struct ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [struct ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md)
  Properties influencing the scroll view a scroll target behavior applies to.
- [struct ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md)
  The context in which a scroll target behavior can decide its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anyscrolltargetbehavior)*