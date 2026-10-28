# FileManager.SearchPathDirectory.downloadsDirectory

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The user’s downloads directory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case downloadsDirectory
```

```c
NSDownloadsDirectory
```

## Discussion

The [`FileManager.SearchPathDirectory.downloadsDirectory`](./downloadsdirectory.md) flag only produces a path when you provide a [`userDomainMask`](../searchpathdomainmask/userdomainmask.md).

## See Also

### Directory Locations
- [FileManager.SearchPathDirectory.applicationDirectory](./applicationdirectory.md)
  Supported applications (`/Applications`).
- [FileManager.SearchPathDirectory.demoApplicationDirectory](./demoapplicationdirectory.md)
  Unsupported applications and demonstration versions.
- [FileManager.SearchPathDirectory.developerApplicationDirectory](./developerapplicationdirectory.md)
  Developer applications (`/Developer/Applications`).
- [FileManager.SearchPathDirectory.adminApplicationDirectory](./adminapplicationdirectory.md)
  System and network administration applications.
- [FileManager.SearchPathDirectory.libraryDirectory](./librarydirectory.md)
  Various user-visible documentation, support, and configuration files (`/Library`).
- [FileManager.SearchPathDirectory.developerDirectory](./developerdirectory.md)
  Developer resources (`/Developer`).
- [FileManager.SearchPathDirectory.userDirectory](./userdirectory.md)
  User home directories (`/Users`).
- [FileManager.SearchPathDirectory.documentationDirectory](./documentationdirectory.md)
  Documentation.
- [FileManager.SearchPathDirectory.documentDirectory](./documentdirectory.md)
  Document directory.
- [FileManager.SearchPathDirectory.coreServiceDirectory](./coreservicedirectory.md)
  Core services (`System/Library/CoreServices`).
- [FileManager.SearchPathDirectory.autosavedInformationDirectory](./autosavedinformationdirectory.md)
  The user’s autosaved documents (`Library/Autosave Information`).
- [FileManager.SearchPathDirectory.desktopDirectory](./desktopdirectory.md)
  The user’s desktop directory.
- [FileManager.SearchPathDirectory.cachesDirectory](./cachesdirectory.md)
  Discardable cache files (`Library/Caches`).
- [FileManager.SearchPathDirectory.applicationSupportDirectory](./applicationsupportdirectory.md)
  Application support files (`Library/Application Support`).
- [FileManager.SearchPathDirectory.inputMethodsDirectory](./inputmethodsdirectory.md)
  Input Methods `(Library/Input Methods)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/downloadsdirectory)*