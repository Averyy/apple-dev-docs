# temporaryDirectory

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSURL * temporaryDirectory;
```

## Mentions

- [Using the file system effectively](../using-the-file-system-effectively.md)

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
- [func homeDirectory(forUser: String) -> URL?](./homedirectory%28foruser%29.md)
  Returns the home directory for the specified user.
- [func NSHomeDirectoryForUser(String?) -> String?](../nshomedirectoryforuser%28_%29.md)
  Returns the path to a given user’s home directory.
- [func NSTemporaryDirectory() -> String](../nstemporarydirectory%28%29.md)
  Returns the path of the temporary directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/temporarydirectory)*