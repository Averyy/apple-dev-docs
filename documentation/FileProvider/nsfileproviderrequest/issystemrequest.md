# isSystemRequest

**Framework**: File Provider  
**Kind**: property

A Boolean value that indicates whether the request came from a system process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isSystemRequest: Bool { get }
```

#### Discussion

System requests occur, for example, when the system needs to update a file after receiving a push notification about a change from the remote storage.

## See Also

- [var domainVersion: NSFileProviderDomainVersion?](nsfileproviderrequest/domainversion.md)
  The version of the domain for the request.
- [var requestingExecutable: URL?](nsfileproviderrequest/requestingexecutable.md)
  The URL of the requesting executable.
- [var isFileViewerRequest: Bool](nsfileproviderrequest/isfileviewerrequest.md)
  A Boolean value that indicates whether the request came from Finder or related system file browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest/issystemrequest)*