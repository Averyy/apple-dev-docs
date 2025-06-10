# FileManager.SearchPathDirectory

**Framework**: Foundation  
**Kind**: enum

The location of significant directories.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SearchPathDirectory
```

#### Overview

Use these constants with the [`init(for:in:appropriateFor:create:)`](url/init(for:in:appropriatefor:create:).md) initializer and the [`urls(for:in:)`](filemanager/urls(for:in:).md) and [`url(for:in:appropriateFor:create:)`](filemanager/url(for:in:appropriatefor:create:).md) methods of FileManager.

## Topics

### Directory Locations
- [FileManager.SearchPathDirectory.applicationDirectory](filemanager/searchpathdirectory/applicationdirectory.md)
  Supported applications (`/Applications`).
- [FileManager.SearchPathDirectory.demoApplicationDirectory](filemanager/searchpathdirectory/demoapplicationdirectory.md)
  Unsupported applications and demonstration versions.
- [FileManager.SearchPathDirectory.developerApplicationDirectory](filemanager/searchpathdirectory/developerapplicationdirectory.md)
  Developer applications (`/Developer/Applications`).
- [FileManager.SearchPathDirectory.adminApplicationDirectory](filemanager/searchpathdirectory/adminapplicationdirectory.md)
  System and network administration applications.
- [FileManager.SearchPathDirectory.libraryDirectory](filemanager/searchpathdirectory/librarydirectory.md)
  Various user-visible documentation, support, and configuration files (`/Library`).
- [FileManager.SearchPathDirectory.developerDirectory](filemanager/searchpathdirectory/developerdirectory.md)
  Developer resources (`/Developer`).
- [FileManager.SearchPathDirectory.userDirectory](filemanager/searchpathdirectory/userdirectory.md)
  User home directories (`/Users`).
- [FileManager.SearchPathDirectory.documentationDirectory](filemanager/searchpathdirectory/documentationdirectory.md)
  Documentation.
- [FileManager.SearchPathDirectory.documentDirectory](filemanager/searchpathdirectory/documentdirectory.md)
  Document directory.
- [FileManager.SearchPathDirectory.coreServiceDirectory](filemanager/searchpathdirectory/coreservicedirectory.md)
  Core services (`System/Library/CoreServices`).
- [FileManager.SearchPathDirectory.autosavedInformationDirectory](filemanager/searchpathdirectory/autosavedinformationdirectory.md)
  The user’s autosaved documents (`Library/Autosave Information`).
- [FileManager.SearchPathDirectory.desktopDirectory](filemanager/searchpathdirectory/desktopdirectory.md)
  The user’s desktop directory.
- [FileManager.SearchPathDirectory.cachesDirectory](filemanager/searchpathdirectory/cachesdirectory.md)
  Discardable cache files (`Library/Caches`).
- [FileManager.SearchPathDirectory.applicationSupportDirectory](filemanager/searchpathdirectory/applicationsupportdirectory.md)
  Application support files (`Library/Application Support`).
- [FileManager.SearchPathDirectory.downloadsDirectory](filemanager/searchpathdirectory/downloadsdirectory.md)
  The user’s downloads directory.
- [FileManager.SearchPathDirectory.inputMethodsDirectory](filemanager/searchpathdirectory/inputmethodsdirectory.md)
  Input Methods `(Library/Input Methods)`.
- [FileManager.SearchPathDirectory.moviesDirectory](filemanager/searchpathdirectory/moviesdirectory.md)
  The user’s Movies directory `(~/Movies`).
- [FileManager.SearchPathDirectory.musicDirectory](filemanager/searchpathdirectory/musicdirectory.md)
  The user’s Music directory (`~/Music`).
- [FileManager.SearchPathDirectory.picturesDirectory](filemanager/searchpathdirectory/picturesdirectory.md)
  The user’s Pictures directory (`~/Pictures`).
- [FileManager.SearchPathDirectory.printerDescriptionDirectory](filemanager/searchpathdirectory/printerdescriptiondirectory.md)
  The system’s PPDs directory (`Library/Printers/PPDs`).
- [FileManager.SearchPathDirectory.sharedPublicDirectory](filemanager/searchpathdirectory/sharedpublicdirectory.md)
  The user’s Public sharing directory (`~/Public`).
- [FileManager.SearchPathDirectory.preferencePanesDirectory](filemanager/searchpathdirectory/preferencepanesdirectory.md)
  The PreferencePanes directory for use with System Preferences (`Library/PreferencePanes`).
- [FileManager.SearchPathDirectory.applicationScriptsDirectory](filemanager/searchpathdirectory/applicationscriptsdirectory.md)
  The user scripts folder for the calling application (`~/Library/Application Scripts/<code-signing-id>`.
- [FileManager.SearchPathDirectory.itemReplacementDirectory](filemanager/searchpathdirectory/itemreplacementdirectory.md)
  The constant used to create a temporary directory.
- [FileManager.SearchPathDirectory.allApplicationsDirectory](filemanager/searchpathdirectory/allapplicationsdirectory.md)
  All directories where applications can be stored.
- [FileManager.SearchPathDirectory.allLibrariesDirectory](filemanager/searchpathdirectory/alllibrariesdirectory.md)
  All directories where resources can be stored.
- [FileManager.SearchPathDirectory.trashDirectory](filemanager/searchpathdirectory/trashdirectory.md)
  The trash directory.
### Initializers
- [init?(rawValue: UInt)](filemanager/searchpathdirectory/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeKey](fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory)*