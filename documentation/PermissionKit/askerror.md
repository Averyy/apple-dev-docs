# AskError

**Framework**: PermissionKit  
**Kind**: enum

Represents errors you encounter when asking a person to send a communication permission question.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
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
  Indicates a system error occurred with underlying details.
### Enumeration Cases
- [AskError.notAvailable](askerror/notavailable.md)
  Indicates the person doesn’t meet the requirements for sending permission requests.
### Instance Properties
- [var errorDescription: String?](askerror/errordescription.md)
  The localized description of the error.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askerror)*