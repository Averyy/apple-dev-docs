# NSButton.BezelStyle.helpButton

**Framework**: AppKit  
**Kind**: case

A round button with a question mark, providing the standard help button look.

**Availability**:
- macOS ?+

## Declaration

```swift
case helpButton
```

#### Discussion

A help button appears within a view and opens app-specific help documentation.

![A screenshot displaying a voice over dialog. The main content of the dialog explains what voice over is. In the lower right corner of the dialog there is a help button.](https://docs-assets.developer.apple.com/published/9a92b8ea6d213e3336ff2b162b87043e/media-4306763%402x.png)

These are circular, consistently sized buttons that contain a question mark.

Use the system-provided help button to display your help documentation. People are familiar with the appearance of the standard help button and know that choosing it opens help content.

Include no more than one help button per window. Multiple help buttons in the same context make it hard for people to predict the result of clicking one.

Avoid displaying text that introduces a help button. People know what a help button does, so they don’t need additional descriptive text.

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

- [NSButton.BezelStyle.badge](nsbutton/bezelstyle-swift.enum/badge.md)
  A button style suitable for displaying additional information.
- [NSButton.BezelStyle.circular](nsbutton/bezelstyle-swift.enum/circular.md)
  A round button that can contain either a single character or an icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/helpbutton)*