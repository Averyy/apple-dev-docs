# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

The table below describes keys for an `NSDictionary` object containing information about an app. This dictionary is returned by [`activeApplication()`](./nsworkspace/activeapplication%28%29.md) and [`launchedApplications`](./nsworkspace/launchedapplications.md), and is also provided in the `userInfo` of `NSWorkspace` notifications for app launch and termination.

Note that these constants are considered legacy.

> **Note**:  It is strongly suggested that you use the `NSWorkspace` class’s [`runningApplications`](./nsworkspace/runningapplications.md) method and the [`NSRunningApplication`](./nsrunningapplication.md) class to retrieve this information in apps target macOS 10.6 and later, rather than the [`activeApplication()`](./nsworkspace/activeapplication%28%29.md) and [`launchedApplications`](./nsworkspace/launchedapplications.md) methods.

| Key | Value |
| --- | --- |
| `@"NSApplicationPath"` | The full path to the app, as a `NSString` object. |
| `@"NSApplicationName"` | The app’s name, as an `NSString` object. |
| `@"NSApplicationBundleIdentifier"` | The app’s bundle identifier, as an `NSString` object. |
| `@"NSApplicationProcessIdentifier"` | The app’s process ID, as an `NSNumber` object. |
| `@"NSApplicationProcessSerialNumberHigh"` | The high long of the process serial number (PSN), as an `NSNumber` object. |
| `@"NSApplicationProcessSerialNumberLow"` | The low long of the process serial number (PSN), as an `NSNumber` object. |

## Topics

