# applicationIcon

**Framework**: AppKit  
**Kind**: property

The icon to display for the app in the About panel.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let applicationIcon: NSApplication.AboutPanelOptionKey
```

#### Discussion

The value associated with this key is an [`NSImage`](nsimage.md) object. If you do not specify an image, AppKit looks for an image with the name `NSApplicationIcon`. If neither is available, this method uses the generic app icon.

## See Also

- [static let applicationName: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationname.md)
  The name of the application to display in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationversion.md)
  The version information to display in the About panel.
- [static let credits: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/credits.md)
  The credits string to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/version.md)
  The version number to display in the About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey/applicationicon)*