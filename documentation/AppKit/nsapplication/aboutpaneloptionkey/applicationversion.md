# applicationVersion

**Framework**: AppKit  
**Kind**: property

The version information to display in the About panel.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let applicationVersion: NSApplication.AboutPanelOptionKey
```

#### Discussion

The value of this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object with the app version (“Version 1.0”). If not specified, AppKit obtains the version string from the `CFBundleShortVersionString` key in the app’s `Info.plist` file. If neither is available, AppKit uses the build version, printed as `Version x.x`.

## See Also

- [static let applicationIcon: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationName: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationname.md)
  The name of the application to display in the About panel.
- [static let credits: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/credits.md)
  The credits string to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/version.md)
  The version number to display in the About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey/applicationversion)*