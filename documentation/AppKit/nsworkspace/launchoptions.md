# NSWorkspace.LaunchOptions

**Framework**: AppKit  
**Kind**: struct

Constants specifying how you want to launch an app

**Availability**:
- macOS ?+

## Declaration

```swift
struct LaunchOptions
```

## Topics

### Options
- [static var andPrint: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/andprint.md)
  Print items instead of opening them.
- [static var withErrorPresentation: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/witherrorpresentation.md)
  Display an error panel to the user if a failure occurs.
- [static var inhibitingBackgroundOnly: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/inhibitingbackgroundonly.md)
  Causes launch to fail if the target is background-only.
- [static var withoutAddingToRecents: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/withoutaddingtorecents.md)
  Do not add the app or documents to the Recents menu.
- [static var withoutActivation: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/withoutactivation.md)
  Launch the app but do not bring it into the foreground.
- [static var async: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/async.md)
  Launch the app and return the results asynchronously.
- [static var allowingClassicStartup: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/allowingclassicstartup.md)
  Start up the Classic compatibility environment, if it is required by the app.
- [static var preferringClassic: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/preferringclassic.md)
  Force the app to launch in the Classic compatibility environment.
- [static var newInstance: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/newinstance.md)
  Create a new instance of the app, even if one is already running.
- [static var andHide: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/andhide.md)
  Tell the app to hide itself as soon as it finishes launching.
- [static var andHideOthers: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/andhideothers.md)
  Hide all apps except the newly launched one.
- [static var `default`: NSWorkspace.LaunchOptions](nsworkspace/launchoptions/default.md)
  Launch the app asynchronously and launch it in the Classic environment, if required.
### Initializers
- [init(rawValue: UInt)](nsworkspace/launchoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey.md)
  The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](nsworkspace/launchapplication(at:options:configuration:).md) method.  Each key is optional, and if omitted, default behavior is applied.
- [NSWorkspace.FileOperationName](nsworkspace/fileoperationname.md)
  These constants specify different types of file operations used by [`performFileOperation(_:source:destination:files:tag:)`](nsworkspace/performfileoperation(_:source:destination:files:tag:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchoptions)*