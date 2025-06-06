# Authorization Services Result Codes

**Framework**: Security

Recognize result codes specific to the authorization services API.

#### Overview

Use the [`SecCopyErrorMessageString(_:_:)`](seccopyerrormessagestring(_:_:).md) function to obtain a human readable string corresponding to these status codes.

The functions of the [`Authorization Services`](authorization-services.md) API may also return the general codes listed in [`Security Framework Result Codes`](security-framework-result-codes.md).

## Topics

### Codes
- [var errAuthorizationSuccess: OSStatus](errauthorizationsuccess.md)
  The operation completed successfully.
- [var errAuthorizationInvalidSet: OSStatus](errauthorizationinvalidset.md)
  The set parameter is invalid.
- [var errAuthorizationInvalidRef: OSStatus](errauthorizationinvalidref.md)
  The authorization parameter is invalid.
- [var errAuthorizationInvalidTag: OSStatus](errauthorizationinvalidtag.md)
  The tag parameter is invalid.
- [var errAuthorizationInvalidPointer: OSStatus](errauthorizationinvalidpointer.md)
  The authorizedRights parameter is invalid.
- [var errAuthorizationDenied: OSStatus](errauthorizationdenied.md)
  The Security Server denied authorization for one or more requested rights.
- [var errAuthorizationCanceled: OSStatus](errauthorizationcanceled.md)
  The user canceled the operation.
- [var errAuthorizationInteractionNotAllowed: OSStatus](errauthorizationinteractionnotallowed.md)
  The Security Server denied authorization because no user interaction is allowed.
- [var errAuthorizationInternal: OSStatus](errauthorizationinternal.md)
  An unrecognized internal error occurred.
- [var errAuthorizationExternalizeNotAllowed: OSStatus](errauthorizationexternalizenotallowed.md)
  The Security Server denied externalization of the authorization reference.
- [var errAuthorizationInternalizeNotAllowed: OSStatus](errauthorizationinternalizenotallowed.md)
  The Security Server denied internalization of the authorization reference.
- [var errAuthorizationInvalidFlags: OSStatus](errauthorizationinvalidflags.md)
  The flags parameter is invalid.
- [var errAuthorizationToolExecuteFailure: OSStatus](errauthorizationtoolexecutefailure.md)
  The tool failed to execute.
- [var errAuthorizationToolEnvironmentError: OSStatus](errauthorizationtoolenvironmenterror.md)
  The attempt to execute the tool failed to return a success or an error code.
- [var errAuthorizationBadAddress: OSStatus](errauthorizationbadaddress.md)
  The requested socket address is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorization-services-result-codes)*