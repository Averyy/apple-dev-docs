# NSOpenStepRootDirectory()

**Framework**: Foundation  
**Kind**: func

Returns the root directory of the user’s system.

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
func NSOpenStepRootDirectory() -> String
```

#### Return Value

A string identifying the root directory of the user’s system.

#### Discussion

For more information on file system utilities, see Low-Level File Management Programming Topics.

## See Also

- [func NSHomeDirectory() -> String](nshomedirectory().md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
- [func NSHomeDirectoryForUser(String?) -> String?](nshomedirectoryforuser(_:).md)
  Returns the path to a given user’s home directory.
- [func url(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask, appropriateFor: URL?, create: Bool) throws -> URL](filemanager/url(for:in:appropriatefor:create:).md)
  Locates and optionally creates the specified common directory in a domain.
- [func urls(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask) -> [URL]](filemanager/urls(for:in:).md)
  Returns an array of URLs for the specified common directory in the requested domains.
- [func NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory, FileManager.SearchPathDomainMask, Bool) -> [String]](nssearchpathfordirectoriesindomains(_:_:_:).md)
  Creates a list of directory search paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsopensteprootdirectory())*