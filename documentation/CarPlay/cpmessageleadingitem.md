# CPMessageLeadingItem

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of symbol to display at the leading edge of a message list row.

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

Use these constants to specify symbols that are common to conversations and contacts.

## Topics

### Leading Items
- [CPMessageLeadingItem.none](./cpmessageleadingitem/none.md)
  An option to display no symbol.
- [CPMessageLeadingItem.pin](./cpmessageleadingitem/pin.md)
  An option to display a pin image in the row.
- [CPMessageLeadingItem.star](./cpmessageleadingitem/star.md)
  An option to display a star image in the row.
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

### Getting the leading item
- [var leadingItem: CPMessageLeadingItem](./cpmessagelistitemleadingconfiguration/leadingitem.md)
  The standard system symbol to display in the row’s leading region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessageleadingitem)*