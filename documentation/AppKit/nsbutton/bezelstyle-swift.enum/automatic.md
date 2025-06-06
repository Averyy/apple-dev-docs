# NSButton.BezelStyle.automatic

**Framework**: AppKit  
**Kind**: case

The default button style based on the button’s contents and position within the window.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case automatic
```

#### Discussion

The system picks which style of button to display automatically based on context and content. This ensures the button displays correctly in toolbars, forms, and touch bar.

In a normal window context, the system picks the [`NSButton.BezelStyle.push`](nsbutton/bezelstyle-swift.enum/push.md) button style. If the system detects that the button has a title that spans multiple lines, or the image content is too tall, it uses [`NSButton.BezelStyle.flexiblePush`](nsbutton/bezelstyle-swift.enum/flexiblepush.md).

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/automatic)*