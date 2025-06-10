# credits

**Framework**: AppKit  
**Kind**: property

The credits string to display in the About panel.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let credits: NSApplication.AboutPanelOptionKey
```

#### Discussion

The value of this key is an [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) displayed in the info area of the panel. If not specified, AppKit then looks for a file named “Credits.html”, “Credits.rtf”, and “Credits.rtfd”, in that order, in the bundle returned by the [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) class method main. The first file found is used. If none is found, the info area is left blank.

## See Also

- [static let applicationIcon: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationName: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationname.md)
  The name of the application to display in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationversion.md)
  The version information to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/version.md)
  The version number to display in the About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey/credits)*