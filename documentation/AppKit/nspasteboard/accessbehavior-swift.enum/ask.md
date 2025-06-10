# NSPasteboard.AccessBehavior.ask

**Framework**: AppKit  
**Kind**: case

The system will notify the user and ask for permission before granting pasteboard access. However, access that is both user originated and paste related will always be allowed, and will not result in a notification. The app is listed in the corresponding System Settings pane.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case ask
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/accessbehavior-swift.enum/ask)*