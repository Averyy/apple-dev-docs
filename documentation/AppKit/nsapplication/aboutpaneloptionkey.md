# NSApplication.AboutPanelOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys to include in the options dictionary when displaying an About panel.

**Availability**:
- macOS

## Declaration

```swift
struct AboutPanelOptionKey
```

```c
typedef NSString * NSAboutPanelOptionKey;
```

## Topics

### Option Keys
- [static let applicationIcon: NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey/applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationName: NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey/applicationname.md)
  The name of the application to display in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey/applicationversion.md)
  The version information to display in the About panel.
- [static let credits: NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey/credits.md)
  The credits string to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey/version.md)
  The version number to display in the About panel.
### Initializers
- [init(rawValue: String)](./aboutpaneloptionkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Panels
- [func orderFrontColorPanel(Any?)](./orderfrontcolorpanel%28_%29.md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](./orderfrontstandardaboutpanel%28_%29.md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](./orderfrontstandardaboutpanel%28options%29.md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](./orderfrontcharacterpalette%28_%29.md)
  Opens the character palette.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey)*