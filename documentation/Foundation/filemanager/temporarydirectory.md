# temporaryDirectory

**Framework**: Foundation  
**Kind**: property

The temporary directory for the current user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var temporaryDirectory: URL { get }
```

## Mentions

- [Using the file system effectively](using-the-file-system-effectively.md)

## See Also

- [var homeDirectoryForCurrentUser: URL](filemanager/homedirectoryforcurrentuser.md)
  The home directory for the current user.
- [func NSHomeDirectory() -> String](nshomedirectory().md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
- [func NSUserName() -> String](nsusername().md)
  Returns the logon name of the current user.
- [func NSFullUserName() -> String](nsfullusername().md)
  Returns a string containing the full name of the current user.
- [func homeDirectory(forUser: String) -> URL?](filemanager/homedirectory(foruser:).md)
  Returns the home directory for the specified user.
- [func NSHomeDirectoryForUser(String?) -> String?](nshomedirectoryforuser(_:).md)
  Returns the path to a given user’s home directory.
- [func NSTemporaryDirectory() -> String](nstemporarydirectory().md)
  Returns the path of the temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/temporarydirectory)*