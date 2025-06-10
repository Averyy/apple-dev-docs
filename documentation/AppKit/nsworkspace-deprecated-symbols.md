# Deprecated Symbols

**Framework**: AppKit

Review unsupported symbols and their replacements.

#### Overview

The table below describes keys for an `NSDictionary` object containing information about an app. This dictionary is returned by [`activeApplication()`](nsworkspace/activeapplication().md) and [`launchedApplications`](nsworkspace/launchedapplications.md), and is also provided in the `userInfo` of `NSWorkspace` notifications for app launch and termination.

Note that these constants are considered legacy.

> **Note**:  It is strongly suggested that you use the `NSWorkspace` class’s [`runningApplications`](nsworkspace/runningapplications.md) method and the [`NSRunningApplication`](nsrunningapplication.md) class to retrieve this information in apps target macOS 10.6 and later, rather than the [`activeApplication()`](nsworkspace/activeapplication().md) and [`launchedApplications`](nsworkspace/launchedapplications.md) methods.

| Key | Value |
| --- | --- |
| `@"NSApplicationPath"` | The full path to the app, as a `NSString` object. |
| `@"NSApplicationName"` | The app’s name, as an `NSString` object. |
| `@"NSApplicationBundleIdentifier"` | The app’s bundle identifier, as an `NSString` object. |
| `@"NSApplicationProcessIdentifier"` | The app’s process ID, as an `NSNumber` object. |
| `@"NSApplicationProcessSerialNumberHigh"` | The high long of the process serial number (PSN), as an `NSNumber` object. |
| `@"NSApplicationProcessSerialNumberLow"` | The low long of the process serial number (PSN), as an `NSNumber` object. |

## Topics

### Methods
- [func open(URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](nsworkspace/open(_:options:configuration:).md)
- [func open([URL], withApplicationAt: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](nsworkspace/open(_:withapplicationat:options:configuration:).md)
- [func openFile(String) -> Bool](nsworkspace/openfile(_:).md)
  Opens the specified file specified using the default app associated with its type.
- [func openFile(String, withApplication: String?) -> Bool](nsworkspace/openfile(_:withapplication:).md)
  Opens a file using the specified app.
- [func openFile(String, withApplication: String?, andDeactivate: Bool) -> Bool](nsworkspace/openfile(_:withapplication:anddeactivate:).md)
  Opens the specified file and optionally deactivates the sending app.
- [func openFile(String, from: NSImage?, at: NSPoint, in: NSView?) -> Bool](nsworkspace/openfile(_:from:at:in:).md)
  Opens a file using the default app for its type and animates the action using a custom icon.
- [func launchApplication(String) -> Bool](nsworkspace/launchapplication(_:).md)
  Launches the specified app.
- [func launchApplication(String, showIcon: Bool, autolaunch: Bool) -> Bool](nsworkspace/launchapplication(_:showicon:autolaunch:).md)
  Launches the specified app using additional options.
- [func launchApplication(at: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](nsworkspace/launchapplication(at:options:configuration:).md)
  Launches the app at the specified URL.
- [func performFileOperation(NSWorkspace.FileOperationName, source: String, destination: String, files: [Any], tag: UnsafeMutablePointer<Int>?) -> Bool](nsworkspace/performfileoperation(_:source:destination:files:tag:).md)
  Performs a file operation on a set of files in a particular directory.
- [func fullPath(forApplication: String) -> String?](nsworkspace/fullpath(forapplication:).md)
  Returns the full path for the specified app.
- [func absolutePathForApplication(withBundleIdentifier: String) -> String?](nsworkspace/absolutepathforapplication(withbundleidentifier:).md)
  Returns the absolute file system path of an app bundle.
- [func launchApplication(withBundleIdentifier: String, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifier: AutoreleasingUnsafeMutablePointer<NSNumber?>?) -> Bool](nsworkspace/launchapplication(withbundleidentifier:options:additionaleventparamdescriptor:launchidentifier:).md)
  Launches the app corresponding to the specified `bundleIdentifier`.
- [func open([URL], withAppBundleIdentifier: String?, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifiers: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](nsworkspace/open(_:withappbundleidentifier:options:additionaleventparamdescriptor:launchidentifiers:).md)
  Opens one or more files from an array of URLs.
- [func mountedRemovableMedia() -> [Any]?](nsworkspace/mountedremovablemedia.md)
  Returns the full pathnames of all currently mounted removable disks.
- [func mountedLocalVolumePaths() -> [Any]?](nsworkspace/mountedlocalvolumepaths.md)
  Returns the mount points of all local volumes, not just the removable ones returned by [`mountedRemovableMedia()`](nsworkspace/mountedremovablemedia().md).
- [func activeApplication() -> [AnyHashable : Any]?](nsworkspace/activeapplication.md)
  Returns a dictionary with information about the current active app.
- [func icon(forFileType: String) -> NSImage](nsworkspace/icon(forfiletype:).md)
  Returns an image containing the icon for files of the specified type.
### Types
- [NSWorkspace.LaunchOptions](nsworkspace/launchoptions.md)
  Constants specifying how you want to launch an app
- [NSWorkspace.LaunchConfigurationKey](nsworkspace/launchconfigurationkey.md)
  The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](nsworkspace/launchapplication(at:options:configuration:).md) method.  Each key is optional, and if omitted, default behavior is applied.
- [NSWorkspace.FileOperationName](nsworkspace/fileoperationname.md)
  These constants specify different types of file operations used by [`performFileOperation(_:source:destination:files:tag:)`](nsworkspace/performfileoperation(_:source:destination:files:tag:).md).
### Constants
- [class let applicationUserInfoKey: String](nsworkspace/applicationuserinfokey.md)
  The value corresponding to this key is an instance of [`NSRunningApplication`](nsrunningapplication.md) that reflects the affected app.
### Notifications
- [class let didPerformFileOperationNotification: NSNotification.Name](nsworkspace/didperformfileoperationnotification.md)
  Posted when a file operation has been performed in the receiving app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace-deprecated-symbols)*