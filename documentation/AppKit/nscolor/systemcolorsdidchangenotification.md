# systemColorsDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent when the system colors have changed, such as through a system control panel interface.

**Availability**:
- macOS

## Declaration

```swift
class let systemColorsDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSSystemColorsDidChangeNotification;
```

## Discussion

This notification contains no notification object and no `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSColor.SystemColorsDidChangeMessage`](./systemcolorsdidchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/systemcolorsdidchangenotification)*