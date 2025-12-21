# performFileOperation(_:source:destination:files:tag:)

**Framework**: AppKit  
**Kind**: method

Performs a file operation on a set of files in a particular directory.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func performFileOperation(_ operation: NSWorkspace.FileOperationName, source: String, destination: String, files: [Any], tag: UnsafeMutablePointer<Int>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation succeeded; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Some operations—such as moving, copying, and linking files—require a destination directory to be specified. If not, `destination` should be the empty string (`@""`). Before this method returns, it posts an [`didPerformFileOperationNotification`](nsworkspace/didperformfileoperationnotification.md) to the `NSWorkspace` object’s notification center.

It is safe to call this method from any thread of your app.

## Parameters

- `operation`: The file operation to perform. The possible values for this parameter are described in  .
- `source`: The full path to the directory containing the files on which to operate.
- `destination`: The full path to the destination directory of the operation.
- `files`: An array of   objects specifying the names of the files and directories to be manipulated. Each string must not contain any path information other than the name of the file or directory. In other words, all of the files and directories must be located in the source directory and not in one if its subdirectories.
- `tag`: On input, a integer variable; on return, this variable contains a negative integer if the operation fails, 0 if the operation was performed synchronously and succeeded, or a positive integer if the operation was performed asynchronously. If the value is a positive integer, the value is a tag that identifies the requested file operation.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/performfileoperation(_:source:destination:files:tag:))*