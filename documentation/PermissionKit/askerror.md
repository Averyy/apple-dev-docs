# AskError

**Framework**: PermissionKit  
**Kind**: enum

Represents errors you encounter when asking a person to send a communication permission question.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.1+

## Declaration

```swift
enum AskError
```

## Topics

### Handling errors
- [AskError.unknown](askerror/unknown.md)
  Indicates an unknown error response.
- [AskError.communicationLimitsNotEnabled](askerror/communicationlimitsnotenabled.md)
  Indicates communication limits isn’t enabled to send permission requests.
- [AskError.contactSyncNotSetup](askerror/contactsyncnotsetup.md)
  Indicates contact sync isn’t enabled to send permission requests.
- [AskError.invalidQuestion](askerror/invalidquestion.md)
  Indicates your permission request is invalid.
- [case systemError(underlyingError: any Error)](askerror/systemerror(underlyingerror:).md)
### Enumeration Cases
- [AskError.notAvailable](askerror/notavailable.md)
### Instance Properties
- [var errorDescription: String?](askerror/errordescription.md)
  The localized description of the error.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askerror)*