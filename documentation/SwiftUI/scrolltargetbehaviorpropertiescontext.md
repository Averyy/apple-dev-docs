# ScrollTargetBehaviorPropertiesContext

**Framework**: SwiftUI  
**Kind**: struct

The context in which a scroll target behavior can decide its properties.

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
struct ScrollTargetBehaviorPropertiesContext
```

## Topics

### Instance Properties
- [var axes: Axis.Set](scrolltargetbehaviorpropertiescontext/axes.md)
  The scrollable axes of the scroll view.
- [var environment: EnvironmentValues](scrolltargetbehaviorpropertiescontext/environment.md)
  The environment of the scroll view.

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
- [struct ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md)
  Properties influencing the scroll view a scroll target behavior applies to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorpropertiescontext)*