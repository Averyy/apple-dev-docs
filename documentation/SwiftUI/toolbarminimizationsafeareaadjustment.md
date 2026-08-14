# ToolbarMinimizationSafeAreaAdjustment

**Framework**: SwiftUI  
**Kind**: struct

The safe area adjustment during toolbar minimization.

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
struct ToolbarMinimizationSafeAreaAdjustment
```

#### Overview

Use this type with the [`toolbarMinimizationSafeAreaAdjustment(_:for:)`](view/toolbarminimizationsafeareaadjustment(_:for:).md) modifier to control whether the safe area updates as bars minimize. By default the safe area adjusts interactively, but you can disable this to keep content in place – for example, when displaying full-bleed media beneath a minimizing bar.

```swift
.toolbarMinimizationBehavior(
    .onScrollDown, for: .navigationBar)
.toolbarMinimizationSafeAreaAdjustment(
    .disabled, for: .navigationBar)
```

## Topics

### Minimization adjustment options
- [static let automatic: ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment/automatic.md)
  The system determines the safe area adjustment.
- [static let disabled: ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment/disabled.md)
  The safe area remains unchanged as bars minimize.
- [static let enabled: ToolbarMinimizationSafeAreaAdjustment](toolbarminimizationsafeareaadjustment/enabled.md)
  The safe area adjusts interactively as bars minimize.

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
- [struct ToolbarMinimizationRestoration](toolbarminimizationrestoration.md)
  The restoration behavior during toolbar minimization.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationsafeareaadjustment)*