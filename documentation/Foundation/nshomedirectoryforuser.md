# NSHomeDirectoryForUser(_:)

**Framework**: Foundation  
**Kind**: func

Returns the path to a given user’s home directory.

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
func NSHomeDirectoryForUser(_ userName: String?) -> String?
```

#### Return Value

The path to the home directory for the user specified by `userName`.

#### Discussion

For more information on file system utilities, see Low-Level File Management Programming Topics.

## Parameters

- `userName`: The name of a user.

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
- [var temporaryDirectory: URL](filemanager/temporarydirectory.md)
  The temporary directory for the current user.
- [func NSTemporaryDirectory() -> String](nstemporarydirectory().md)
  Returns the path of the temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshomedirectoryforuser(_:))*