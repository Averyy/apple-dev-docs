# setBadgeText(_:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Sets the badge text for the toolbar item.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
func setBadgeText(_ badgeText: String?)
```

```objc
- (void) setBadgeText:(NSString *) badgeText;
```

## Mentions

- [Adjusting settings for a toolbar item](../adjusting-settings-for-a-toolbar-item.md)

## Parameters

- `badgeText`: String to display on the badge. Pass `nil` to remove the badge.

## See Also

### Controlling Toolbar Items
- [func setEnabled(Bool, withBadgeText: String?)](./setenabled%28_,withbadgetext%29.md)
  Sets the enabled state and the badge text for the toolbar item.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets whether the toolbar item is enabled.
- [func setImage(NSImage?)](./setimage%28_%29.md)
  Sets the image displayed in the toolbar button.
- [func setLabel(String?)](./setlabel%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/setbadgetext(_:))*