# urls(for:in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<NSURL *> *) URLsForDirectory:(NSSearchPathDirectory) directory inDomains:(NSSearchPathDomainMask) domainMask;
```

## Mentions

- [Using the file system effectively](../using-the-file-system-effectively.md)

## Return Value

An array of [`NSURL`](../nsurl.md) objects identifying the requested directories. The directories are ordered according to the order of the domain mask constants, with items in the user domain first and items in the system domain last.

## Discussion

This method is intended to locate known and common directories in the system. For example, setting the directory to [`FileManager.SearchPathDirectory.applicationDirectory`](./searchpathdirectory/applicationdirectory.md), will return the Applications directories in the requested domain. There are a number of common directories available in the [`FileManager.SearchPathDirectory`](./searchpathdirectory.md), including: [`FileManager.SearchPathDirectory.desktopDirectory`](./searchpathdirectory/desktopdirectory.md), [`FileManager.SearchPathDirectory.applicationSupportDirectory`](./searchpathdirectory/applicationsupportdirectory.md), and many more.

## Parameters

- `directory`: The search path directory. The supported values are described in [`FileManager.SearchPathDirectory`](./searchpathdirectory.md).
- `domainMask`: The file system domain to search. The value for this parameter is one or more of the constants described in [`FileManager.SearchPathDomainMask`](./searchpathdomainmask.md).

## See Also

### Locating system directories
- [func url(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws -> URL](./url%28for,in,appropriatefor,create%29.md)
  Locates and optionally creates the specified common directory in a domain.
- [func NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory, FileManager.SearchPathDomainMask, Bool) -> [String]](../nssearchpathfordirectoriesindomains%28_,_,_%29.md)
  Creates a list of directory search paths.
- [func NSOpenStepRootDirectory() -> String](../nsopensteprootdirectory%28%29.md)
  Returns the root directory of the user’s system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/urls(for:in:))*