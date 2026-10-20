# NSButton.BezelStyle.disclosure

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A bezel style button for use with a disclosure triangle.

**Availability**:
- macOS

## Declaration

```swift
case disclosure
```

```c
NSBezelStyleDisclosure
```

#### Discussion

Use this style of button when you want to reveal more information. When you use this bezel style along with the [`NSButton.ButtonType.pushOnPushOff`](../buttontype/pushonpushoff.md) button type, the button points it’s disclosure triangle to the right representing a closed state. When someone clicks the button the triangle animates down representing an open state.

**Swift**:

```swift
let button = NSButton()
button.title = ""
button.setButtonType(.pushOnPushOff)
button.bezelStyle = .disclosure
```

**Objective-C**:

```objc
NSButton *button = [[NSButton alloc] init];
button.title = @"";
button.bezelStyle = NSBezelStyleDisclosure;
[button setButtonType:NSButtonTypePushOnPushOff];
```

For design guidance, see [Human Interface Guidelines > Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

### Disclosure
- [NSButton.BezelStyle.pushDisclosure](./pushdisclosure.md)
  A bezel style push button with a disclosure triangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure)*