# NSButton.BezelStyle.circular

**Framework**: AppKit  
**Kind**: case

A round button that can contain either a single character or an icon.

**Availability**:
- macOS ?+

## Declaration

```swift
case circular
```

#### Discussion

Use this button type to display either a single character:

**Swift**:

```swift
let button = NSButton()
button.title = "C"
button.bezelStyle = .circular
```

**Objective-C**:

```objc
NSButton *button = [[NSButton alloc] init];
button.title = @"C";
button.bezelStyle = NSBezelStyleCircular;
```

Or a small icon.

**Swift**:

```swift
let button = NSButton()
button.image = NSImage(systemSymbolName: "star", accessibilityDescription: "")
button.bezelStyle = .circular
```

**Objective-C**:

```objc
NSButton *button = [[NSButton alloc] init];
button.image = [NSImage imageWithSystemSymbolName:@"star" accessibilityDescription:nil];
button.bezelStyle = NSBezelStyleCircular;
```

Use system images such as [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sf-symbols) for best results as they automatically scale to fit the button. Large images don’t clip when they display with this style. Instead, they shrink to fit the button’s bounds.

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

- [NSButton.BezelStyle.helpButton](nsbutton/bezelstyle-swift.enum/helpbutton.md)
  A round button with a question mark, providing the standard help button look.
- [NSButton.BezelStyle.badge](nsbutton/bezelstyle-swift.enum/badge.md)
  A button style suitable for displaying additional information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/circular)*