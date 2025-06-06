# musicDirectory

**Framework**: Foundation  
**Kind**: property

The standard directory for music files.

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
static var musicDirectory: URL { get }
```

#### Discussion

In iOS, this directory is within the app’s sandbox directory. In macOS, it’s within the app’s sandbox directory for sandboxed apps, or in the current user’s home directory `(~/Music)` if the app isn’t sandboxed.

This computed property is equivalent to calling [`NSSearchPathForDirectoriesInDomains(_:_:_:)`](nssearchpathfordirectoriesindomains(_:_:_:).md) with the [`FileManager.SearchPathDirectory.musicDirectory`](filemanager/searchpathdirectory/musicdirectory.md) parameter.

## See Also

- [static var applicationDirectory: URL](url/applicationdirectory.md)
  The standard directory for apps.
- [static var applicationSupportDirectory: URL](url/applicationsupportdirectory.md)
  The standard directory for application support files.
- [static var cachesDirectory: URL](url/cachesdirectory.md)
  The standard directory for discardable cache files.
- [static var desktopDirectory: URL](url/desktopdirectory.md)
  The standard directory for files on the desktop.
- [static var documentsDirectory: URL](url/documentsdirectory.md)
  The standard directory for document files.
- [static var downloadsDirectory: URL](url/downloadsdirectory.md)
  The standard directory for download files.
- [static var libraryDirectory: URL](url/librarydirectory.md)
  The standard directory for documentation, support, and configuration files.
- [static var moviesDirectory: URL](url/moviesdirectory.md)
  The standard directory for movie files.
- [static var picturesDirectory: URL](url/picturesdirectory.md)
  The standard directory for image files.
- [static var sharedPublicDirectory: URL](url/sharedpublicdirectory.md)
  The standard directory for publicly shared files.
- [static var temporaryDirectory: URL](url/temporarydirectory.md)
  The standard directory for temporary files.
- [static var trashDirectory: URL](url/trashdirectory.md)
  The standard trash directory.
- [static var userDirectory: URL](url/userdirectory.md)
  The container directory of user home directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/musicdirectory)*