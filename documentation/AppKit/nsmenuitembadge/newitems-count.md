# newItems(count:)

**Framework**: AppKit  
**Kind**: method

Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class func newItems(count itemCount: Int) -> Self
```

#### Return Value

Returns a new badge item of type [`NSMenuItemBadge.BadgeType.newItems`](nsmenuitembadge/badgetype/newitems.md).

## Parameters

- `itemCount`: The badge count.

## See Also

- [class func alerts(count: Int) -> Self](nsmenuitembadge/alerts(count:).md)
  Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.
- [class func updates(count: Int) -> Self](nsmenuitembadge/updates(count:).md)
  Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.
- [NSMenuItemBadge.BadgeType](nsmenuitembadge/badgetype.md)
  Constants that define types of badges for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/newitems(count:))*