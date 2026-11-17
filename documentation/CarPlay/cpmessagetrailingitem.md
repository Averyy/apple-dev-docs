# CPMessageTrailingItem

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of symbol to display at the trailing edge of a message list row.

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

Use these constants to specify relevant symbols for the conversation or contact.

## Topics

### Trailing Items
- [CPMessageTrailingItem.none](./cpmessagetrailingitem/none.md)
  An option to display no symbol.
- [CPMessageTrailingItem.mute](./cpmessagetrailingitem/mute.md)
  An option to display a mute symbol.
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

### Getting the trailing item
- [var trailingItem: CPMessageTrailingItem](./cpmessagelistitemtrailingconfiguration/trailingitem.md)
  The standard system symbol to display in the row’s trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagetrailingitem)*