# ToolbarMinimizationBehavior

**Framework**: SwiftUI  
**Kind**: struct

The minimization behavior of a toolbar.

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

### Type Properties
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
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior)*