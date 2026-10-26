# noteFileSystemChanged

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the `NSWorkspace` object that the file system has changed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use the FSEvents API described in `FSEvents` instead.

## Declaration

```objc
- (void) noteFileSystemChanged;
```

#### Discussion

The `NSWorkspace` object then gets the status of all the files and directories it is interested in and updates itself appropriately. This method is used by many objects that write or delete files.

The `NSDocument` and `NSSavePanel` objects use this method when saving a file. If you create a file directly, you should call [`noteFileSystemChanged`](./notefilesystemchanged.md) so that the Finder can update the folder if it is open.

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
- [func launchApplication(withBundleIdentifier: String, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifier: AutoreleasingUnsafeMutablePointer<NSNumber?>?) -> Bool](./launchapplication%28withbundleidentifier,options,additionaleventparamdescriptor,launchidentifier%29.md)
  Launches the app corresponding to the specified `bundleIdentifier`.
- [func open([URL], withAppBundleIdentifier: String?, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifiers: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](./open%28_,withappbundleidentifier,options,additionaleventparamdescriptor,launchidentifiers%29.md)
  Opens one or more files from an array of URLs.
- [- openTempFile:](./opentempfile_.md)
  Opens the specified temporary file using the default app for its type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/notefilesystemchanged)*