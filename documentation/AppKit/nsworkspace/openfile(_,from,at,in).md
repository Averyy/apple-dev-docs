# openFile(_:from:at:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Opens a file using the default app for its type and animates the action using a custom icon.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`open(_:)`](./open%28_%29.md) instead.

## Declaration

```swift
func openFile(_ fullPath: String, from image: NSImage?, at point: NSPoint, in view: NSView?) -> Bool
```

```objc
- (BOOL) openFile:(NSString *) fullPath fromImage:(NSImage *) image at:(NSPoint) point inView:(NSView *) view;
```

## Return Value

[`true`](../../Swift/true.md) if the file was successfully opened; otherwise, [`false`](../../Swift/false.md).

## Discussion

Use of this method is discouraged. The method currently provides the same behavior as the [`openFile(_:)`](./openfile%28_%29.md) method. The Finder provides an animation before opening the file to give the user feedback that the file is to be opened. To provide this animation, `anImage` should contain an icon for the file, and its image should be displayed at `point`, specified in the coordinates of `aView`.

The sending app is deactivated before the request is sent.

It is safe to call this method from any thread in your app in macOS 10.6 and later.

## Parameters

- `fullPath`: The full path to the file.
- `image`: The icon for the file.
- `point`: The point in `aView` at which to display the icon.
- `view`: The view in which to display the icon.

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
- [func launchApplication(withBundleIdentifier: String, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifier: AutoreleasingUnsafeMutablePointer<NSNumber?>?) -> Bool](./launchapplication%28withbundleidentifier,options,additionaleventparamdescriptor,launchidentifier%29.md)
  Launches the app corresponding to the specified `bundleIdentifier`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openfile(_:from:at:in:))*