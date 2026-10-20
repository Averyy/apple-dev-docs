# credits

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The credits string to display in the About panel.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let credits: NSApplication.AboutPanelOptionKey
```

```c
extern NSAboutPanelOptionKey const NSAboutPanelOptionCredits;
```

#### Discussion

The value of this key is an [`NSAttributedString`](../../../Foundation/nsattributedstring.md) displayed in the info area of the panel. If not specified, AppKit then looks for a file named “Credits.html”, “Credits.rtf”, and “Credits.rtfd”, in that order, in the bundle returned by the [`Bundle`](../../../Foundation/bundle.md) class method main. The first file found is used. If none is found, the info area is left blank.

## See Also

### Option Keys
- [static let applicationIcon: NSApplication.AboutPanelOptionKey](./applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationName: NSApplication.AboutPanelOptionKey](./applicationname.md)
  The name of the application to display in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](./applicationversion.md)
  The version information to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](./version.md)
  The version number to display in the About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey/credits)*