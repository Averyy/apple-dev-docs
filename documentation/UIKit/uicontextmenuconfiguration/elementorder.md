# UIContextMenuConfiguration.ElementOrder

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIContextMenuConfigurationElementOrder : NSInteger;
```

## Topics

### Constants
- [UIContextMenuConfiguration.ElementOrder.automatic](./elementorder/automatic.md)
  A constant that allows the system to choose an ordering strategy according to the current context.
- [UIContextMenuConfiguration.ElementOrder.priority](./elementorder/priority.md)
  A constant that displays menu elements according to their priority.
- [UIContextMenuConfiguration.ElementOrder.fixed](./elementorder/fixed.md)
  A constant that displays menu elements in a fixed order.
### Initializers
- [init?(rawValue: Int)](./elementorder/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the order of menu elements
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](./preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/elementorder)*