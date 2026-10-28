# requestingExecutable

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The URL of the requesting executable.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var requestingExecutable: URL? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSURL * requestingExecutable;
```

## Discussion

This property is `nil` unless the device has a Mobile Device Management (MDM) profile, and the profile’s administrator installed the file provider’s app using the MDM profile.

## See Also

### Accessing Application Information
- [var domainVersion: NSFileProviderDomainVersion?](./domainversion.md)
  The version of the domain for the request.
- [var isFileViewerRequest: Bool](./isfileviewerrequest.md)
  A Boolean value that indicates whether the request came from Finder or related system file browsers.
- [var isSystemRequest: Bool](./issystemrequest.md)
  A Boolean value that indicates whether the request came from a system process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderrequest/requestingexecutable)*