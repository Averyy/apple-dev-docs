# FamilyControlsError.unavailable

**Framework**: Family Controls  
**Kind**: case  
**Role**: Case

The system failed to set up the Family Control framework.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+

## Declaration

```swift
case unavailable
```

#### Discussion

To access data, the user must be in a region that supports data access.

## See Also

### Error values
- [FamilyControlsError.invalidAccountType](./invalidaccounttype.md)
  The device isn’t signed into a valid iCloud account.
- [FamilyControlsError.authorizationConflict](./authorizationconflict.md)
  Another authorized app already provides parental controls.
- [FamilyControlsError.authorizationCanceled](./authorizationcanceled.md)
  The parent or guardian canceled a request for authorization.
- [FamilyControlsError.invalidArgument](./invalidargument.md)
  The method’s arguments are invalid.
- [FamilyControlsError.restricted](./restricted.md)
  A restriction prevents your app from using Family Controls on this device.
- [FamilyControlsError.networkError](./networkerror.md)
  The device must be connected to the network in order to enroll with parental controls.
- [FamilyControlsError.authenticationMethodUnavailable](./authenticationmethodunavailable.md)
  The device must have a passcode set in order for an individual to enroll with parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familycontrolserror/unavailable)*