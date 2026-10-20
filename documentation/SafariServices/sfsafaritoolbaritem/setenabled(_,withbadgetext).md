# setEnabled(_:withBadgeText:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Sets the enabled state and the badge text for the toolbar item.

**Availability**:
- macOS 10.12+ - Deprecated in 10.13

> **Deprecated**: use -setEnabled: and -setBadgeText:

## Declaration

```swift
func setEnabled(_ enabled: Bool, withBadgeText badgeText: String?)
```

```objc
- (void) setEnabled:(BOOL) enabled withBadgeText:(NSString *) badgeText;
```

#### Discussion

The badge text is visible even when the toolbar item is disabled.

## Parameters

- `enabled`: [`true`](../../Swift/true.md) to enable the toolbar item; otherwise [`false`](../../Swift/false.md).
- `badgeText`: String to display on the badge. Pass `nil` to remove the badge.

## See Also

### Controlling Toolbar Items
- [func setBadgeText(String?)](./setbadgetext%28_%29.md)
  Sets the badge text for the toolbar item.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets whether the toolbar item is enabled.
- [func setImage(NSImage?)](./setimage%28_%29.md)
  Sets the image displayed in the toolbar button.
- [func setLabel(String?)](./setlabel%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/setenabled(_:withbadgetext:))*