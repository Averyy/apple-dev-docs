# currentDirectory()

**Framework**: Foundation  
**Kind**: method

Returns the working directory of the current process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func currentDirectory() -> URL
```

#### Return Value

Calling this method issues a `getcwd` system call. This method’s return value can change between calls because any thread can change the process’s current working directory at any time. Take precautions when reasoning about the current directory in a multithreaded environment.

## See Also

- [static var homeDirectory: URL](url/homedirectory.md)
  The home directory for the current user.
- [static func homeDirectory(forUser: String) -> URL?](url/homedirectory(foruser:).md)
  Returns the home directory for the specified user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/currentdirectory())*