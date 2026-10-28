# runningApplications

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns an array of running apps.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var runningApplications: [NSRunningApplication] { get }
```

```objc
@property (copy, readonly) NSArray<NSRunningApplication *> * runningApplications;
```

## Return Value

An array of  [`NSRunningApplication`](../nsrunningapplication.md) instances. This value is key-value observing compliant.

## Discussion

The order of the array is unspecified, but it is stable, meaning that the relative order of particular apps will not change across multiple calls to `runningApplications`. See [`NSRunningApplication`](../nsrunningapplication.md) for more information on `NSRunningApplication`.

Similar to the [`NSRunningApplication`](../nsrunningapplication.md) class’s properties, this property will only change when the main run loop runs in a common mode.  Instead of polling, use key-value observing to be notified of changes to this array property.

You can safely call this method from any of your app’s threads. The method returns its value atomically.

## See Also

### Requesting Information
- [func urlForApplication(toOpen: URL) -> URL?](./urlforapplication%28toopen%29-7qkzf.md)
  Returns the URL to the default app to open the specified URL.
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
- [var menuBarOwningApplication: NSRunningApplication?](./menubarowningapplication.md)
  Returns the app that owns the currently displayed menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/runningapplications)*