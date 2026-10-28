# performFileOperation(_:source:destination:files:tag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs a file operation on a set of files in a particular directory.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
func performFileOperation(_ operation: NSWorkspace.FileOperationName, source: String, destination: String, files: [Any], tag: UnsafeMutablePointer<Int>?) -> Bool
```

```objc
- (BOOL) performFileOperation:(NSWorkspaceFileOperationName) operation source:(NSString *) source destination:(NSString *) destination files:(NSArray *) files tag:(NSInteger *) tag;
```

## Return Value

[`true`](../../Swift/true.md) if the operation succeeded; otherwise, [`false`](../../Swift/false.md).

## Discussion

Some operations—such as moving, copying, and linking files—require a destination directory to be specified. If not, `destination` should be the empty string (`@""`). Before this method returns, it posts an [`didPerformFileOperationNotification`](./didperformfileoperationnotification.md) to the `NSWorkspace` object’s notification center.

It is safe to call this method from any thread of your app.

## Parameters

- `operation`: The file operation to perform. The possible values for this parameter are described in `File Operations`.
- `source`: The full path to the directory containing the files on which to operate.
- `destination`: The full path to the destination directory of the operation.
- `files`: An array of [`NSString`](../../Foundation/nsstring.md) objects specifying the names of the files and directories to be manipulated. Each string must not contain any path information other than the name of the file or directory. In other words, all of the files and directories must be located in the source directory and not in one if its subdirectories.
- `tag`: On input, a integer variable; on return, this variable contains a negative integer if the operation fails, 0 if the operation was performed synchronously and succeeded, or a positive integer if the operation was performed asynchronously. If the value is a positive integer, the value is a tag that identifies the requested file operation.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/performfileoperation(_:source:destination:files:tag:))*