# NSMenuItemBadge.BadgeType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define types of badges for display.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum BadgeType
```

```c
enum NSMenuItemBadgeType : NSInteger;
```

## Overview

The predefined strings that display are localizable and automatically handle any pluralization of [`itemCount`](./itemcount.md).

## Topics

### Getting badge types
- [NSMenuItemBadge.BadgeType.alerts](./badgetype/alerts.md)
  A badge representing the number of alerts.
- [NSMenuItemBadge.BadgeType.newItems](./badgetype/newitems.md)
  A badge representing the number of new items.
- [NSMenuItemBadge.BadgeType.none](./badgetype/none.md)
  A badge with no string portion.
- [NSMenuItemBadge.BadgeType.updates](./badgetype/updates.md)
  A badge representing the number of available updates.
### Initializers
- [init?(rawValue: Int)](./badgetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating badges of a specific type
- [class func alerts(count: Int) -> Self](./alerts%28count%29.md)
  Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.
- [class func newItems(count: Int) -> Self](./newitems%28count%29.md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [class func updates(count: Int) -> Self](./updates%28count%29.md)
  Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/badgetype)*