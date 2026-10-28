# homeDirectory(forUser:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the home directory for the specified user.

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
static func homeDirectory(forUser user: String) -> URL?
```

## Return Value

The home directory for the specified user.

## Parameters

- `user`: The system user name for a given user.

## See Also

### Accessing home and user directories
- [static func currentDirectory() -> URL](./currentdirectory%28%29.md)
  Returns the working directory of the current process.
- [static var homeDirectory: URL](./homedirectory.md)
  The home directory for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/homedirectory(foruser:))*