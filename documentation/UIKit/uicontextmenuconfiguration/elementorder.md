# UIContextMenuConfiguration.ElementOrder

**Framework**: UIKit  
**Kind**: enum

Constants that define the ordering strategy for menu elements in a context menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum ElementOrder
```

## Topics

### Constants
- [UIContextMenuConfiguration.ElementOrder.automatic](uicontextmenuconfiguration/elementorder/automatic.md)
  A constant that allows the system to choose an ordering strategy according to the current context.
- [UIContextMenuConfiguration.ElementOrder.priority](uicontextmenuconfiguration/elementorder/priority.md)
  A constant that displays menu elements according to their priority.
- [UIContextMenuConfiguration.ElementOrder.fixed](uicontextmenuconfiguration/elementorder/fixed.md)
  A constant that displays menu elements in a fixed order.
### Initializers
- [init?(rawValue: Int)](uicontextmenuconfiguration/elementorder/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uicontextmenuconfiguration/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/elementorder)*