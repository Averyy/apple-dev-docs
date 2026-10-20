# init(scheme:host:path:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly created NSURL with a specified scheme, host, and path.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.11
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use NSURLComponents instead, which lets you create a valid URL with any valid combination of URL components and subcomponents (not just scheme, host and path), and lets you set components and subcomponents with either percent-encoded or un-percent-encoded strings.

## Declaration

```swift
convenience init?(scheme: String, host: String?, path: String)
```

```objc
- (instancetype) initWithScheme:(NSString *) scheme host:(NSString *) host path:(NSString *) path;
```

#### Return Value

The newly initialized NSURL object.

#### Discussion

This method automatically uses percent encoding to escape the `path` and `host` parameters.

## Parameters

- `scheme`: The scheme for the NSURL object. For example, in the URL `http://www.example.com/index.html`, the scheme is `http`.
- `host`: The host for the NSURL object (for example, `www.example.com`). May be the empty string.
- `path`: The path for the NSURL object (for example, `/index.html`). If the path begins with a tilde, you must first expand it by calling [`expandingTildeInPath`](../nsstring/expandingtildeinpath.md).

## See Also

### Related Documentation
- [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [URL Loading System](../url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(scheme:host:path:))*