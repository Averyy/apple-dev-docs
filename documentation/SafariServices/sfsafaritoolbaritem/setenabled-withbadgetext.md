# setEnabled(_:withBadgeText:)

**Framework**: Safari Services  
**Kind**: method

Sets the enabled state and the badge text for the toolbar item.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func setEnabled(_ enabled: Bool, withBadgeText badgeText: String?)
```

#### Discussion

The badge text is visible even when the toolbar item is disabled.

## Parameters

- `enabled`:   to enable the toolbar item; otherwise  .
- `badgeText`: String to display on the badge. Pass   to remove the badge.

## See Also

- [func setBadgeText(String?)](sfsafaritoolbaritem/setbadgetext(_:).md)
  Sets the badge text for the toolbar item.
- [func setEnabled(Bool)](sfsafaritoolbaritem/setenabled(_:).md)
  Sets whether the toolbar item is enabled.
- [func setImage(NSImage?)](sfsafaritoolbaritem/setimage(_:).md)
  Sets the image displayed in the toolbar button.
- [func setLabel(String?)](sfsafaritoolbaritem/setlabel(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/setenabled(_:withbadgetext:))*