# updates(count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates an update-style badge with an integer count and a predefined label that represents the number of available updates.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class func updates(count itemCount: Int) -> Self
```

```objc
+ (instancetype) updatesWithCount:(NSInteger) itemCount;
```

## Return Value

Returns a new badge item of type [`NSMenuItemBadge.BadgeType.updates`](./badgetype/updates.md).

## Parameters

- `itemCount`: The badge count.

## See Also

### Creating badges of a specific type
- [class func alerts(count: Int) -> Self](./alerts%28count%29.md)
  Creates an alert-style badge with an integer count and a predefined label that represents the number of alerts.
- [class func newItems(count: Int) -> Self](./newitems%28count%29.md)
  Creates a new item-style badge with an integer count and a predefined label that represents the number of new items.
- [NSMenuItemBadge.BadgeType](./badgetype.md)
  Constants that define types of badges for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/updates(count:))*