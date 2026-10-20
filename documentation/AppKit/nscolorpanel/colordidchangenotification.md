# colorDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when the color of the `NSColorPanel` is set, as when [`NSColorPanel`](../nscolorpanel.md) is invoked.

**Availability**:
- macOS

## Declaration

```swift
class let colorDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSColorPanelColorDidChangeNotification;
```

#### Discussion

The notification object is the notifying `NSColorPanel`. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSColorPanel.ColorDidChangeMessage`](./colordidchangemessage.md).

## See Also

### Responding to a color change
- [protocol NSColorChanging](../nscolorchanging.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/colordidchangenotification)*