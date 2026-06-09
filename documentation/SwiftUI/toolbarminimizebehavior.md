# ToolbarMinimizeBehavior

**Framework**: SwiftUI  
**Kind**: struct

The minimize behavior of a toolbar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ToolbarMinimizeBehavior
```

#### Overview

Use this type with the [`toolbarMinimizeBehavior(_:for:)`](view/toolbarminimizebehavior(_:for:).md) modifier to control how toolbars minimize in response to scrolling.

On iOS, you can minimize the navigation bar using [`onScrollDown`](toolbarminimizebehavior/onscrolldown.md) or [`onScrollUp`](toolbarminimizebehavior/onscrollup.md):

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizeBehavior(
        .onScrollDown, for: .navigationBar)
}
```

## Topics

### Getting behaviors
- [static var automatic: ToolbarMinimizeBehavior](toolbarminimizebehavior/automatic.md)
  The system determines the minimize behavior. By default, navigation bars on iOS will minimize when the view has a searchable using the [`toolbarPrincipal`](searchfieldplacement/toolbarprincipal.md) placement.
### Type Properties
- [static let never: ToolbarMinimizeBehavior](toolbarminimizebehavior/never.md)
  The toolbar cannot be minimized.
- [static let onScrollDown: ToolbarMinimizeBehavior](toolbarminimizebehavior/onscrolldown.md)
  Minimize when scrolling down.
- [static let onScrollUp: ToolbarMinimizeBehavior](toolbarminimizebehavior/onscrollup.md)
  Minimize when scrolling up.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func toolbarMinimizeBehavior(ToolbarMinimizeBehavior, for: ToolbarPlacement...) -> some View](view/toolbarminimizebehavior(_:for:).md)
  Sets the minimize behavior for the specified bars.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.
- [struct ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md)
  The safe area adjustment during toolbar minimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizebehavior)*