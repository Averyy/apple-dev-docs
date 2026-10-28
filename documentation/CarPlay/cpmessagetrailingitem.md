# CPMessageTrailingItem

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The accessories that a message list item can display in its trailing region.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPMessageTrailingItem
```

```c
enum CPMessageTrailingItem : NSInteger;
```

## Overview

Use these constants when creating instances of [`CPMessageListItemTrailingConfiguration`](./cpmessagelistitemtrailingconfiguration.md). A trailing item can provide additional context for a list item’s contents, or help communicate its behavior.

## Topics

### Trailing Items
- [CPMessageTrailingItem.none](./cpmessagetrailingitem/none.md)
  Don’t show a trailing item.
- [CPMessageTrailingItem.mute](./cpmessagetrailingitem/mute.md)
  Show a muted speaker icon.
### Initializers
- [init?(rawValue: Int)](./cpmessagetrailingitem/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Trailing Item
- [var trailingItem: CPMessageTrailingItem](./cpmessagelistitemtrailingconfiguration/trailingitem.md)
  The configuration’s item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagetrailingitem)*