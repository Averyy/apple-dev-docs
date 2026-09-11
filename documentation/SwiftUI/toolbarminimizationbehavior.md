# ToolbarMinimizationBehavior

**Framework**: SwiftUI  
**Kind**: struct

The minimization behavior of a toolbar.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ToolbarMinimizationBehavior
```

#### Overview

Use this type with the [`toolbarMinimizationBehavior(_:for:)`](view/toolbarminimizationbehavior(_:for:).md) modifier to control how toolbars minimize in response to scrolling.

On iOS, you can minimize the navigation bar using [`onScrollDown`](toolbarminimizationbehavior/onscrolldown.md) or [`onScrollUp`](toolbarminimizationbehavior/onscrollup.md):

```swift
NavigationStack {
    ScrollView {
        // ...
    }
    .toolbarMinimizationBehavior(
        .onScrollDown, for: .navigationBar)
}
```

## Topics

### Getting behaviors
- [static var automatic: ToolbarMinimizationBehavior](toolbarminimizationbehavior/automatic.md)
  The system determines the minimize behavior. By default, navigation bars on iOS will minimize when the view has a searchable using the [`toolbarPrincipal`](searchfieldplacement/toolbarprincipal.md) placement.
- [static let never: ToolbarMinimizationBehavior](toolbarminimizationbehavior/never.md)
  The toolbar cannot be minimized.
- [static let onScrollDown: ToolbarMinimizationBehavior](toolbarminimizationbehavior/onscrolldown.md)
  Minimize when scrolling down.
- [static let onScrollUp: ToolbarMinimizationBehavior](toolbarminimizationbehavior/onscrollup.md)
  Minimize when scrolling up.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func toolbarMinimizationBehavior(ToolbarMinimizationBehavior, for: ToolbarPlacement...) -> some View](view/toolbarminimizationbehavior(_:for:).md)
  Sets the minimize behavior for the specified bars.
- [func toolbarMinimizationRestoration(ToolbarMinimizationRestoration, for: ToolbarPlacement...) -> some View](view/toolbarminimizationrestoration(_:for:).md)
  Sets the restoration behavior for the specified bars during minimization.
- [struct ToolbarMinimizationRestoration](toolbarminimizationrestoration.md)
  The restoration behavior during toolbar minimization.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.
- [struct ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md)
  The safe area adjustment during toolbar minimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior)*