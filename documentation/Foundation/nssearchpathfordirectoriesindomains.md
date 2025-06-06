# NSSearchPathForDirectoriesInDomains(_:_:_:)

**Framework**: Foundation  
**Kind**: func

Creates a list of directory search paths.

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
func NSSearchPathForDirectoriesInDomains(_ directory: FileManager.SearchPathDirectory, _ domainMask: FileManager.SearchPathDomainMask, _ expandTilde: Bool) -> [String]
```

#### Discussion

Creates a list of path strings for the specified directories in the specified domains. The list is in the order in which you should search the directories. If `expandTilde` is [`true`](https://developer.apple.com/documentation/swift/true), tildes are expanded as described in [`expandingTildeInPath`](nsstring/expandingtildeinpath.md).

You should consider using the [`FileManager`](filemanager.md) methods [`urls(for:in:)`](filemanager/urls(for:in:).md) and [`url(for:in:appropriateFor:create:)`](filemanager/url(for:in:appropriatefor:create:).md). which return URLs, which are the preferred format.

For more information on file system utilities, see [`File System Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

> **Note**:  The directory returned by this method may not exist. This method simply gives you the appropriate location for the requested directory. Depending on the application’s needs, it may be up to the developer to create the appropriate directory and any in between.

 The directory returned by this method may not exist. This method simply gives you the appropriate location for the requested directory. Depending on the application’s needs, it may be up to the developer to create the appropriate directory and any in between.

## See Also

- [func url(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws -> URL](filemanager/url(for:in:appropriatefor:create:).md)
  Locates and optionally creates the specified common directory in a domain.
- [func urls(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask) -> [URL]](filemanager/urls(for:in:).md)
  Returns an array of URLs for the specified common directory in the requested domains.
- [func NSOpenStepRootDirectory() -> String](nsopensteprootdirectory().md)
  Returns the root directory of the user’s system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssearchpathfordirectoriesindomains(_:_:_:))*