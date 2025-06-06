# requestingExecutable

**Framework**: File Provider  
**Kind**: property

The URL of the requesting executable.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var requestingExecutable: URL? { get }
```

#### Discussion

This property is `nil` unless the device has a Mobile Device Management (MDM) profile, and the profile’s administrator installed the file provider’s app using the MDM profile.

## See Also

- [var domainVersion: NSFileProviderDomainVersion?](nsfileproviderrequest/domainversion.md)
  The version of the domain for the request.
- [var isFileViewerRequest: Bool](nsfileproviderrequest/isfileviewerrequest.md)
  A Boolean value that indicates whether the request came from Finder or related system file browsers.
- [var isSystemRequest: Bool](nsfileproviderrequest/issystemrequest.md)
  A Boolean value that indicates whether the request came from a system process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest/requestingexecutable)*