# updates(count:)

**Framework**: AppKit  
**Kind**: method

Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class func updates(count itemCount: Int) -> Self
```

#### Return Value

Returns a new badge item of type [`NSMenuItemBadge.BadgeType.updates`](nsmenuitembadge/badgetype/updates.md).

## Parameters

- `itemCount`: The badge count.

## See Also

- [class func alerts(count: Int) -> Self](nsmenuitembadge/alerts(count:).md)
  Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.
- [class func newItems(count: Int) -> Self](nsmenuitembadge/newitems(count:).md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [NSMenuItemBadge.BadgeType](nsmenuitembadge/badgetype.md)
  Constants that define types of badges for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/updates(count:))*