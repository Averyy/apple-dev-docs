# NSTemporaryDirectory()

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns the path of the temporary directory for the current user.

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
func NSTemporaryDirectory() -> String
```

```c
extern NSString *NSTemporaryDirectory();
```

## Return Value

A string containing the path of the temporary directory for the current user.

## Discussion

See the [`FileManager`](./filemanager.md) method [`url(for:in:appropriateFor:create:)`](./filemanager/url%28for,in,appropriatefor,create%29.md) for the preferred means of finding the correct temporary directory.

For more information about temporary files, see [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

## See Also

### Related Documentation
- [func NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory, FileManager.SearchPathDomainMask, Bool) -> [String]](./nssearchpathfordirectoriesindomains%28_,_,_%29.md)
  Creates a list of directory search paths.
### Accessing user directories
- [var homeDirectoryForCurrentUser: URL](./filemanager/homedirectoryforcurrentuser.md)
  The home directory for the current user.
- [func NSHomeDirectory() -> String](./nshomedirectory%28%29.md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
- [func NSUserName() -> String](./nsusername%28%29.md)
  Returns the logon name of the current user.
- [func NSFullUserName() -> String](./nsfullusername%28%29.md)
  Returns a string containing the full name of the current user.
- [func homeDirectory(forUser: String) -> URL?](./filemanager/homedirectory%28foruser%29.md)
  Returns the home directory for the specified user.
- [func NSHomeDirectoryForUser(String?) -> String?](./nshomedirectoryforuser%28_%29.md)
  Returns the path to a given user’s home directory.
- [var temporaryDirectory: URL](./filemanager/temporarydirectory.md)
  The temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstemporarydirectory())*