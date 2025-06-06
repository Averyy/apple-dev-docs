# NSPasteboard.AccessBehavior

**Framework**: AppKit  
**Kind**: enum

A value indicating pasteboard access behavior.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum AccessBehavior
```

## Topics

### Working with defined behaviors
- [NSPasteboard.AccessBehavior.alwaysAllow](nspasteboard/accessbehavior-swift.enum/alwaysallow.md)
  The system will automatically allow all pasteboard access, without notifying the user.  The app is listed in the corresponding System Settings pane.
- [NSPasteboard.AccessBehavior.alwaysDeny](nspasteboard/accessbehavior-swift.enum/alwaysdeny.md)
  The system will automatically deny all pasteboard access, without notifying the user. However, access that is both user originated and paste related will always be allowed, and will not result in a notification. The app is listed in the corresponding System Settings pane.
- [NSPasteboard.AccessBehavior.ask](nspasteboard/accessbehavior-swift.enum/ask.md)
  The system will notify the user and ask for permission before granting pasteboard access. However, access that is both user originated and paste related will always be allowed, and will not result in a notification. The app is listed in the corresponding System Settings pane.
- [NSPasteboard.AccessBehavior.default](nspasteboard/accessbehavior-swift.enum/default.md)
  The default behavior for the General pasteboard is to ask upon programmatic access. All other pasteboards default to always allow access. If an app has never triggered a pasteboard access alert, its General pasteboard will report `.default` behavior. Such an app is not shown in the corresponding System Settings pane. Once programmatic pasteboard access triggers the first pasteboard access alert, the state automatically changes to `.ask`. At this point the app starts being shown in System Settings, where the user can toggle the behavior between `.ask`, `.alwaysAllow`, and `.alwaysDeny`.
### Initializers
- [init?(rawValue: Int)](nspasteboard/accessbehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var accessBehavior: NSPasteboard.AccessBehavior](nspasteboard/accessbehavior-9k4t4.md)
  The current pasteboard access behavior. The user can customize this behavior per-app in System Settings for any app that has triggered a pasteboard access alert in the past.
- [var accessBehavior: NSPasteboard.AccessBehavior](nspasteboard/accessbehavior-86972.md)
  The current pasteboard access behavior. The user can customize this behavior per-app in System Settings for any app that has triggered a pasteboard access alert in the past.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/accessbehavior-swift.enum)*