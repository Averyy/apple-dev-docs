# setImage(_:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Sets the image displayed in the toolbar button.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
func setImage(_ image: NSImage?)
```

```objc
- (void) setImage:(NSImage *) image;
```

## Mentions

- [Adjusting settings for a toolbar item](../adjusting-settings-for-a-toolbar-item.md)

#### Discussion

Pass nil to use the image specified in the `Info.plist` file.

## Parameters

- `image`: The image to display in the toolbar button.

## See Also

### Controlling Toolbar Items
- [func setEnabled(Bool, withBadgeText: String?)](./setenabled%28_,withbadgetext%29.md)
  Sets the enabled state and the badge text for the toolbar item.
- [func setBadgeText(String?)](./setbadgetext%28_%29.md)
  Sets the badge text for the toolbar item.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets whether the toolbar item is enabled.
- [func setLabel(String?)](./setlabel%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/setimage(_:))*