# currentControlTintDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Sent after the user changes control tint preference.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let currentControlTintDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is `NSApp`. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let systemColorsDidChangeNotification: NSNotification.Name](nscolor/systemcolorsdidchangenotification.md)
  Sent when the system colors have changed, such as through a system control panel interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltintdidchangenotification)*