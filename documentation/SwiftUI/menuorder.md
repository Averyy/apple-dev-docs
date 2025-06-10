# MenuOrder

**Framework**: SwiftUI  
**Kind**: struct

The order in which a menu presents its content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct MenuOrder
```

#### Overview

You can configure the preferred menu order using the [`menuOrder(_:)`](view/menuorder(_:).md) view modifier.

## Topics

### Getting menu orders
- [static let automatic: MenuOrder](menuorder/automatic.md)
  The ordering of the menu chosen by the system for the current context.
- [static let fixed: MenuOrder](menuorder/fixed.md)
  Order items from top to bottom.
- [static let priority: MenuOrder](menuorder/priority.md)
  Keep the first items closest to user’s interaction point.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func menuOrder(MenuOrder) -> some View](view/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [var menuOrder: MenuOrder](environmentvalues/menuorder.md)
  The preferred order of items for menus presented from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menuorder)*