# launchApplication(_:showIcon:autolaunch:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Launches the specified app using additional options.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Use [`openApplication(at:configuration:completionHandler:)`](./openapplication%28at,configuration,completionhandler%29.md) instead.

## Declaration

```swift
func launchApplication(_ appName: String, showIcon: Bool, autolaunch: Bool) -> Bool
```

```objc
- (BOOL) launchApplication:(NSString *) appName showIcon:(BOOL) showIcon autolaunch:(BOOL) autolaunch;
```

#### Return Value

[`true`](../../Swift/true.md) if the app was successfully launched or was already running; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Use of this method is discouraged. Its current behavior is the same as the [`launchApplication(_:)`](./launchapplication%28_%29.md) method.

Returns [`true`](../../Swift/true.md) if the app is successfully launched or already running, and [`false`](../../Swift/false.md) if it can’t be launched.

Before this method begins, it posts an [`willLaunchApplicationNotification`](./willlaunchapplicationnotification.md) to the `NSWorkspace` object’s notification center. When the operation is complete, it posts an [`didLaunchApplicationNotification`](./didlaunchapplicationnotification.md).

It is safe to call this method from any thread in your app in macOS 10.6 and later.

## Parameters

- `appName`: The name of the app to open.
- `showIcon`: If [`false`](../../Swift/false.md), the app’s icon is not placed on the screen. (The icon still exists, though.)
- `autolaunch`: If [`true`](../../Swift/true.md), the autolaunch default is set as though the specified app were autolaunched at startup.

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
- [func launchApplication(at: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./launchapplication%28at,options,configuration%29.md)
  Launches the app at the specified URL.
- [func performFileOperation(NSWorkspace.FileOperationName, source: String, destination: String, files: [Any], tag: UnsafeMutablePointer<Int>?) -> Bool](./performfileoperation%28_,source,destination,files,tag%29.md)
  Performs a file operation on a set of files in a particular directory.
- [func fullPath(forApplication: String) -> String?](./fullpath%28forapplication%29.md)
  Returns the full path for the specified app.
- [func absolutePathForApplication(withBundleIdentifier: String) -> String?](./absolutepathforapplication%28withbundleidentifier%29.md)
  Returns the absolute file system path of an app bundle.
- [func launchApplication(withBundleIdentifier: String, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifier: AutoreleasingUnsafeMutablePointer<NSNumber?>?) -> Bool](./launchapplication%28withbundleidentifier,options,additionaleventparamdescriptor,launchidentifier%29.md)
  Launches the app corresponding to the specified `bundleIdentifier`.
- [func open([URL], withAppBundleIdentifier: String?, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifiers: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](./open%28_,withappbundleidentifier,options,additionaleventparamdescriptor,launchidentifiers%29.md)
  Opens one or more files from an array of URLs.
- [func mountedRemovableMedia() -> [Any]?](./mountedremovablemedia%28%29.md)
  Returns the full pathnames of all currently mounted removable disks.
- [func mountedLocalVolumePaths() -> [Any]?](./mountedlocalvolumepaths%28%29.md)
  Returns the mount points of all local volumes, not just the removable ones returned by [`mountedRemovableMedia()`](./mountedremovablemedia%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/launchapplication(_:showicon:autolaunch:))*