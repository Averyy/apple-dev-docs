# kSMErrorAuthorizationFailure

**Framework**: Service Management  
**Kind**: var

The authorization requested failed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
var kSMErrorAuthorizationFailure: Int { get }
```

#### Discussion

The request requires authorization (such as, adding a job to the [`kSMDomainSystemLaunchd`](ksmdomainsystemlaunchd.md)), but the `AuthorizationRef` doesn’t contain the required right.

## See Also

- [var kSMErrorAlreadyRegistered: Int](ksmerroralreadyregistered.md)
  The application is already registered.
- [var kSMErrorInternalFailure: Int](ksmerrorinternalfailure.md)
  An internal failure has occurred.
- [var kSMErrorInvalidPlist: Int](ksmerrorinvalidplist.md)
  The app’s property list is invalid.
- [var kSMErrorInvalidSignature: Int](ksmerrorinvalidsignature.md)
  The app’s code signature doesn’t meet the requirements to perform the operation.
- [var kSMErrorJobMustBeEnabled: Int](ksmerrorjobmustbeenabled.md)
- [var kSMErrorJobNotFound: Int](ksmerrorjobnotfound.md)
  The system can’t find the specified job.
- [var kSMErrorJobPlistNotFound: Int](ksmerrorjobplistnotfound.md)
- [var kSMErrorLaunchDeniedByUser: Int](ksmerrorlaunchdeniedbyuser.md)
  The user denied the app’s launch request.
- [var kSMErrorServiceUnavailable: Int](ksmerrorserviceunavailable.md)
  The service necessary to perform this operation is unavailable or is no longer accepting requests.
- [var kSMErrorToolNotValid: Int](ksmerrortoolnotvalid.md)
  The specified path doesn’t exist or the helper tool at the specified path isn’t valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/ksmerrorauthorizationfailure)*