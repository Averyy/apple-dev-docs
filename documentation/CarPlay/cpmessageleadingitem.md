# CPMessageLeadingItem

**Framework**: CarPlay  
**Kind**: enum

The accessories that a message list item can display in its leading region.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPMessageLeadingItem
```

#### Overview

Use these constants when creating instances of [`CPMessageListItemLeadingConfiguration`](cpmessagelistitemleadingconfiguration.md). A leading item can provide additional context for a list item’s contents, or help communicate its behavior.

## Topics

### Leading Items
- [CPMessageLeadingItem.none](cpmessageleadingitem/none.md)
  Don’t show a leading item.
- [CPMessageLeadingItem.pin](cpmessageleadingitem/pin.md)
  Show a pin icon.
- [CPMessageLeadingItem.star](cpmessageleadingitem/star.md)
  Show a star icon.
### Initializers
- [init?(rawValue: Int)](cpmessageleadingitem/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var leadingItem: CPMessageLeadingItem](cpmessagelistitemleadingconfiguration/leadingitem.md)
  The configuration’s item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessageleadingitem)*