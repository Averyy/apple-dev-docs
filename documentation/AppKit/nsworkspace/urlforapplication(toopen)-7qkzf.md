# urlForApplication(toOpen:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the URL to the default app to open the specified URL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func urlForApplication(toOpen url: URL) -> URL?
```

```objc
- (NSURL *) URLForApplicationToOpenURL:(NSURL *) url;
```

#### Return Value

The URL of the default app that would open the specified `url`. Returns `nil` if no app can open the URL, or if the file URL does not exist.

#### Discussion

This method is the programmatic equivalent of double-clicking a document in the Finder.

You can safely call this method from any thread of your app.

## Parameters

- `url`: The URL of the file to open.

## See Also

### Requesting Information
- [func urlForApplication(toOpen: UTType) -> URL?](./urlforapplication%28toopen%29-95cvp.md)
  Returns the URL to the default app to open the specified content type.
- [func urlForApplication(withBundleIdentifier: String) -> URL?](./urlforapplication%28withbundleidentifier%29.md)
  Returns the URL to the default app with the specified bundle identifier.
- [func urlsForApplications(toOpen: URL) -> [URL]](./urlsforapplications%28toopen%29-ualk.md)
  Returns an array of URLs to all available applications that can open the URL.
- [func urlsForApplications(toOpen: UTType) -> [URL]](./urlsforapplications%28toopen%29-60rkm.md)
  Returns an array of URLs to all available applications that can open the specified content type.
- [func urlsForApplications(withBundleIdentifier: String) -> [URL]](./urlsforapplications%28withbundleidentifier%29.md)
  Returns an array of URLs to all available applications that can open the specified bundle identifier.
- [func getFileSystemInfo(forPath: String, isRemovable: UnsafeMutablePointer<ObjCBool>?, isWritable: UnsafeMutablePointer<ObjCBool>?, isUnmountable: UnsafeMutablePointer<ObjCBool>?, description: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getfilesysteminfo%28forpath,isremovable,iswritable,isunmountable,description,type%29.md)
  Returns information about the file system at the specified path.
- [func isFilePackage(atPath: String) -> Bool](./isfilepackage%28atpath%29.md)
  Determines whether the specified path is a file package.
- [var frontmostApplication: NSRunningApplication?](./frontmostapplication.md)
  Returns the frontmost app, which is the app that receives key events.
- [var runningApplications: [NSRunningApplication]](./runningapplications.md)
  Returns an array of running apps.
- [var menuBarOwningApplication: NSRunningApplication?](./menubarowningapplication.md)
  Returns the app that owns the currently displayed menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/urlforapplication(toopen:)-7qkzf)*