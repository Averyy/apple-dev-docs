# CPMessageLeadingItem

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The accessories that a message list item can display in its leading region.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPMessageLeadingItem
```

```c
enum CPMessageLeadingItem : NSInteger;
```

## Overview

Use these constants when creating instances of [`CPMessageListItemLeadingConfiguration`](./cpmessagelistitemleadingconfiguration.md). A leading item can provide additional context for a list item’s contents, or help communicate its behavior.

## Topics

### Leading Items
- [CPMessageLeadingItem.none](./cpmessageleadingitem/none.md)
  Don’t show a leading item.
- [CPMessageLeadingItem.pin](./cpmessageleadingitem/pin.md)
  Show a pin icon.
- [CPMessageLeadingItem.star](./cpmessageleadingitem/star.md)
  Show a star icon.
### Initializers
- [init?(rawValue: Int)](./cpmessageleadingitem/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Leading Item
- [var leadingItem: CPMessageLeadingItem](./cpmessagelistitemleadingconfiguration/leadingitem.md)
  The configuration’s item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessageleadingitem)*