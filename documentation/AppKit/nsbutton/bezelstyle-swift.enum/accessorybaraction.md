# NSButton.BezelStyle.accessoryBarAction

**Framework**: AppKit  
**Kind**: case

A button style that you use for extra actions in an accessory toolbar.

**Availability**:
- macOS ?+

## Declaration

```swift
case accessoryBarAction
```

#### Discussion

Use this style when you need to perform an action on a button that appears in an accessory or scope bar.

**Swift**:

```swift
let button = NSButton()
button.title = "Accessory bar action"
button.bezelStyle = .accessoryBarAction
```

**Objective-C**:

```objc
NSButton *button = [[NSButton alloc] init];
button.title = @"Accessory bar action";
button.bezelStyle = NSBezelStyleAccessoryBarAction;
```

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

- [NSButton.BezelStyle.toolbar](nsbutton/bezelstyle-swift.enum/toolbar.md)
  A button style that’s appropriate for a toolbar item.
- [NSButton.BezelStyle.accessoryBar](nsbutton/bezelstyle-swift.enum/accessorybar.md)
  A button style that’s typically used in the context of an accessory toolbar for buttons that narrow the focus of a search or other operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/accessorybaraction)*