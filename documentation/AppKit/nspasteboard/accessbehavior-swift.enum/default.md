# NSPasteboard.AccessBehavior.default

**Framework**: AppKit  
**Kind**: case

The default behavior for the General pasteboard is to ask upon programmatic access. All other pasteboards default to always allow access. If an app has never triggered a pasteboard access alert, its General pasteboard will report `.default` behavior. Such an app is not shown in the corresponding System Settings pane. Once programmatic pasteboard access triggers the first pasteboard access alert, the state automatically changes to `.ask`. At this point the app starts being shown in System Settings, where the user can toggle the behavior between `.ask`, `.alwaysAllow`, and `.alwaysDeny`.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case `default`
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/accessbehavior-swift.enum/default)*