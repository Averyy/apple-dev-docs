# NSMenuItemBadge.BadgeType

**Framework**: AppKit  
**Kind**: enum

Constants that define types of badges for display.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum BadgeType
```

#### Overview

The predefined strings that display are localizable and automatically handle any pluralization of [`itemCount`](nsmenuitembadge/itemcount.md).

## Topics

### Getting badge types
- [NSMenuItemBadge.BadgeType.alerts](nsmenuitembadge/badgetype/alerts.md)
  A badge representing the number of alerts.
- [NSMenuItemBadge.BadgeType.newItems](nsmenuitembadge/badgetype/newitems.md)
  A badge representing the number of new items.
- [NSMenuItemBadge.BadgeType.none](nsmenuitembadge/badgetype/none.md)
  A badge with no string portion.
- [NSMenuItemBadge.BadgeType.updates](nsmenuitembadge/badgetype/updates.md)
  A badge representing the number of available updates.
### Initializers
- [init?(rawValue: Int)](nsmenuitembadge/badgetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func alerts(count: Int) -> Self](nsmenuitembadge/alerts(count:).md)
  Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.
- [class func newItems(count: Int) -> Self](nsmenuitembadge/newitems(count:).md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [class func updates(count: Int) -> Self](nsmenuitembadge/updates(count:).md)
  Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/badgetype)*