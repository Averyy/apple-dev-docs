# domainVersion

**Framework**: File Provider  
**Kind**: property

The version of the domain for the request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var domainVersion: NSFileProviderDomainVersion? { get }
```

#### Discussion

If the file provider extension doesn’t implement the [`NSFileProviderDomainState`](nsfileproviderdomainstate.md) protocol, this property is `nil`.

## See Also

- [var requestingExecutable: URL?](nsfileproviderrequest/requestingexecutable.md)
  The URL of the requesting executable.
- [var isFileViewerRequest: Bool](nsfileproviderrequest/isfileviewerrequest.md)
  A Boolean value that indicates whether the request came from Finder or related system file browsers.
- [var isSystemRequest: Bool](nsfileproviderrequest/issystemrequest.md)
  A Boolean value that indicates whether the request came from a system process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest/domainversion)*