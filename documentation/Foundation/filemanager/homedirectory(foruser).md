# homeDirectory(forUser:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the home directory for the specified user.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func homeDirectory(forUser userName: String) -> URL?
```

```objc
- (NSURL *) homeDirectoryForUser:(NSString *) userName;
```

## Return Value

A URL object containing the location of the specified user’s home directory, or `nil` if no such user exists or the user’s home directory is not available.

## Parameters

- `userName`: The username of the owner of the desired home directory.

## See Also

### Accessing user directories
- [var homeDirectoryForCurrentUser: URL](./homedirectoryforcurrentuser.md)
  The home directory for the current user.
- [func NSHomeDirectory() -> String](../nshomedirectory%28%29.md)
  Returns the path to either the user’s or application’s home directory, depending on the platform.
- [func NSUserName() -> String](../nsusername%28%29.md)
  Returns the logon name of the current user.
- [func NSFullUserName() -> String](../nsfullusername%28%29.md)
  Returns a string containing the full name of the current user.
- [func NSHomeDirectoryForUser(String?) -> String?](../nshomedirectoryforuser%28_%29.md)
  Returns the path to a given user’s home directory.
- [var temporaryDirectory: URL](./temporarydirectory.md)
  The temporary directory for the current user.
- [func NSTemporaryDirectory() -> String](../nstemporarydirectory%28%29.md)
  Returns the path of the temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/homedirectory(foruser:))*