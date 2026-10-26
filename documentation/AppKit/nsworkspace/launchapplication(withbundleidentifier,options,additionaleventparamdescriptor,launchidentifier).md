# launchApplication(withBundleIdentifier:options:additionalEventParamDescriptor:launchIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Launches the app corresponding to the specified `bundleIdentifier`.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`openApplication(at:configuration:completionHandler:)`](./openapplication%28at,configuration,completionhandler%29.md) instead.

## Declaration

```swift
func launchApplication(withBundleIdentifier bundleIdentifier: String, options: NSWorkspace.LaunchOptions = [], additionalEventParamDescriptor descriptor: NSAppleEventDescriptor?, launchIdentifier identifier: AutoreleasingUnsafeMutablePointer<NSNumber?>?) -> Bool
```

```objc
- (BOOL) launchAppWithBundleIdentifier:(NSString *) bundleIdentifier options:(NSWorkspaceLaunchOptions) options additionalEventParamDescriptor:(NSAppleEventDescriptor *) descriptor launchIdentifier:(NSNumber **) identifier;
```

#### Return Value

[`true`](../../Swift/true.md) if the app was found and launched; otherwise, [`false`](../../Swift/false.md).

#### Discussion

It is safe to call this method from any thread of your app.

## Parameters

- `bundleIdentifier`: A bundle identifier string. This value corresponds to the value in the `CFBundleIdentifier` key of the app’s `Info.plist` file. For example, the bundle identifier of the TextEdit app is `com.apple.TextEdit`.
- `options`: Options to use when launching the app. Values for this parameter are described in [`NSWorkspace.LaunchOptions`](./launchoptions.md).
- `descriptor`: Additional options specified in an AppleEvent-style descriptor. For example, you could use this parameter to specify additional documents to open when the app is launched.
- `identifier`: The `launchIdentifiers` are currently unused, and you should pass `NULL`.

## See Also

### Deprecated methods
- [func open(URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./open%28_,options,configuration%29.md)
- [func open([URL], withApplicationAt: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./open%28_,withapplicationat,options,configuration%29.md)
- [func openFile(String) -> Bool](./openfile%28_%29.md)
  Opens the specified file specified using the default app associated with its type.
- [func openFile(String, withApplication: String?) -> Bool](./openfile%28_,withapplication%29.md)
  Opens a file using the specified app.
- [func openFile(String, withApplication: String?, andDeactivate: Bool) -> Bool](./openfile%28_,withapplication,anddeactivate%29.md)
  Opens the specified file and optionally deactivates the sending app.
- [func openFile(String, from: NSImage?, at: NSPoint, in: NSView?) -> Bool](./openfile%28_,from,at,in%29.md)
  Opens a file using the default app for its type and animates the action using a custom icon.
- [func launchApplication(String) -> Bool](./launchapplication%28_%29.md)
  Launches the specified app.
- [func launchApplication(String, showIcon: Bool, autolaunch: Bool) -> Bool](./launchapplication%28_,showicon,autolaunch%29.md)
  Launches the specified app using additional options.
- [func launchApplication(at: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./launchapplication%28at,options,configuration%29.md)
  Launches the app at the specified URL.
- [func performFileOperation(NSWorkspace.FileOperationName, source: String, destination: String, files: [Any], tag: UnsafeMutablePointer<Int>?) -> Bool](./performfileoperation%28_,source,destination,files,tag%29.md)
  Performs a file operation on a set of files in a particular directory.
- [func fullPath(forApplication: String) -> String?](./fullpath%28forapplication%29.md)
  Returns the full path for the specified app.
- [func absolutePathForApplication(withBundleIdentifier: String) -> String?](./absolutepathforapplication%28withbundleidentifier%29.md)
  Returns the absolute file system path of an app bundle.
- [func open([URL], withAppBundleIdentifier: String?, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifiers: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](./open%28_,withappbundleidentifier,options,additionaleventparamdescriptor,launchidentifiers%29.md)
  Opens one or more files from an array of URLs.
- [func mountedRemovableMedia() -> [Any]?](./mountedremovablemedia%28%29.md)
  Returns the full pathnames of all currently mounted removable disks.
- [func mountedLocalVolumePaths() -> [Any]?](./mountedlocalvolumepaths%28%29.md)
  Returns the mount points of all local volumes, not just the removable ones returned by [`mountedRemovableMedia()`](./mountedremovablemedia%28%29.md).
- [- openTempFile:](./opentempfile_.md)
  Opens the specified temporary file using the default app for its type.
- [- findApplications](./findapplications.md)
  Examines all apps and updates the records of registered services and file types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchapplication(withbundleidentifier:options:additionaleventparamdescriptor:launchidentifier:))*