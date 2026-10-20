# applicationName

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The name of the application to display in the About panel.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let applicationName: NSApplication.AboutPanelOptionKey
```

```c
extern NSAboutPanelOptionKey const NSAboutPanelOptionApplicationName;
```

#### Discussion

The value of this key is an [`NSString`](../../../Foundation/nsstring.md) object containing the app’s name. If you do not specify this key, AppKit uses the value of the `CFBundleName` key from the app’s `Info.plist` file. If neither is found, AppKit uses the name of the app’s process.

## See Also

### Option Keys
- [static let applicationIcon: NSApplication.AboutPanelOptionKey](./applicationicon.md)
  The icon to display for the app in the About panel.
- [static let applicationVersion: NSApplication.AboutPanelOptionKey](./applicationversion.md)
  The version information to display in the About panel.
- [static let credits: NSApplication.AboutPanelOptionKey](./credits.md)
  The credits string to display in the About panel.
- [static let version: NSApplication.AboutPanelOptionKey](./version.md)
  The version number to display in the About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/aboutpaneloptionkey/applicationname)*