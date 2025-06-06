# ScrollTargetBehavior

**Framework**: SwiftUI  
**Kind**: protocol

A type that defines the scroll behavior of a scrollable view.

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
protocol ScrollTargetBehavior
```

#### Overview

A scrollable view calculates where scroll gestures should end using its deceleration rate and the state of its scroll gesture by default. A scroll behavior allows for customizing this logic.

You define a scroll behavior using the [`updateTarget(_:context:)`](scrolltargetbehavior/updatetarget(_:context:).md) method.

Using this method, you can control where someone can scroll in a scrollable view. For example, you can create a custom scroll behavior that aligns to every 10 points by doing the following:

```swift
struct BasicScrollTargetBehavior: ScrollTargetBehavior {
    func updateTarget(_ target: inout Target, context: TargetContext) {
        // Align to every 1/10 the size of the scroll view.
        target.rect.x.round(
            toMultipleOf: round(context.containerSize.width / 10.0))
    }
}
```

##### Paging Behavior

SwiftUI offers built in scroll behaviors. One such behavior is the [`PagingScrollTargetBehavior`](pagingscrolltargetbehavior.md) which uses the geometry of the scroll view to decide where to allow scrolls to end.

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

SwiftUI also offers a [`ViewAlignedScrollTargetBehavior`](viewalignedscrolltargetbehavior.md) scroll behavior that will always settle on the geometry of individual views.

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

Use types conforming to this protocol with the [`scrollTargetBehavior(_:)`](view/scrolltargetbehavior(_:).md) modifier.

## Topics

### Getting the scroll target behavior
- [static var paging: PagingScrollTargetBehavior](scrolltargetbehavior/paging.md)
  The scroll behavior that aligns scroll targets to container-based geometry.
- [static var viewAligned: ViewAlignedScrollTargetBehavior](scrolltargetbehavior/viewaligned.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [static func viewAligned(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self](scrolltargetbehavior/viewaligned(limitbehavior:).md)
  The scroll behavior that aligns scroll targets to view-based geometry.
### Updating the proposed target
- [func updateTarget(inout ScrollTarget, context: Self.TargetContext)](scrolltargetbehavior/updatetarget(_:context:).md)
  Updates the proposed target that a scrollable view should scroll to.
- [ScrollTargetBehavior.TargetContext](scrolltargetbehavior/targetcontext.md)
  The context in which a scroll behavior updates the scroll target.
### Instance Methods
- [func properties(context: Self.PropertiesContext) -> Self.Properties](scrolltargetbehavior/properties(context:).md)
  Properties of this behavior
### Type Aliases
- [ScrollTargetBehavior.Properties](scrolltargetbehavior/properties.md)
  The properties of a scroll behavior
- [ScrollTargetBehavior.PropertiesContext](scrolltargetbehavior/propertiescontext.md)
  The properties context of a scroll behavior.

## Relationships

### Conforming Types
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md)
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)

## See Also

- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](view/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](view/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [struct ScrollTarget](scrolltarget.md)
  A type defining the target in which a scroll view should try and scroll to.
- [struct ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md)
  The context in which a scroll target behavior updates its scroll target.
- [struct PagingScrollTargetBehavior](pagingscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to container-based geometry.
- [struct ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [struct AnyScrollTargetBehavior](anyscrolltargetbehavior.md)
  A type-erased scroll target behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehavior)*