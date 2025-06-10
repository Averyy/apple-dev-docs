# ScrollTargetBehaviorProperties

**Framework**: SwiftUI  
**Kind**: struct

Properties influencing the scroll view a scroll target behavior applies to.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct ScrollTargetBehaviorProperties
```

## Topics

### Initializers
- [init()](scrolltargetbehaviorproperties/init.md)
  Creates a default set of properties.
### Instance Properties
- [var limitsScrolls: Bool](scrolltargetbehaviorproperties/limitsscrolls.md)
  Whether this scroll target behavior should limit the distance a scroll view scrolls by default. When enabled, the scroll view prefers to scroll a shorter distance. By default, this is not enabled.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.
- [struct ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md)
  The context in which a scroll target behavior can decide its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorproperties)*