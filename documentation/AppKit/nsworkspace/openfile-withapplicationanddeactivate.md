# openFile(_:withApplication:andDeactivate:)

**Framework**: AppKit  
**Kind**: method

Opens the specified file and optionally deactivates the sending app.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func openFile(_ fullPath: String, withApplication appName: String?, andDeactivate flag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the file was successfully opened; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The  `appName` parameter need not be specified with a full path and, in the case of an app wrapper, may be specified with or without the `.app` extension, as described in [`Use of .app Extension`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/AppExtensions.html#//apple_ref/doc/uid/20001003). If `appName` is `nil`, the default app for the file’s type is used.

It is safe to call this method from any thread in your app in macOS 10.6 and later.

## Parameters

- `fullPath`: The full path to the file.
- `appName`: The name of the app to use when opening the file.
- `flag`: If YES, the sending app is deactivated before the request is sent, allowing the opening app to become the active app.

## See Also

- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func open(URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](nsworkspace/open(_:options:configuration:).md)
- [func open([URL], withApplicationAt: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](nsworkspace/open(_:withapplicationat:options:configuration:).md)
- [func openFile(String) -> Bool](nsworkspace/openfile(_:).md)
  Opens the specified file specified using the default app associated with its type.
- [func openFile(String, withApplication: String?) -> Bool](nsworkspace/openfile(_:withapplication:).md)
  Opens a file using the specified app.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openfile(_:withapplication:anddeactivate:))*