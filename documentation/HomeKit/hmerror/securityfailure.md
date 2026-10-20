# securityFailure

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

A security failure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var securityFailure: HMError.Code { get }
```

## See Also

### Detecting authorization errors
- [static var invalidOrMissingAuthorizationData: HMError.Code](./invalidormissingauthorizationdata.md)
  An error indicating the authorization data is invalid or missing.
- [static var locationForHomeDisabled: HMError.Code](./locationforhomedisabled.md)
  An error indicating the home’s location is disabled.
- [static var homeAccessNotAuthorized: HMError.Code](./homeaccessnotauthorized.md)
  An error indicating access to the home is not authorized.
- [static var insufficientPrivileges: HMError.Code](./insufficientprivileges.md)
  An error indicating insufficient privileges for the operation.
- [static var messageAuthenticationFailed: HMError.Code](./messageauthenticationfailed.md)
  A message authentication failure.
- [static var notAuthorizedForLocationServices: HMError.Code](./notauthorizedforlocationservices.md)
  An error indicating location services are not authorized.
- [static var notAuthorizedForMicrophoneAccess: HMError.Code](./notauthorizedformicrophoneaccess.md)
  An error indicating microphone access is not authorized.
- [static var notSignedIntoiCloud: HMError.Code](./notsignedintoicloud.md)
  An error indicating the user is not signed into iCloud.
- [static var ownershipFailure: HMError.Code](./ownershipfailure.md)
  The ownership code did not match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/securityfailure)*