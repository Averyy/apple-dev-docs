# NSPasteboard.AccessBehavior.alwaysDeny

**Framework**: AppKit  
**Kind**: case

The system will automatically deny all pasteboard access, without notifying the user. However, access that is both user originated and paste related will always be allowed, and will not result in a notification. The app is listed in the corresponding System Settings pane.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case alwaysDeny
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/accessbehavior-swift.enum/alwaysdeny)*