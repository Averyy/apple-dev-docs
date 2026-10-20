# homeDirectoryForCurrentUser

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The home directory for the current user.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var homeDirectoryForCurrentUser: URL { get }
```

```objc
@property (copy, readonly) NSURL * homeDirectoryForCurrentUser;
```

## See Also

### Accessing user directories
- [func NSHomeDirectory() -> String](../nshomedirectory%28%29.md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
- [func NSUserName() -> String](../nsusername%28%29.md)
  Returns the logon name of the current user.
- [func NSFullUserName() -> String](../nsfullusername%28%29.md)
  Returns a string containing the full name of the current user.
- [func homeDirectory(forUser: String) -> URL?](./homedirectory%28foruser%29.md)
  Returns the home directory for the specified user.
- [func NSHomeDirectoryForUser(String?) -> String?](../nshomedirectoryforuser%28_%29.md)
  Returns the path to a given user’s home directory.
- [var temporaryDirectory: URL](./temporarydirectory.md)
  The temporary directory for the current user.
- [func NSTemporaryDirectory() -> String](../nstemporarydirectory%28%29.md)
  Returns the path of the temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/homedirectoryforcurrentuser)*