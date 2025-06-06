# init(scheme:host:path:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly created NSURL with a specified scheme, host, and path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(scheme: String, host: String?, path: String)
```

#### Return Value

The newly initialized NSURL object.

#### Discussion

This method automatically uses percent encoding to escape the `path` and `host` parameters.

## Parameters

- `scheme`: The scheme for the NSURL object. For example, in the URL  , the scheme is  .
- `host`: The host for the NSURL object (for example,  ). May be the empty string.
- `path`: The path for the NSURL object (for example,  ). If the path begins with a tilde, you must first expand it by calling  .

## See Also

- [File System Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(scheme:host:path:))*