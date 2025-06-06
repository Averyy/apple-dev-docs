# urls(for:in:)

**Framework**: Foundation  
**Kind**: method

Returns an array of URLs for the specified common directory in the requested domains.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func urls(for directory: FileManager.SearchPathDirectory, in domainMask: FileManager.SearchPathDomainMask) -> [URL]
```

#### Return Value

An array of [`NSURL`](nsurl.md) objects identifying the requested directories. The directories are ordered according to the order of the domain mask constants, with items in the user domain first and items in the system domain last.

#### Discussion

This method is intended to locate known and common directories in the system. For example, setting the directory to [`FileManager.SearchPathDirectory.applicationDirectory`](filemanager/searchpathdirectory/applicationdirectory.md), will return the Applications directories in the requested domain. There are a number of common directories available in the [`FileManager.SearchPathDirectory`](filemanager/searchpathdirectory.md), including: [`FileManager.SearchPathDirectory.desktopDirectory`](filemanager/searchpathdirectory/desktopdirectory.md), [`FileManager.SearchPathDirectory.applicationSupportDirectory`](filemanager/searchpathdirectory/applicationsupportdirectory.md), and many more.

## Parameters

- `directory`: The search path directory. The supported values are described in  .
- `domainMask`: The file system domain to search. The value for this parameter is one or more of the constants described in  .

## See Also

- [func url(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws -> URL](filemanager/url(for:in:appropriatefor:create:).md)
  Locates and optionally creates the specified common directory in a domain.
- [func NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory, FileManager.SearchPathDomainMask, Bool) -> [String]](nssearchpathfordirectoriesindomains(_:_:_:).md)
  Creates a list of directory search paths.
- [func NSOpenStepRootDirectory() -> String](nsopensteprootdirectory().md)
  Returns the root directory of the user’s system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/urls(for:in:))*