# getFileSystemInfo(forPath:isRemovable:isWritable:isUnmountable:description:type:)

**Framework**: AppKit  
**Kind**: method

Returns information about the file system at the specified path.

**Availability**:
- macOS ?+

## Declaration

```swift
func getFileSystemInfo(forPath fullPath: String, isRemovable removableFlag: UnsafeMutablePointer<ObjCBool>?, isWritable writableFlag: UnsafeMutablePointer<ObjCBool>?, isUnmountable unmountableFlag: UnsafeMutablePointer<ObjCBool>?, description: AutoreleasingUnsafeMutablePointer<NSString?>?, type fileSystemType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the information was returned; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You can safely call this method from any thread of your app.

## Parameters

- `fullPath`: The path to the file system mount point.
- `removableFlag`: On input, a Boolean variable; on return, this variable contains   if the file system is on removable media.
- `writableFlag`: On input, a Boolean variable; on return, this variable contains   if the file system writable.
- `unmountableFlag`: On input, a Boolean variable; on return, this variable contains   if the file system is unmountable.
- `description`: On input, a pointer to a string object variable; on return, if the method was successful, this variable contains a string object that describes the file system. You should not rely on this description for program logic but can use it in message strings. Values can include  “hard,” “nfs,” and “foreign.”
- `fileSystemType`: On input, a pointer to a string object variable; on return, if the method was successful, this variable contains the file system type. Values can include “HFS,” “UFS,” or other values.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/getfilesysteminfo(forpath:isremovable:iswritable:isunmountable:description:type:))*