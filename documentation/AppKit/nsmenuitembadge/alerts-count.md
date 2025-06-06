# alerts(count:)

**Framework**: AppKit  
**Kind**: method

Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class func alerts(count itemCount: Int) -> Self
```

#### Return Value

Returns a new badge item of type [`NSMenuItemBadge.BadgeType.alerts`](nsmenuitembadge/badgetype/alerts.md).

## Parameters

- `itemCount`: The badge count.

## See Also

- [class func newItems(count: Int) -> Self](nsmenuitembadge/newitems(count:).md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [class func updates(count: Int) -> Self](nsmenuitembadge/updates(count:).md)
  Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.
- [NSMenuItemBadge.BadgeType](nsmenuitembadge/badgetype.md)
  Constants that define types of badges for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/alerts(count:))*