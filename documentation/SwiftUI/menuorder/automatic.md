# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The ordering of the menu chosen by the system for the current context.

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
static let automatic: MenuOrder
```

#### Discussion

On iOS, this order resolves to [`fixed`](./fixed.md) for menus presented within scrollable content. Pickers that use the [`menu`](../pickerstyle/menu.md) style also default to [`fixed`](./fixed.md) order. In all other cases, menus default to [`priority`](./priority.md) order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to [`fixed`](./fixed.md) order.

## See Also

### Getting menu orders
- [static let fixed: MenuOrder](./fixed.md)
  Order items from top to bottom.
- [static let priority: MenuOrder](./priority.md)
  Keep the first items closest to user’s interaction point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menuorder/automatic)*