### Deprecated methods
- [func open(URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./nsworkspace/open%28_,options,configuration%29.md)
- [func open([URL], withApplicationAt: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./nsworkspace/open%28_,withapplicationat,options,configuration%29.md)
- [func openFile(String) -> Bool](./nsworkspace/openfile%28_%29.md)
  Opens the specified file specified using the default app associated with its type.
- [func openFile(String, withApplication: String?) -> Bool](./nsworkspace/openfile%28_,withapplication%29.md)
  Opens a file using the specified app.
- [func openFile(String, withApplication: String?, andDeactivate: Bool) -> Bool](./nsworkspace/openfile%28_,withapplication,anddeactivate%29.md)
  Opens the specified file and optionally deactivates the sending app.
- [func openFile(String, from: NSImage?, at: NSPoint, in: NSView?) -> Bool](./nsworkspace/openfile%28_,from,at,in%29.md)
  Opens a file using the default app for its type and animates the action using a custom icon.
- [func launchApplication(String) -> Bool](./nsworkspace/launchapplication%28_%29.md)
  Launches the specified app.
- [func launchApplication(String, showIcon: Bool, autolaunch: Bool) -> Bool](./nsworkspace/launchapplication%28_,showicon,autolaunch%29.md)
  Launches the specified app using additional options.
- [func launchApplication(at: URL, options: NSWorkspace.LaunchOptions, configuration: [NSWorkspace.LaunchConfigurationKey : Any]) throws -> NSRunningApplication](./nsworkspace/launchapplication%28at,options,configuration%29.md)
  Launches the app at the specified URL.
- [func performFileOperation(NSWorkspace.FileOperationName, source: String, destination: String, files: [Any], tag: UnsafeMutablePointer<Int>?) -> Bool](./nsworkspace/performfileoperation%28_,source,destination,files,tag%29.md)
  Performs a file operation on a set of files in a particular directory.
- [func fullPath(forApplication: String) -> String?](./nsworkspace/fullpath%28forapplication%29.md)
  Returns the full path for the specified app.
- [func absolutePathForApplication(withBundleIdentifier: String) -> String?](./nsworkspace/absolutepathforapplication%28withbundleidentifier%29.md)
  Returns the absolute file system path of an app bundle.
- [func launchApplication(withBundleIdentifier: String, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifier: AutoreleasingUnsafeMutablePointer<NSNumber?>?) -> Bool](./nsworkspace/launchapplication%28withbundleidentifier,options,additionaleventparamdescriptor,launchidentifier%29.md)
  Launches the app corresponding to the specified `bundleIdentifier`.
- [func open([URL], withAppBundleIdentifier: String?, options: NSWorkspace.LaunchOptions, additionalEventParamDescriptor: NSAppleEventDescriptor?, launchIdentifiers: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> Bool](./nsworkspace/open%28_,withappbundleidentifier,options,additionaleventparamdescriptor,launchidentifiers%29.md)
  Opens one or more files from an array of URLs.
- [func mountedRemovableMedia() -> [Any]?](./nsworkspace/mountedremovablemedia%28%29.md)
  Returns the full pathnames of all currently mounted removable disks.
- [func mountedLocalVolumePaths() -> [Any]?](./nsworkspace/mountedlocalvolumepaths%28%29.md)
  Returns the mount points of all local volumes, not just the removable ones returned by [`mountedRemovableMedia()`](./nsworkspace/mountedremovablemedia%28%29.md).
- [func activeApplication() -> [AnyHashable : Any]?](./nsworkspace/activeapplication%28%29.md)
  Returns a dictionary with information about the current active app.
- [func icon(forFileType: String) -> NSImage](./nsworkspace/icon%28forfiletype%29.md)
  Returns an image containing the icon for files of the specified type.
- [func type(ofFile: String) throws -> String](./nsworkspace/type%28offile%29.md)
  Returns the uniform type identifier of the specified file, if it can be determined.
- [func localizedDescription(forType: String) -> String?](./nsworkspace/localizeddescription%28fortype%29.md)
  Returns the localized description for the specified Uniform Type Identifier (UTI).
- [func preferredFilenameExtension(forType: String) -> String?](./nsworkspace/preferredfilenameextension%28fortype%29.md)
  Returns the preferred filename extension for the specified Uniform Type Identifier (UTI).
- [func filenameExtension(String, isValidForType: String) -> Bool](./nsworkspace/filenameextension%28_,isvalidfortype%29.md)
  Returns whether the specified filename extension is appropriate for the Uniform Type Identifier (UTI).
- [func type(String, conformsToType: String) -> Bool](./nsworkspace/type%28_,conformstotype%29.md)
  Returns a Boolean indicating that the first Uniform Type Identifier (UTI) conforms to the second UTI.
- [func getInfoForFile(String, application: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./nsworkspace/getinfoforfile%28_,application,type%29.md)
  Retrieves information about the specified file.
- [- openTempFile:](./nsworkspace/opentempfile_.md)
  Opens the specified temporary file using the default app for its type.
- [- findApplications](./nsworkspace/findapplications.md)
  Examines all apps and updates the records of registered services and file types.
- [- noteUserDefaultsChanged](./nsworkspace/noteuserdefaultschanged.md)
  Informs the `NSWorkspace` object that the defaults database has changed.
- [- slideImage:from:to:](./nsworkspace/slideimage_from_to_.md)
  Animates a sliding image from one point to another.
- [- checkForRemovableMedia](./nsworkspace/checkforremovablemedia.md)
  Polls the system’s drives for any disks that have been inserted but not yet mounted.
- [- noteFileSystemChanged](./nsworkspace/notefilesystemchanged.md)
  Informs the `NSWorkspace` object that the file system has changed.
- [- fileSystemChanged](./nsworkspace/filesystemchanged.md)
  Returns a Boolean value indicating whether a change to the file system has been registered with a [`noteFileSystemChanged`](./nsworkspace/notefilesystemchanged.md) message since the last [`fileSystemChanged`](./nsworkspace/filesystemchanged.md) message.
- [- userDefaultsChanged](./nsworkspace/userdefaultschanged.md)
  Returns a Boolean value indicating whether a change to the defaults database has been registered with a [`noteUserDefaultsChanged`](./nsworkspace/noteuserdefaultschanged.md) message since the last [`userDefaultsChanged`](./nsworkspace/userdefaultschanged.md) message.
- [- mountNewRemovableMedia](./nsworkspace/mountnewremovablemedia.md)
  Returns the full pathnames of any newly mounted disks.
- [- launchedApplications](./nsworkspace/launchedapplications.md)
  Returns an array of dictionaries, one entry for each running app.
### Deprecated types
- [NSWorkspace.LaunchOptions](./nsworkspace/launchoptions.md)
  Constants specifying how you want to launch an app
- [NSWorkspace.LaunchConfigurationKey](./nsworkspace/launchconfigurationkey.md)
  The following keys can be used in the configuration dictionary of the [`launchApplication(at:options:configuration:)`](./nsworkspace/launchapplication%28at,options,configuration%29.md) method.  Each key is optional, and if omitted, default behavior is applied.
- [NSWorkspace.FileOperationName](./nsworkspace/fileoperationname.md)
  Constants that define types of file operations.
### Deprecated constants
- [class let applicationUserInfoKey: String](./nsworkspace/applicationuserinfokey.md)
  The value corresponding to this key is an instance of [`NSRunningApplication`](./nsrunningapplication.md) that reflects the affected app.
- [NSPlainFileType](./nsplainfiletype.md)
  Plain (untyped) file.
- [NSDirectoryFileType](./nsdirectoryfiletype.md)
  Directory.
- [NSApplicationFileType](./nsapplicationfiletype.md)
  Cocoa app.
- [NSFilesystemFileType](./nsfilesystemfiletype.md)
  File-system mount point.
- [NSShellCommandFileType](./nsshellcommandfiletype.md)
  Executable shell command.
### Deprecated notifications
- [class let didPerformFileOperationNotification: NSNotification.Name](./nsworkspace/didperformfileoperationnotification.md)
  Posted when a file operation has been performed in the receiving app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace-deprecated-symbols)*