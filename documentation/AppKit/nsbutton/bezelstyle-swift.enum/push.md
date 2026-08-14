# NSButton.BezelStyle.push

**Framework**: AppKit  
**Kind**: case

A standard push style button.

**Availability**:
- macOS ?+

## Declaration

```swift
case push
```

#### Discussion

Use this style when you want the default button style.

**Swift**:

```swift
// Create a push style button.
let cancelButton = NSButton()
cancelButton.title = "Cancel"
cancelButton.bezelStyle = .push

// Create a push style button.
let saveButton = NSButton()
saveButton.title = "Save"
saveButton.bezelStyle = .push
// Make this the default button.
saveButton.keyEquivalent = "\r"
```

**Objective-C**:

```objc
// Create a push style button.
NSButton *cancelButton = [[NSButton alloc] init];
cancelButton.title = @"Cancel";
cancelButton.bezelStyle = NSBezelStylePush;

// Create a push style button.
NSButton *saveButton = [[NSButton alloc] init];
saveButton.title = @"Save";
saveButton.bezelStyle = NSBezelStylePush;
// Make this the default button.
saveButton.keyEquivalent = @"/r";
```

![A screenshot of two push buttons side-by-side. The  button on the left is titled cancel. The  button on the right is active and is titled save.](/images/com.apple.appkit/media-4307817@2x.png)

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).

## See Also

- [NSButton.BezelStyle.flexiblePush](nsbutton/bezelstyle-swift.enum/flexiblepush.md)
  A push button with a flexible height to accommodate longer text labels or an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/push)*