# NSWorkspace

**Framework**: AppKit  
**Kind**: class

A workspace that can launch other apps and perform a variety of file-handling services.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSWorkspace
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Overview

There is one shared [`NSWorkspace`](nsworkspace.md) object per app. You use the class method [`shared`](nsworkspace/shared.md) to access it. For example, the following statement uses an [`NSWorkspace`](nsworkspace.md) object to request that a file be opened in the TextEdit app:

You can use the workspace object to:

- Open, manipulate, and get information about files and devices.
- Track changes to the file system, devices, and the user database.
- Get and set Finder information for files.
- Launch apps.

## Topics

### Accessing the Shared Workspace
- [class var shared: NSWorkspace](nsworkspace/shared.md)
  The shared workspace object.
### Accessing the Workspace Notification Center
- [var notificationCenter: NotificationCenter](nsworkspace/notificationcenter.md)
  The notification center for workspace notifications.
### Opening URLs
- [func open(URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](nsworkspace/open(_:configuration:completionhandler:).md)
  Opens a URL asynchronously using the provided options.
- [func open([URL], withApplicationAt: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](nsworkspace/open(_:withapplicationat:configuration:completionhandler:).md)
  Opens one or more URLs asynchronously in the specified app using the provided options.
- [func open(URL) -> Bool](nsworkspace/open(_:).md)
  Opens the location at the specified URL.
### Launching and Hiding Apps
- [func openApplication(at: URL, configuration: NSWorkspace.OpenConfiguration, completionHandler: ((NSRunningApplication?, (any Error)?) -> Void)?)](nsworkspace/openapplication(at:configuration:completionhandler:).md)
  Launches the app at the specified URL and asynchronously reports back on the app’s status.
- [func hideOtherApplications()](nsworkspace/hideotherapplications.md)
  Hides all applications other than the sender.
### Managing Open Configurations
- [NSWorkspace.OpenConfiguration](nsworkspace/openconfiguration.md)
  The configuration options for opening URLs or launching apps.
### Manipulating Files
- [func duplicate([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](nsworkspace/duplicate(_:completionhandler:).md)
  Duplicates the specified URLS asynchronously in the same manner as the Finder.
- [func recycle([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](nsworkspace/recycle(_:completionhandler:).md)
  Moves the specified URLs to the trash in the same manner as the Finder.
- [func activateFileViewerSelecting([URL])](nsworkspace/activatefileviewerselecting(_:).md)
  Activates the Finder, and opens one or more windows selecting the specified files.
- [func selectFile(String?, inFileViewerRootedAtPath: String) -> Bool](nsworkspace/selectfile(_:infileviewerrootedatpath:).md)
  Selects the file at the specified path.
### Manipulating Uniform Type Identifier Information
- [func type(ofFile: String) throws -> String](nsworkspace/type(offile:).md)
  Returns the uniform type identifier of the specified file, if it can be determined.
- [func localizedDescription(forType: String) -> String?](nsworkspace/localizeddescription(fortype:).md)
  Returns the localized description for the specified Uniform Type Identifier (UTI).
- [func preferredFilenameExtension(forType: String) -> String?](nsworkspace/preferredfilenameextension(fortype:).md)
  Returns the preferred filename extension for the specified Uniform Type Identifier (UTI).
- [func filenameExtension(String, isValidForType: String) -> Bool](nsworkspace/filenameextension(_:isvalidfortype:).md)
  Returns whether the specified filename extension is appropriate for the Uniform Type Identifier (UTI).
- [func type(String, conformsToType: String) -> Bool](nsworkspace/type(_:conformstotype:).md)
  Returns a Boolean indicating that the first Uniform Type Identifier (UTI) conforms to the second UTI.
### Requesting Information
- [func urlForApplication(toOpen: URL) -> URL?](nsworkspace/urlforapplication(toopen:)-7qkzf.md)
  Returns the URL to the default app to open the specified URL.
- [func urlForApplication(toOpen: UTType) -> URL?](nsworkspace/urlforapplication(toopen:)-95cvp.md)
  Returns the URL to the default app to open the specified content type.
- [func urlForApplication(withBundleIdentifier: String) -> URL?](nsworkspace/urlforapplication(withbundleidentifier:).md)
  Returns the URL to the default app with the specified bundle identifier.
- [func urlsForApplications(toOpen: URL) -> [URL]](nsworkspace/urlsforapplications(toopen:)-ualk.md)
  Returns an array of URLs to all available applications that can open the URL.
- [func urlsForApplications(toOpen: UTType) -> [URL]](nsworkspace/urlsforapplications(toopen:)-60rkm.md)
  Returns an array of URLs to all available applications that can open the specified content type.
- [func urlsForApplications(withBundleIdentifier: String) -> [URL]](nsworkspace/urlsforapplications(withbundleidentifier:).md)
  Returns an array of URLs to all available applications that can open the specified bundle identifier.
- [func getFileSystemInfo(forPath: String, isRemovable: UnsafeMutablePointer<ObjCBool>?, isWritable: UnsafeMutablePointer<ObjCBool>?, isUnmountable: UnsafeMutablePointer<ObjCBool>?, description: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](nsworkspace/getfilesysteminfo(forpath:isremovable:iswritable:isunmountable:description:type:).md)
  Returns information about the file system at the specified path.
- [func isFilePackage(atPath: String) -> Bool](nsworkspace/isfilepackage(atpath:).md)
  Determines whether the specified path is a file package.
- [var frontmostApplication: NSRunningApplication?](nsworkspace/frontmostapplication.md)
  Returns the frontmost app, which is the app that receives key events.
- [var runningApplications: [NSRunningApplication]](nsworkspace/runningapplications.md)
  Returns an array of running apps.
- [var menuBarOwningApplication: NSRunningApplication?](nsworkspace/menubarowningapplication.md)
  Returns the app that owns the currently displayed menu bar.
- [func getInfoForFile(String, application: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](nsworkspace/getinfoforfile(_:application:type:).md)
  Retrieves information about the specified file.
### Setting Default Application Information
- [func setDefaultApplication(at: URL, toOpenFileAt: URL, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopenfileat:completion:).md)
  Sets the default app to use when opening a specific file.
- [func setDefaultApplication(at: URL, toOpen: UTType, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopen:completion:).md)
  Sets the default app to use when opening files of a specific content type.
- [func setDefaultApplication(at: URL, toOpenContentTypeOfFileAt: URL, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopencontenttypeoffileat:completion:).md)
  Sets the default app to use when opening files of a specific content type defined by a file URL.
- [func setDefaultApplication(at: URL, toOpenURLsWithScheme: String, completion: (((any Error)?) -> Void)?)](nsworkspace/setdefaultapplication(at:toopenurlswithscheme:completion:).md)
  Sets the default app to use when opening files of a specific scheme.
### Managing Icons
- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](nsworkspace/icon(forfiles:).md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](nsworkspace/icon(for:).md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](nsworkspace/seticon(_:forfile:options:).md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions.md)
  Constants that describe options for creating icons.
### Unmounting a Device
- [func unmountAndEjectDevice(atPath: String) -> Bool](nsworkspace/unmountandejectdevice(atpath:).md)
  Unmounts and ejects the device at the specified path.
- [func unmountAndEjectDevice(at: URL) throws](nsworkspace/unmountandejectdevice(at:).md)
  Attempts to eject the volume mounted at the given path.
### Managing the Desktop Image
- [func desktopImageURL(for: NSScreen) -> URL?](nsworkspace/desktopimageurl(for:).md)
  Returns the URL for the desktop image for the given screen.
- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](nsworkspace/setdesktopimageurl(_:for:options:).md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [func desktopImageOptions(for: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?](nsworkspace/desktopimageoptions(for:).md)
  Returns the desktop image options for the given screen.
- [NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey.md)
  Keys that indicate how to display a new desktop image.
### Performing Finder Spotlight Searches
- [func showSearchResults(forQueryString: String) -> Bool](nsworkspace/showsearchresults(forquerystring:).md)
  Displays a Spotlight search results window in Finder for the specified query string.
### Finder File Labels
- [var fileLabels: [String]](nsworkspace/filelabels.md)
  The array of file labels, returned as strings.
- [var fileLabelColors: [NSColor]](nsworkspace/filelabelcolors.md)
  The array of colors for the file labels.
### Tracking Changes to the File System
- [func noteFileSystemChanged(String)](nsworkspace/notefilesystemchanged(_:).md)
  Informs the workspace object that the file system changed at the specified path.
### Requesting Additional Time Before Logout
- [func extendPowerOff(by: Int) -> Int](nsworkspace/extendpoweroff(by:).md)
  Requests the system wait for the specified amount of time before turning off the power or logging out the user.
### Supporting Accessibility
- [var accessibilityDisplayShouldDifferentiateWithoutColor: Bool](nsworkspace/accessibilitydisplayshoulddifferentiatewithoutcolor.md)
  A Boolean value that indicates whether the app avoids conveying information through color alone.
- [var accessibilityDisplayShouldIncreaseContrast: Bool](nsworkspace/accessibilitydisplayshouldincreasecontrast.md)
  A Boolean value that indicates whether the app presents a high-contrast user interface.
- [var accessibilityDisplayShouldReduceTransparency: Bool](nsworkspace/accessibilitydisplayshouldreducetransparency.md)
  A Boolean value that indicates whether the app avoids using semitransparent backgrounds.
- [var accessibilityDisplayShouldInvertColors: Bool](nsworkspace/accessibilitydisplayshouldinvertcolors.md)
  A Boolean value that indicates whether the accessibility option to invert colors is in an enabled state.
- [var accessibilityDisplayShouldReduceMotion: Bool](nsworkspace/accessibilitydisplayshouldreducemotion.md)
  A Boolean value that indicates whether the accessibility option to reduce motion is in an enabled state.
- [var isSwitchControlEnabled: Bool](nsworkspace/isswitchcontrolenabled.md)
  A Boolean value that indicates whether Switch Control is currently running.
- [var isVoiceOverEnabled: Bool](nsworkspace/isvoiceoverenabled.md)
  A Boolean value that indicates whether VoiceOver is currently running.
### Performing Privileged Operations
- [func requestAuthorization(to: NSWorkspace.AuthorizationType, completionHandler: (NSWorkspace.Authorization?, (any Error)?) -> Void)](nsworkspace/requestauthorization(to:completionhandler:).md)
  Requests authorization to perform a privileged file operation.
- [NSWorkspace.Authorization](nsworkspace/authorization.md)
  The authorization granted to the app by the user.
- [NSWorkspace.AuthorizationType](nsworkspace/authorizationtype.md)
  The types of privileged file operations that can be authorized by the user.
### Responding to Environment Notifications
- [class let willLaunchApplicationNotification: NSNotification.Name](nsworkspace/willlaunchapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to launch an app.
- [class let didLaunchApplicationNotification: NSNotification.Name](nsworkspace/didlaunchapplicationnotification.md)
  A notification that the workspace posts when a new app starts up.
- [class let didTerminateApplicationNotification: NSNotification.Name](nsworkspace/didterminateapplicationnotification.md)
  A notification that the workspace posts when an app finishes executing.
- [class let sessionDidBecomeActiveNotification: NSNotification.Name](nsworkspace/sessiondidbecomeactivenotification.md)
  A notification that the workspace posts after a user session switches in.
- [class let sessionDidResignActiveNotification: NSNotification.Name](nsworkspace/sessiondidresignactivenotification.md)
  A notification that the workspace posts before a user session switches out.
- [class let didHideApplicationNotification: NSNotification.Name](nsworkspace/didhideapplicationnotification.md)
  A notification that the workspace posts when the Finder hides an app.
- [class let didUnhideApplicationNotification: NSNotification.Name](nsworkspace/didunhideapplicationnotification.md)
  A notification that the workspace posts when the Finder unhides an app.
- [class let didActivateApplicationNotification: NSNotification.Name](nsworkspace/didactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder is about to activate an app.
- [class let didDeactivateApplicationNotification: NSNotification.Name](nsworkspace/diddeactivateapplicationnotification.md)
  A notification that the workspace posts when the Finder deactivates an app.
- [class let didRenameVolumeNotification: NSNotification.Name](nsworkspace/didrenamevolumenotification.md)
  A notification that the workspace posts when a volume changes its name or mount path.
- [class let didMountNotification: NSNotification.Name](nsworkspace/didmountnotification.md)
  A notification that the workspace posts when a new device mounts.
- [class let willUnmountNotification: NSNotification.Name](nsworkspace/willunmountnotification.md)
  A notification that the workspace posts when the Finder is about to unmount a device.
- [class let didUnmountNotification: NSNotification.Name](nsworkspace/didunmountnotification.md)
  A notification that the workspace posts when the Finder unmounts a device.
- [class let didChangeFileLabelsNotification: NSNotification.Name](nsworkspace/didchangefilelabelsnotification.md)
  A notification that the workspace posts when the Finder file labels or colors change.
- [class let activeSpaceDidChangeNotification: NSNotification.Name](nsworkspace/activespacedidchangenotification.md)
  A notification that the workspace posts when a Spaces change occurs.
- [class let didWakeNotification: NSNotification.Name](nsworkspace/didwakenotification.md)
  A notification that the workspace posts when the device wakes from sleep.
- [class let willPowerOffNotification: NSNotification.Name](nsworkspace/willpoweroffnotification.md)
  A notification that the workspace posts when the user requests a logout or powers off the device.
- [class let willSleepNotification: NSNotification.Name](nsworkspace/willsleepnotification.md)
  A notification that the workspace posts before the device goes to sleep.
- [class let screensDidSleepNotification: NSNotification.Name](nsworkspace/screensdidsleepnotification.md)
  A notification that the workspace posts when the device’s screen goes to sleep.
- [class let screensDidWakeNotification: NSNotification.Name](nsworkspace/screensdidwakenotification.md)
  A notification that the workspace posts when the device’s screens wake.
- [class let accessibilityDisplayOptionsDidChangeNotification: NSNotification.Name](nsworkspace/accessibilitydisplayoptionsdidchangenotification.md)
  A notification that the workspace posts when any of the accessibility display options change.
- [class let localizedVolumeNameUserInfoKey: String](nsworkspace/localizedvolumenameuserinfokey.md)
  A string containing the user-visible name of the volume.
- [class let volumeURLUserInfoKey: String](nsworkspace/volumeurluserinfokey.md)
  A URL containing the mount path of the volume.
- [class let oldLocalizedVolumeNameUserInfoKey: String](nsworkspace/oldlocalizedvolumenameuserinfokey.md)
  A string containing the old user-visible name of the volume
- [class let oldVolumeURLUserInfoKey: String](nsworkspace/oldvolumeurluserinfokey.md)
  A URL containing the old mount path of the volume
### Deprecated
- [Deprecated Symbols](nsworkspace-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [NSWorkspace.OpenConfiguration](nsworkspace/openconfiguration.md)
  The configuration options for opening URLs or launching apps.
- [struct NSAppKitVersion](nsappkitversion.md)
  Constants for determining which version of AppKit is available.
- [LSMinimumSystemVersion](../BundleResources/Information-Property-List/LSMinimumSystemVersion.md)
  The minimum version of the operating system required for the app to run in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace)*