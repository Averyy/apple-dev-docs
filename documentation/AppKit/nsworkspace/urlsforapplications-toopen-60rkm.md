# urlsForApplications(toOpen:)

**Framework**: AppKit  
**Kind**: method

Returns an array of URLs to all available applications that can open the specified content type.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func urlsForApplications(toOpen contentType: UTType) -> [URL]
```

#### Return Value

An array of URLs to available apps that can open the specified `contentType`. Returns an empty array if no app can open the content type.

#### Discussion

The system sorts the resulting array according to each app’s suitability to open the `contentType`. The returned array lists the best match first.

## Parameters

- `contentType`: The content type to open.

## See Also

- [func urlForApplication(toOpen: URL) -> URL?](nsworkspace/urlforapplication(toopen:)-7qkzf.md)
  Returns the URL to the default app to open the specified URL.
- [func urlForApplication(toOpen: UTType) -> URL?](nsworkspace/urlforapplication(toopen:)-95cvp.md)
  Returns the URL to the default app to open the specified content type.
- [func urlForApplication(withBundleIdentifier: String) -> URL?](nsworkspace/urlforapplication(withbundleidentifier:).md)
  Returns the URL to the default app with the specified bundle identifier.
- [func urlsForApplications(toOpen: URL) -> [URL]](nsworkspace/urlsforapplications(toopen:)-ualk.md)
  Returns an array of URLs to all available applications that can open the URL.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/urlsforapplications(toopen:)-60rkm)*