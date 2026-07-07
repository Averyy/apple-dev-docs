# isFileViewerRequest

**Framework**: File Provider  
**Kind**: property

A Boolean value that indicates whether the request came from Finder or related system file browsers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isFileViewerRequest: Bool { get }
```

## See Also

- [var domainVersion: NSFileProviderDomainVersion?](nsfileproviderrequest/domainversion.md)
  The version of the domain for the request.
- [var requestingExecutable: URL?](nsfileproviderrequest/requestingexecutable.md)
  The URL of the requesting executable.
- [var isSystemRequest: Bool](nsfileproviderrequest/issystemrequest.md)
  A Boolean value that indicates whether the request came from a system process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest/isfileviewerrequest)*