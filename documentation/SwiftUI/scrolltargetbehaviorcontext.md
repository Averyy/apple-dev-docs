# ScrollTargetBehaviorContext

**Framework**: SwiftUI  
**Kind**: struct

The context in which a scroll target behavior updates its scroll target.

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
@dynamicMemberLookup
struct ScrollTargetBehaviorContext
```

## Topics

### Getting the scroll target behavior context
- [var axes: Axis.Set](scrolltargetbehaviorcontext/axes.md)
  The axes in which the scrollable view is scrollable.
- [var containerSize: CGSize](scrolltargetbehaviorcontext/containersize.md)
  The size of the container of the scrollable view.
- [var contentSize: CGSize](scrolltargetbehaviorcontext/contentsize.md)
  The size of the content of the scrollable view.
- [var originalTarget: ScrollTarget](scrolltargetbehaviorcontext/originaltarget.md)
  The original target when the scroll gesture began.
- [var velocity: CGVector](scrolltargetbehaviorcontext/velocity.md)
  The current velocity of the scrollable view’s scroll gesture.
### Accessing the context
- [subscript<T>(dynamicMember _: KeyPath<EnvironmentValues, T>) -> T](scrolltargetbehaviorcontext/subscript(dynamicmember:).md)

## See Also

- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](view/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](view/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [struct ScrollTarget](scrolltarget.md)
  A type defining the target in which a scroll view should try and scroll to.
- [protocol ScrollTargetBehavior](scrolltargetbehavior.md)
  A type that defines the scroll behavior of a scrollable view.
- [struct PagingScrollTargetBehavior](pagingscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to container-based geometry.
- [struct ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [struct AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorcontext)*