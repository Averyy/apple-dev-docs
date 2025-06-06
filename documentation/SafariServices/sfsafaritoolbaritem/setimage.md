# setImage(_:)

**Framework**: Safari Services  
**Kind**: method

Sets the image displayed in the toolbar button.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
func setImage(_ image: NSImage?)
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

#### Discussion

Pass nil to use the image specified in the `Info.plist` file.

## Parameters

- `image`: The image to display in the toolbar button.

## See Also

- [func setEnabled(Bool, withBadgeText: String?)](sfsafaritoolbaritem/setenabled(_:withbadgetext:).md)
  Sets the enabled state and the badge text for the toolbar item.
- [func setBadgeText(String?)](sfsafaritoolbaritem/setbadgetext(_:).md)
  Sets the badge text for the toolbar item.
- [func setEnabled(Bool)](sfsafaritoolbaritem/setenabled(_:).md)
  Sets whether the toolbar item is enabled.
- [func setLabel(String?)](sfsafaritoolbaritem/setlabel(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/setimage(_:))*