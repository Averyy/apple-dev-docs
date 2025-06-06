# Sessions API Result Codes

**Framework**: Security

Recognize result codes specific to the sessions API.

#### Discussion

Use the [`SecCopyErrorMessageString(_:_:)`](seccopyerrormessagestring(_:_:).md) function to obtain a human readable string corresponding to these status codes.

The functions of the sessions API may also return result codes from the authorization services API listed in [`Authorization Services Result Codes`](authorization-services-result-codes.md) or the general codes listed in [`Security Framework Result Codes`](security-framework-result-codes.md).

## Topics

### Codes
- [var errSessionSuccess: OSStatus](errsessionsuccess.md)
  The operation completed successfully.
- [var errSessionInvalidId: OSStatus](errsessioninvalidid.md)
  Detected an invalid session ID.
- [var errSessionInvalidAttributes: OSStatus](errsessioninvalidattributes.md)
  Detected an invalid set of request attribute bits.
- [var errSessionAuthorizationDenied: OSStatus](errsessionauthorizationdenied.md)
  Authorization denied.
- [var errSessionValueNotSet: OSStatus](errsessionvaluenotset.md)
  The requested session attribute has not been set.
- [var errSessionInternal: OSStatus](errsessioninternal.md)
  An unrecognized internal error occurred.
- [var errSessionInvalidFlags: OSStatus](errsessioninvalidflags.md)
  Encountered invalid flags or options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sessions-api-result-codes)*