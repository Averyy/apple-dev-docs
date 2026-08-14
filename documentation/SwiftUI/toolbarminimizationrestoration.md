# ToolbarMinimizationRestoration

**Framework**: SwiftUI  
**Kind**: struct

The restoration behavior during toolbar minimization.

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
struct ToolbarMinimizationRestoration
```

#### Overview

Use this type with the [`toolbarMinimizationRestoration(_:for:)`](view/toolbarminimizationrestoration(_:for:).md) modifier to control when a minimized toolbar restores. By default the toolbar restores when the user reverses scroll direction; with [`atScrollEdge`](toolbarminimizationrestoration/atscrolledge.md), the toolbar instead restores only when the scroll view’s content reaches the scroll edge – appropriate for screens where the bar is mostly chrome that doesn’t need to follow the user.

```swift
.toolbarMinimizationBehavior(
    .onScrollDown, for: .navigationBar)
.toolbarMinimizationRestoration(
    .atScrollEdge, for: .navigationBar)
```

## Topics

### Getting restoration options
- [static let atScrollEdge: ToolbarMinimizationRestoration](toolbarminimizationrestoration/atscrolledge.md)
  The toolbar restores only when the scroll view’s content reaches the scroll edge.
- [static let automatic: ToolbarMinimizationRestoration](toolbarminimizationrestoration/automatic.md)
  The system determines the restoration behavior.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func toolbarMinimizationBehavior(ToolbarMinimizationBehavior, for: ToolbarPlacement...) -> some View](view/toolbarminimizationbehavior(_:for:).md)
  Sets the minimize behavior for the specified bars.
- [struct ToolbarMinimizationBehavior](toolbarminimizationbehavior.md)
  The minimization behavior of a toolbar.
- [func toolbarMinimizationRestoration(ToolbarMinimizationRestoration, for: ToolbarPlacement...) -> some View](view/toolbarminimizationrestoration(_:for:).md)
  Sets the restoration behavior for the specified bars during minimization.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.
- [struct ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment.md)
  The safe area adjustment during toolbar minimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration)*