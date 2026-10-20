# homeDirectory

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

### Accessing home and user directories
- [static func currentDirectory() -> URL](./currentdirectory%28%29.md)
  Returns the working directory of the current process.
- [static func homeDirectory(forUser: String) -> URL?](./homedirectory%28foruser%29.md)
  Returns the home directory for the specified user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/homedirectory)*