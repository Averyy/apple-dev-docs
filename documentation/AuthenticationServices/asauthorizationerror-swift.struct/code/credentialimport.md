# ASAuthorizationError.Code.credentialImport

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

The credential import request failed.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
case credentialImport
```

```c
ASAuthorizationErrorCredentialImport
```

#### Discussion

Details are available in the error’s [`userInfo`](../../../Foundation/nserror/userinfo.md).

## See Also

### Codes
- [ASAuthorizationError.Code.canceled](./canceled.md)
  The user canceled the authorization attempt.
- [ASAuthorizationError.Code.failed](./failed.md)
  The authorization attempt failed.
- [ASAuthorizationError.Code.invalidResponse](./invalidresponse.md)
  The authorization request received an invalid response.
- [ASAuthorizationError.Code.notHandled](./nothandled.md)
  The authorization request wasn’t handled.
- [ASAuthorizationError.Code.unknown](./unknown.md)
  The authorization attempt failed for an unknown reason.
- [ASAuthorizationError.Code.notInteractive](./notinteractive.md)
  The authorization request isn’t interactive.
- [ASAuthorizationError.Code.credentialExport](./credentialexport.md)
  The credential export request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationerror-swift.struct/code/credentialimport)*