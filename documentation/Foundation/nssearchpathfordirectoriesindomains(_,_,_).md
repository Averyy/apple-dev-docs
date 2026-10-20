# NSSearchPathForDirectoriesInDomains(_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern NSArray<NSString *> *NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory directory, NSSearchPathDomainMask domainMask, BOOL expandTilde);
```

#### Discussion

Creates a list of path strings for the specified directories in the specified domains. The list is in the order in which you should search the directories. If `expandTilde` is [`true`](../Swift/true.md), tildes are expanded as described in [`expandingTildeInPath`](./nsstring/expandingtildeinpath.md).

You should consider using the [`FileManager`](./filemanager.md) methods [`urls(for:in:)`](./filemanager/urls%28for,in%29.md) and [`url(for:in:appropriateFor:create:)`](./filemanager/url%28for,in,appropriatefor,create%29.md). which return URLs, which are the preferred format.

For more information on file system utilities, see [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

> **Note**:  The directory returned by this method may not exist. This method simply gives you the appropriate location for the requested directory. Depending on the application’s needs, it may be up to the developer to create the appropriate directory and any in between.

## See Also

### Locating system directories
- [func url(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws -> URL](./filemanager/url%28for,in,appropriatefor,create%29.md)
  Locates and optionally creates the specified common directory in a domain.
- [func urls(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask) -> [URL]](./filemanager/urls%28for,in%29.md)
  Returns an array of URLs for the specified common directory in the requested domains.
- [func NSOpenStepRootDirectory() -> String](./nsopensteprootdirectory%28%29.md)
  Returns the root directory of the user’s system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssearchpathfordirectoriesindomains(_:_:_:))*