# NSHomeDirectory()

**Framework**: Foundation  
**Kind**: func

Returns the path to either the user’s or application’s home directory, depending on the platform.

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
func NSHomeDirectory() -> String
```

#### Return Value

The path to the current home directory.

#### Discussion

In iOS, the home directory is the application’s sandbox directory. In macOS, it’s the application’s sandbox directory, or the current user’s home directory if the application isn’t in a sandbox.

## See Also

- [var homeDirectoryForCurrentUser: URL](filemanager/homedirectoryforcurrentuser.md)
  The home directory for the current user.
- [func NSUserName() -> String](nsusername().md)
  Returns the logon name of the current user.
- [func NSFullUserName() -> String](nsfullusername().md)
  Returns a string containing the full name of the current user.
- [func homeDirectory(forUser: String) -> URL?](filemanager/homedirectory(foruser:).md)
  Returns the home directory for the specified user.
- [func NSHomeDirectoryForUser(String?) -> String?](nshomedirectoryforuser(_:).md)
  Returns the path to a given user’s home directory.
- [var temporaryDirectory: URL](filemanager/temporarydirectory.md)
  The temporary directory for the current user.
- [func NSTemporaryDirectory() -> String](nstemporarydirectory().md)
  Returns the path of the temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshomedirectory())*