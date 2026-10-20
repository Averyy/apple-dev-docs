# withoutAddingToRecents

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Do not add the app or documents to the Recents menu.

**Availability**:
- macOS 10.3+ - Deprecated in 11.0

> **Deprecated**: Use -[NSWorkspaceOpenConfiguration setAddsToRecentItems:YES] instead.

## Declaration

```swift
static var withoutAddingToRecents: NSWorkspace.LaunchOptions { get }
```

```c
NSWorkspaceLaunchWithoutAddingToRecents
```

## See Also

### Deprecated symbols
- [static var andPrint: NSWorkspace.LaunchOptions](./andprint.md)
  Print items instead of opening them.
- [static var withErrorPresentation: NSWorkspace.LaunchOptions](./witherrorpresentation.md)
  Display an error panel to the user if a failure occurs.
- [static var inhibitingBackgroundOnly: NSWorkspace.LaunchOptions](./inhibitingbackgroundonly.md)
  Causes launch to fail if the target is background-only.
- [static var withoutActivation: NSWorkspace.LaunchOptions](./withoutactivation.md)
  Launch the app but do not bring it into the foreground.
- [static var async: NSWorkspace.LaunchOptions](./async.md)
  Launch the app and return the results asynchronously.
- [static var allowingClassicStartup: NSWorkspace.LaunchOptions](./allowingclassicstartup.md)
  Start up the Classic compatibility environment, if it is required by the app.
- [static var preferringClassic: NSWorkspace.LaunchOptions](./preferringclassic.md)
  Force the app to launch in the Classic compatibility environment.
- [static var newInstance: NSWorkspace.LaunchOptions](./newinstance.md)
  Create a new instance of the app, even if one is already running.
- [static var andHide: NSWorkspace.LaunchOptions](./andhide.md)
  Tell the app to hide itself as soon as it finishes launching.
- [static var andHideOthers: NSWorkspace.LaunchOptions](./andhideothers.md)
  Hide all apps except the newly launched one.
- [static var `default`: NSWorkspace.LaunchOptions](./default.md)
  Launch the app asynchronously and launch it in the Classic environment, if required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchoptions/withoutaddingtorecents)*