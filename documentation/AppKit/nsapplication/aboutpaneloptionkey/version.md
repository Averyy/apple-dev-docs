# version

**Framework**: AppKit  
**Kind**: property

The version number to display in the About panel.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let version: NSApplication.AboutPanelOptionKey
```

#### Discussion

The value of this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object with the build version number of the app, such as `58.4`. AppKit displays this string as `(v58.4)`. If not specified, AppKit obtains the version number from the CFBundleVersion key of the app’s Info.plist file. If no version information is found, AppKit does not display version information.

## See Also

- [static let applicationIcon: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationName: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationname.md)
  The name of the application to display in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationversion.md)
  The version information to display in the About panel.
- [static let credits: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/credits.md)
  The credits string to display in the About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey/version)*