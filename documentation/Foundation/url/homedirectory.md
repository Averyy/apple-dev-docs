# homeDirectory

**Framework**: Foundation  
**Kind**: property

The home directory for the current user.

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
static var homeDirectory: URL { get }
```

#### Discussion

This URL is the equivalent of the shell value `~/`.

Complexity: `O(1)`.

## See Also

- [static func currentDirectory() -> URL](url/currentdirectory.md)
  Returns the working directory of the current process.
- [static func homeDirectory(forUser: String) -> URL?](url/homedirectory(foruser:).md)
  Returns the home directory for the specified user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/homedirectory)*