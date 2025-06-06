# activeApplication()

**Framework**: AppKit  
**Kind**: method

Returns a dictionary with information about the current active app.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func activeApplication() -> [AnyHashable : Any]?
```

#### Return Value

A dictionary with information about the app. The dictionary contains as many of the keys described in [`Deprecated Symbols`](deprecated-symbols.md) as are available.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/activeapplication())*