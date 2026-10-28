# NSButton.BezelStyle.flexiblePush

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A push button with a flexible height to accommodate longer text labels or an image.

**Availability**:
- macOS

## Declaration

```swift
case flexiblePush
```

```c
NSBezelStyleFlexiblePush
```

## Discussion

Use this style of button when you need to accommodate tall or variable height content.

Tall or variable height content includes text with newlines (`n`) as well as buttons you constrain the width of through Auto Layout. This style automatically wraps text based on button width and available space.

**Swift**:

```swift
let button = NSButton()
button.title = "Flexible\n push"
button.bezelStyle = .flexiblePush
```

**Objective-C**:

```objc
NSButton *button = [[NSButton alloc] init];
button.title = @"Flexible\n push";
button.bezelStyle = NSBezelStyleFlexiblePush;
```

For design guidance, see [Human Interface Guidelines > Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

### Push
- [NSButton.BezelStyle.push](./push.md)
  A standard push style button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/flexiblepush)*