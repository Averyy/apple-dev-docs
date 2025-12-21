# AskError.systemError(underlyingError:)

**Framework**: PermissionKit  
**Kind**: case

Indicates a system error occurred with underlying details.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- Unknown ?+ - Deprecated
- visionOS 26.1+

## Declaration

```swift
case systemError(underlyingError: any Error)
```

## See Also

- [AskError.unknown](askerror/unknown.md)
  Indicates an unknown error response.
- [AskError.communicationLimitsNotEnabled](askerror/communicationlimitsnotenabled.md)
  Indicates communication limits isn’t enabled to send permission requests.
- [AskError.contactSyncNotSetup](askerror/contactsyncnotsetup.md)
  Indicates contact sync isn’t enabled to send permission requests.
- [AskError.invalidQuestion](askerror/invalidquestion.md)
  Indicates your permission request is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askerror/systemerror(underlyingerror:))*