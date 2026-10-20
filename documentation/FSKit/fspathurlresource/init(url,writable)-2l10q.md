# init(url:writable:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a path URL resource.

**Availability**:
- macOS 26.0+

## Declaration

```swift
init(url URL: URL, writable: Bool)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL writable:(BOOL) writable;
```

## Parameters

- `URL`: A URL in the system file space that represents the contents of a file system. This parameter uses the `file:` scheme.
- `writable`: A Boolean value that indicates whether the file system supports writing to the contents of the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspathurlresource/init(url:writable:)-2l10q)*