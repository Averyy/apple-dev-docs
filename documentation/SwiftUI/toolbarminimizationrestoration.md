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

### Type Properties
- [static let atScrollEdge: ToolbarMinimizationRestoration](toolbarminimizationrestoration/atscrolledge.md)
  The toolbar restores only when the scroll view’s content reaches the scroll edge.
- [static let automatic: ToolbarMinimizationRestoration](toolbarminimizationrestoration/automatic.md)
  The system determines the restoration behavior.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration)*