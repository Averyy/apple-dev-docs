# NSButton.BezelStyle.flexiblePush

**Framework**: AppKit  
**Kind**: case

A push button with a flexible height to accommodate longer text labels or an image.

**Availability**:
- macOS ?+

## Declaration

```swift
case flexiblePush
```

#### Discussion

Use this style of button when you need to accommodate tall or variable height content.

Tall or variable height content includes text with newlines (`n`) as well as buttons you constrain the width of through Auto Layout. This style automatically wraps text based on button width and available space.

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

- [NSButton.BezelStyle.push](nsbutton/bezelstyle-swift.enum/push.md)
  A standard push style button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/flexiblepush)*