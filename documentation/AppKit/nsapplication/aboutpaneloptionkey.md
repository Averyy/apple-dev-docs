# NSApplication.AboutPanelOptionKey

**Framework**: AppKit  
**Kind**: struct

Keys to include in the options dictionary when displaying an About panel.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AboutPanelOptionKey
```

## Topics

### Option Keys
- [static let applicationIcon: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationName: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationname.md)
  The name of the application to display in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/applicationversion.md)
  The version information to display in the About panel.
- [static let credits: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/credits.md)
  The credits string to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey/version.md)
  The version number to display in the About panel.
### Initializers
- [init(rawValue: String)](nsapplication/aboutpaneloptionkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func orderFrontColorPanel(Any?)](nsapplication/orderfrontcolorpanel(_:).md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](nsapplication/orderfrontstandardaboutpanel(_:).md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](nsapplication/orderfrontstandardaboutpanel(options:).md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](nsapplication/orderfrontcharacterpalette(_:).md)
  Opens the character palette.
- [func runPageLayout(Any?)](nsapplication/runpagelayout(_:).md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey)*