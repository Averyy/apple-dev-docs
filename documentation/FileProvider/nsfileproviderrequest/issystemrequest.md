# isSystemRequest

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request came from a system process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isSystemRequest: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isSystemRequest;
```

#### Discussion

System requests occur, for example, when the system needs to update a file after receiving a push notification about a change from the remote storage.

## See Also

### Accessing Application Information
- [var domainVersion: NSFileProviderDomainVersion?](./domainversion.md)
  The version of the domain for the request.
- [var requestingExecutable: URL?](./requestingexecutable.md)
  The URL of the requesting executable.
- [var isFileViewerRequest: Bool](./isfileviewerrequest.md)
  A Boolean value that indicates whether the request came from Finder or related system file browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest/issystemrequest)*