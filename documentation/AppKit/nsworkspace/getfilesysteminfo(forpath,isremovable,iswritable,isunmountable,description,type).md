# getFileSystemInfo(forPath:isRemovable:isWritable:isUnmountable:description:type:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns information about the file system at the specified path.

**Availability**:
- macOS

## Declaration

```swift
func getFileSystemInfo(forPath fullPath: String, isRemovable removableFlag: UnsafeMutablePointer<ObjCBool>?, isWritable writableFlag: UnsafeMutablePointer<ObjCBool>?, isUnmountable unmountableFlag: UnsafeMutablePointer<ObjCBool>?, description: AutoreleasingUnsafeMutablePointer<NSString?>?, type fileSystemType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

```objc
- (BOOL) getFileSystemInfoForPath:(NSString *) fullPath isRemovable:(BOOL *) removableFlag isWritable:(BOOL *) writableFlag isUnmountable:(BOOL *) unmountableFlag description:(NSString **) description type:(NSString **) fileSystemType;
```

#### Return Value

[`true`](../../Swift/true.md) if the information was returned; otherwise, [`false`](../../Swift/false.md).

#### Discussion

You can safely call this method from any thread of your app.

## Parameters

- `fullPath`: The path to the file system mount point.
- `removableFlag`: On input, a Boolean variable; on return, this variable contains [`true`](../../Swift/true.md) if the file system is on removable media.
- `writableFlag`: On input, a Boolean variable; on return, this variable contains [`true`](../../Swift/true.md) if the file system writable.
- `unmountableFlag`: On input, a Boolean variable; on return, this variable contains [`true`](../../Swift/true.md) if the file system is unmountable.
- `description`: On input, a pointer to a string object variable; on return, if the method was successful, this variable contains a string object that describes the file system. You should not rely on this description for program logic but can use it in message strings. Values can include  “hard,” “nfs,” and “foreign.”
- `fileSystemType`: On input, a pointer to a string object variable; on return, if the method was successful, this variable contains the file system type. Values can include “HFS,” “UFS,” or other values.

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
- [func isFilePackage(atPath: String) -> Bool](./isfilepackage%28atpath%29.md)
  Determines whether the specified path is a file package.
- [var frontmostApplication: NSRunningApplication?](./frontmostapplication.md)
  Returns the frontmost app, which is the app that receives key events.
- [var runningApplications: [NSRunningApplication]](./runningapplications.md)
  Returns an array of running apps.
- [var menuBarOwningApplication: NSRunningApplication?](./menubarowningapplication.md)
  Returns the app that owns the currently displayed menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/getfilesysteminfo(forpath:isremovable:iswritable:isunmountable:description:type:))*