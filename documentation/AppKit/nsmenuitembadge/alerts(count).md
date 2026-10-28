# alerts(count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class func alerts(count itemCount: Int) -> Self
```

```objc
+ (instancetype) alertsWithCount:(NSInteger) itemCount;
```

## Return Value

Returns a new badge item of type [`NSMenuItemBadge.BadgeType.alerts`](./badgetype/alerts.md).

## Parameters

- `itemCount`: The badge count.

## See Also

### Creating badges of a specific type
- [class func newItems(count: Int) -> Self](./newitems%28count%29.md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [class func updates(count: Int) -> Self](./updates%28count%29.md)
  Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.
- [NSMenuItemBadge.BadgeType](./badgetype.md)
  Constants that define types of badges for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/alerts(count:))*