# AskError.systemError(underlyingError:)

**Framework**: PermissionKit  
**Kind**: case  
**Role**: Case

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.1+

> **Deprecated**: The underlying error is now propogated directly.

## Declaration

```swift
case systemError(underlyingError: any Error)
```

## See Also

### Handling errors
- [AskError.unknown](./unknown.md)
  Indicates an unknown error response.
- [AskError.communicationLimitsNotEnabled](./communicationlimitsnotenabled.md)
  Indicates communication limits isn’t enabled to send permission requests.
- [AskError.contactSyncNotSetup](./contactsyncnotsetup.md)
  Indicates contact sync isn’t enabled to send permission requests.
- [AskError.invalidQuestion](./invalidquestion.md)
  Indicates your permission request is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askerror/systemerror(underlyingerror:))*