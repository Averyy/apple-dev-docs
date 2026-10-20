# cachesDirectory

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The standard directory for discardable cache files.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var cachesDirectory: URL { get }
```

## Mentions

- [Using the file system effectively](../using-the-file-system-effectively.md)

#### Discussion

In iOS, this directory is within the app’s sandbox directory. In macOS, it’s within the app’s sandbox directory for sandboxed apps, or in the current user’s home directory `(~/Library/Caches)` if the app isn’t sandboxed.

This computed property is equivalent to calling [`NSSearchPathForDirectoriesInDomains(_:_:_:)`](../nssearchpathfordirectoriesindomains%28_,_,_%29.md) with the [`FileManager.SearchPathDirectory.cachesDirectory`](../filemanager/searchpathdirectory/cachesdirectory.md) parameter.

## See Also

### Accessing common directories
- [static var applicationDirectory: URL](./applicationdirectory.md)
  The standard directory for apps.
- [static var applicationSupportDirectory: URL](./applicationsupportdirectory.md)
  The standard directory for application support files.
- [static var desktopDirectory: URL](./desktopdirectory.md)
  The standard directory for files on the desktop.
- [static var documentsDirectory: URL](./documentsdirectory.md)
  The standard directory for document files.
- [static var downloadsDirectory: URL](./downloadsdirectory.md)
  The standard directory for download files.
- [static var libraryDirectory: URL](./librarydirectory.md)
  The standard directory for documentation, support, and configuration files.
- [static var moviesDirectory: URL](./moviesdirectory.md)
  The standard directory for movie files.
- [static var musicDirectory: URL](./musicdirectory.md)
  The standard directory for music files.
- [static var picturesDirectory: URL](./picturesdirectory.md)
  The standard directory for image files.
- [static var sharedPublicDirectory: URL](./sharedpublicdirectory.md)
  The standard directory for publicly shared files.
- [static var temporaryDirectory: URL](./temporarydirectory.md)
  The standard directory for temporary files.
- [static var trashDirectory: URL](./trashdirectory.md)
  The standard trash directory.
- [static var userDirectory: URL](./userdirectory.md)
  The container directory of user home directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/cachesdirectory)*