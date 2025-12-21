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

## See Also

- [NSPasteboard.AccessBehavior.alwaysAllow](nspasteboard/accessbehavior-swift.enum/alwaysallow.md)
  The system will automatically allow all pasteboard access, without notifying the user.  The app is listed in the corresponding System Settings pane.
- [NSPasteboard.AccessBehavior.alwaysDeny](nspasteboard/accessbehavior-swift.enum/alwaysdeny.md)
  The system will automatically deny all pasteboard access, without notifying the user. However, access that is both user originated and paste related will always be allowed, and will not result in a notification. The app is listed in the corresponding System Settings pane.
- [NSPasteboard.AccessBehavior.default](nspasteboard/accessbehavior-swift.enum/default.md)
  The default behavior for the General pasteboard is to ask upon programmatic access. All other pasteboards default to always allow access. If an app has never triggered a pasteboard access alert, its General pasteboard will report `.default` behavior. Such an app is not shown in the corresponding System Settings pane. Once programmatic pasteboard access triggers the first pasteboard access alert, the state automatically changes to `.ask`. At this point the app starts being shown in System Settings, where the user can toggle the behavior between `.ask`, `.alwaysAllow`, and `.alwaysDeny`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/accessbehavior-swift.enum/ask)*