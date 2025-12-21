# getInfoForFile(_:application:type:)

**Framework**: AppKit  
**Kind**: method

Retrieves information about the specified file.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func getInfoForFile(_ fullPath: String, application appName: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if this method successfully retrieved the information, or [`false`](https://developer.apple.com/documentation/Swift/false) if it couldn’t find the file or the app isn’t associated with the file.

#### Discussion

You can safely call this method from any thread of your app.

## Parameters

- `fullPath`: The full path to the desired file.
- `appName`: The app the system would use to open the file.
- `type`: On input, a pointer to a string object variable; on return, if the method is successful, this variable contains a string object with the filename extension or encoded HFS file type of the file.

## See Also

- [func icon(forFiles: [String]) -> NSImage?](nsworkspace/icon(forfiles:).md)
  Returns an image containing the icon for the specified files.
- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/getinfoforfile(_:application:type:))*