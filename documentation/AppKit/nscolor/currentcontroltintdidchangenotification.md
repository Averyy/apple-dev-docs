# currentControlTintDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Sent after the user changes control tint preference.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Changes to the accent color can be manually observed by implementing -viewDidChangeEffectiveAppearance in a NSView subclass, or by Key-Value Observing the -effectiveAppearance property on NSApplication. Views are automatically redisplayed when the accent color changes.

## Declaration

```swift
class let currentControlTintDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSControlTintDidChangeNotification;
```

## Discussion

The notification object is `NSApp`. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltintdidchangenotification)*